from dashboard.models import *
from django.http import HttpResponse, JsonResponse
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
