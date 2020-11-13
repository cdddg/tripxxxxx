import graphene

from . import node

from project.di import InteractorFactory

tour_interactor = InteractorFactory().tour


class Query(graphene.ObjectType):
    tour_groups = graphene.List(
        node.TourGroupNode,
        input=graphene.Argument(node.QueryTourGroupsInput, required=True)
    )

    def resolve_tour_groups(self, info, input):
        input = tour_interactor.node.GetTourGroupsInput(**input)
        return tour_interactor.func.get_tour_groups(input)
