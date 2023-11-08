from dashboard.models import *
from django.http import HttpResponse, JsonResponse
from django.views import View

# Transaction.total_transactions()
# Consultation.consultation_count_by_duration()
# Consultation.revenue_by_interval(interval)

# Cost.total_costs()
# Cost.cost_breakdown()
# Company.revenue()


def index(request):
    return HttpResponse("Hello, world. You're at the dashboard index.")
