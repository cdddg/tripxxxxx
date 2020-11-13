from django.urls import include
from django.urls import path

from ..rest import _tmp

urlpatterns = [
    path("tmp/", include(_tmp.urls)),
]
