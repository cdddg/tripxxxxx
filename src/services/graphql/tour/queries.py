import graphene

from project.di import InteractorFactory

from . import node

tour_interactor = InteractorFactory().tour


class Query(graphene.ObjectType):
    tour_groups = graphene.List(node.TourGroupNode, input=graphene.Argument(node.QueryTourGroupsInput, required=True))

    def resolve_tour_groups(self, info, input):
        info.context.member_id = input.get("member_id")
        input = tour_interactor.node.GetTourGroupsInput(**input)
        return tour_interactor.func.get_tour_groups(input)
