from django.contrib import admin
from django.urls import path
from django.urls import include

import services.rest
from django.views.decorators.csrf import csrf_exempt
from services.graphql.view import BaseGraphQLView


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('api/v1/rest/', include(services.rest.urls)),
    path('api/v1/graphql', csrf_exempt(BaseGraphQLView.as_view(graphiql=True))),
]
