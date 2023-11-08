from django.urls import path

from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("revenue/", RevenueView.as_view(), name="revenue"),
    path(
        "consultation_count_by_duration/",
        ConsultationCountByDurationView.as_view(),
        name="consultation_count_by_duration",
    ),
]
