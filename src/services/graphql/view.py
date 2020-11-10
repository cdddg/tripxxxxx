import logging
import traceback

from django.conf import settings
from graphene_django.views import GraphQLView

from graphql import GraphQLError
from graphql.error.located_error import GraphQLLocatedError


class BaseGraphQLView(GraphQLView):
    pass
