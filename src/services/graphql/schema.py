import graphene
from . import base, tour


class Query(
    base.HelloWorldNode,
    base.CurrentTimeNode,
    # tour.queries.Query,
    graphene.ObjectType,
):
    pass


class Mutation(
    base.CurrentTimeNode,
    graphene.ObjectType,
):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
