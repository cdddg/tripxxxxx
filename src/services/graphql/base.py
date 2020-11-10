import datetime

# from django.conf import settings
import graphene
from graphene.types import Scalar

# from django_graphql_ratelimit import ratelimit as origin_ratelimit
from graphql.language import ast


class TimeStampScalar(Scalar):
    @staticmethod
    def serialize(t):
        if isinstance(t, int):
            return t
        return round(t.timestamp())

    @classmethod
    def parse_literal(cls, node):
        if isinstance(node, ast.IntValue):
            return cls.parse_value(float(node.value))

    @staticmethod
    def parse_value(timestamp):
        return datetime.datetime.utcfromtimestamp(int(timestamp))


class CurrentTimeNode(graphene.ObjectType):
    current_time = TimeStampScalar()

    def resolve_current_time(self, info):
        return datetime.datetime.utcnow()


class HelloWorldNode(graphene.ObjectType):
    hello_world = graphene.String()

    class Meta:
        description = "first example in project"

    def resolve_hello_world(self, info):
        return 'Hello world! GraphQL'
