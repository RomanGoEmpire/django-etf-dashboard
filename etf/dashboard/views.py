import json

from dashboard.models import *
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View


def index(request):
    return HttpResponse("Hello, world. You're at the dashboard index.")


def total_revenue(request):
    total_revenue = Consultation.total_revenue()
    return HttpResponse(total_revenue)


def total_cost(request):
    total_cost = Cost.total_costs()
    return HttpResponse(total_cost)


def total_profit(request):
    total_profit = Company.total_profit()
    return HttpResponse(total_profit)


def total_cost_revenue_profit(request):
    total_cost = Cost.total_costs()
    total_revenue = Consultation.total_revenue()
    total_profit = Company.total_profit()
    return JsonResponse(
        {
            "total_cost": total_cost,
            "total_revenue": total_revenue,
            "total_profit": total_profit,
        }
    )


def consultation_count_by_duration(request):
    consultation_count_by_duration = Consultation.consultation_count_by_duration()
    return JsonResponse(consultation_count_by_duration, safe=False)


def consultation_count_by_employee(request):
    consultation_count_by_employee = Consultation.consultation_count_by_employee()
    print(consultation_count_by_employee)
    return JsonResponse(consultation_count_by_employee, safe=False)


def revenue_by_interval(request, interval):
    revenue_by_interval = Consultation.revenue_by_interval(interval)
    return JsonResponse(revenue_by_interval, safe=False)


def volume_per_etf(request):
    volume_per_etf = Transaction.get_volume_per_etf()
    sorted_volume_per_etf = dict(
        sorted(volume_per_etf.items(), key=lambda x: x[1], reverse=True)
    )
    return JsonResponse(sorted_volume_per_etf, safe=False)


def volume_per_client(request):
    volume_per_client = Transaction.get_volume_client()
    return JsonResponse(volume_per_client, safe=False)


def chart(request):
    data = Transaction.get_volume_client()
    return render(request, "chart.html", {"data": json.dumps(data)})
