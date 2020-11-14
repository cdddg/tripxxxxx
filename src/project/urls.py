from django.conf import settings
from django.urls import include, path
from django.views.decorators.csrf import csrf_exempt

from services.graphql.view import BaseGraphQLView
import services.rest

urlpatterns = [
    # path('admin/', admin.site.urls),
    path("api/v1/rest/", include(services.rest.urls)),
    path("api/v1/graphql", csrf_exempt(BaseGraphQLView.as_view(graphiql=True))),
]


if settings.DEBUG:
    urlpatterns += [path("api/v1/silk", include("silk.urls", namespace="silk"))]
