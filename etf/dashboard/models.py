from datetime import datetime, timedelta

from django.db import models
from django.db.models import Count, Sum
from django.db.models.functions import TruncMonth, TruncQuarter, TruncYear
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField


class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthday = models.DateField()
    gender = models.CharField(max_length=1)
    adress = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=30)

    @classmethod
    def total_client(self):
        return self.objects.count()

    def __str__():
        return f"{self.first_name} {self.second_name}"


class Employee(models.Model):
    GENDER_CHOICES = [
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Other"),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthday = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email = models.EmailField(max_length=100)
    phone_number = PhoneNumberField()
    hire_date = models.DateField()
    role = models.CharField(max_length=50)
    salary = models.IntegerField()

    @classmethod
    def total_employee(self):
        return self.objects.count()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Consultation(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.DO_NOTHING)
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
    date = models.DateField()
    duration = models.SmallIntegerField()
    revenue = models.IntegerField()

    @classmethod
    def total_consultation(self):
        return self.objects.count()

    @classmethod
    def consultation_count_by_duration(cls):
        queryset = (
            cls.objects.values("duration")
            .annotate(total=Count("id"))
            .order_by("-total")
        )
        return {item["duration"]: item["total"] for item in queryset}

    @classmethod
    def consultation_count_by_employee(cls):
        queryset = (
            cls.objects.values("employee__first_name", "employee__last_name")
            .annotate(total=Count("id"))
            .order_by("-total")
        )
        return {
            f"{item['employee__first_name']} {item['employee__last_name']}": item[
                "total"
            ]
            for item in queryset
        }

    def __str__(self):
        return f"{self.employee} consulted {self.client} on {self.date}"

    @classmethod
    def revenue_by_interval(cls, interval):
        return aggregate_by_interval(cls, interval, "revenue")

    @classmethod
    def total_revenue(cls):
        return (
            round(float(cls.objects.aggregate(Sum("revenue"))["revenue__sum"]), 2) or 0
        )

    def __str__(self):
        return f"{self.employee} consulted {self.client} on {self.date}"


class ETF(models.Model):
    id = models.CharField(max_length=4, primary_key=True)
    name = models.CharField(max_length=200)
    exchange = models.CharField(max_length=50)
    ipo_date = models.DateField()
    status = models.CharField(max_length=50)

    @classmethod
    def total_etf(self):
        return self.objects.count()

    def __str__(self):
        return f"{id}"


class Timestamp(models.Model):
    etf = models.ForeignKey(ETF, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    volume = models.IntegerField()

    @classmethod
    def first_date_of_each_etf(cls):
        etfs = ETF.objects.all()
        first_dates = {}
        for etf in etfs:
            first_date = (
                cls.objects.filter(etf=etf).order_by("timestamp").first().timestamp
            )
            first_dates[etf] = first_date
        return first_dates

    def __str__(self):
        return f"{self.etf} {self.timestamp}"


class Transaction(models.Model):
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
    etf = models.ForeignKey(ETF, on_delete=models.DO_NOTHING)
    date = models.DateTimeField()
    option = models.CharField(max_length=4)
    amount = models.IntegerField()
    frequency = models.CharField(max_length=20)

    @classmethod
    def total_transactions(cls):
        return cls.objects.count()

    @classmethod
    def volume_transactions(cls, option):
        return cls.objects.filter(option=option).aggregate(Sum("amount"))["amount__sum"]

    @classmethod
    def total_frequency(cls):
        # dict of frequency and count
        frequency_count = {}
        for transaction in cls.objects.all():
            frequency = transaction.frequency
            if frequency in frequency_count:
                frequency_count[frequency] += 1
            else:
                frequency_count[frequency] = 1
        return frequency_count

    @classmethod
    def get_volume_per_etf(cls):
        # group by etf and sum amount
        volume_per_etf = cls.objects.values("etf_id").annotate(total=Sum("amount"))
        # convert to dict
        return {item["etf_id"]: item["total"] for item in volume_per_etf}

    @classmethod
    def get_volume_client(cls):
        # group by client and sum amount
        volume_per_client = (
            cls.objects.values("client__first_name", "client__last_name")
            .annotate(total=Sum("amount"))
            .order_by("-total")
        )
        # convert to dict
        return {
            f"{item['client__first_name']} {item['client__last_name']}": item["total"]
            for item in volume_per_client
        }

    def __str__(self):
        return f"{self.client} bought {self.etf} of {self.date}"


class Cost(models.Model):
    date = models.DateField()
    cost = models.FloatField()
    reason = models.CharField(max_length=50)
    target = models.CharField(max_length=24)

    def __str__(self):
        return f"{self.reason} cost {self.cost} on {self.date}"

    @classmethod
    def total_costs(cls):
        return round(cls.objects.aggregate(Sum("cost"))["cost__sum"], 2) or 0

    @classmethod
    def cost_breakdown(cls):
        return cls.objects.values("reason").annotate(total=Sum("cost"))

    @classmethod
    def cost_by_interval(cls, interval):
        return aggregate_by_interval(cls, interval, "cost")


class Company(models.Model):
    profit = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    @classmethod
    def update_total_profit(cls):
        total_costs = Cost.objects.aggregate(Sum("cost"))["cost__sum"] or 0
        total_revenue = (
            Consultation.objects.aggregate(Sum("revenue"))["revenue__sum"] or 0
        )
        company = cls.objects.first()  # assuming there's only one Company object
        company.profit = total_revenue - total_costs
        company.save()
        return company.profit

    @classmethod
    def total_profit(cls):
        cls.update_total_profit()
        return round(float(cls.objects.first().profit), 2)


@receiver([post_save, post_delete], sender=Cost)
@receiver([post_save, post_delete], sender=Consultation)
def update_company_total_revenue(sender, **kwargs):
    Company.update_total_profit()


def aggregate_by_interval(cls, interval, field):
    current_date = datetime.now().date()
    data_by_interval = {}

    if interval == "annual":
        start_date = cls.objects.order_by("date").first().date
        end_date = current_date.replace(month=12, day=31)
        date_trunc = TruncYear("date")
    elif interval == "quarterly":
        start_date = cls.objects.order_by("date").first().date
        end_date = current_date.replace(day=1) - timedelta(days=1)
        date_trunc = TruncQuarter("date")
    elif interval == "monthly":
        start_date = cls.objects.order_by("date").first().date
        end_date = current_date.replace(day=1) - timedelta(days=1)
        date_trunc = TruncMonth("date")
    else:
        raise ValueError("Invalid interval parameter")

    data_by_date = (
        cls.objects.filter(date__range=(start_date, end_date))
        .annotate(date_trunc=date_trunc)
        .values("date_trunc")
        .annotate(total=Sum(field))
    )

    for data in data_by_date:
        data_by_interval[str(data["date_trunc"])] = data["total"]

    return data_by_interval


def cost_by_interval(cls, interval):
    return cls.aggregate_by_interval(interval, "cost")


def revenue_by_interval(cls, interval):
    return cls.aggregate_by_interval(interval, "revenue")
