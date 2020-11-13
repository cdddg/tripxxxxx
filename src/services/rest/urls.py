from django.urls import include, path

from ..rest import _tmp

urlpatterns = [
    path("tmp/", include(_tmp.urls)),
]
