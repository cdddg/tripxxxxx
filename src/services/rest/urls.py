from django.urls import include, path

from ..rest import fake

urlpatterns = [
    path("fake/", include(fake.urls)),
]
