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
]
