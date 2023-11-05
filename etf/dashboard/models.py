from django.db import models


class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthday = models.DateField()
    GENDER_OPTIONS = [("M", "male"), ("F", "female")]
    gender = models.CharField(max_length=2, choices=GENDER_OPTIONS)
    adress = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=30)


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthday = models.DateField()
    gender = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=30)
    hire_date = models.DateField()
    role = models.CharField(max_length=50)
    salary = models.IntegerField()


class Consultation(models.Model):
    employee_id = models.ForeignKey(Employee, on_delete=models.DO_NOTHING)
    client_id = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
    date = models.DateField()
    duration = models.SmallIntegerField()
    cost = models.IntegerField()


class ETF(models.Model):
    id = models.CharField(max_length=4, primary_key=True)
    name = models.CharField(max_length=200)
    exchange = models.CharField(max_length=50)
    ipo_date = models.DateField()
    status = models.CharField(max_length=50)


class Timestamp(models.Model):
    etf_id = models.ForeignKey(ETF, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    volume = models.IntegerField()


class Transaction(models.Model):
    client_id = (models.ForeignKey(Client, on_delete=models.DO_NOTHING),)
    etf_id = models.ForeignKey(ETF, on_delete=models.DO_NOTHING)
    date = models.DateTimeField()
    option = models.CharField(max_length=4)
    amount = models.IntegerField()
    frequency = models.CharField(max_length=20)


class Cost(models.Model):
    date = models.DateField()
    cost = models.FloatField()
    reason = models.CharField(max_length=50)
    target = models.CharField(max_length=24)
