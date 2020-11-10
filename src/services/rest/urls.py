from django.urls import include
from django.urls import path

from . import tour

urlpatterns = [
    path("tour/", include(tour.urls)),
]
