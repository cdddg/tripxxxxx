import graphene
from . import base, tour, member


class Query(
    base.HelloWorldNode,
    base.CurrentTimeNode,
    tour.queries.Query,
    member.queries.Query,
    graphene.ObjectType,
):
    pass


class Mutation(
    base.CurrentTimeNode,
    graphene.ObjectType,
):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
