from django.urls import path

from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("total_revenue", total_revenue, name="total_revenue"),
    path("total_cost", total_cost, name="total_cost"),
    path("total_profit", total_profit, name="total_profit"),
    path(
        "total_cost_revenue_profit",
        total_cost_revenue_profit,
        name="total_cost_revenue_profit",
    ),
    path(
        "consultation_count_by_duration",
        consultation_count_by_duration,
        name="consultation_count_by_duration",
    ),
    path(
        "consultation_count_by_employee",
        consultation_count_by_employee,
        name="consultation_count_by_employee",
    ),
    path(
        "revenue_by_interval/<str:interval>",
        revenue_by_interval,
        name="revenue_by_interval",
    ),
    path("volume_per_etf", volume_per_etf, name="volume_per_etf"),
    path("volume_per_client", volume_per_client, name="volume_per_client"),
    path("chart", chart, name="chart"),
]
