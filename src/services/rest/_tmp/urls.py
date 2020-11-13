from django.urls import path

from . import views

urlpatterns = [
    path("insert_fake_data", views.insert_fake_data),
]

