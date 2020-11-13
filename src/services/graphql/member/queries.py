import graphene

from project.di import InteractorFactory

from . import node

member_interactor = InteractorFactory().member


class Query(graphene.ObjectType):
    member = graphene.Field(node.MemberNode, input=graphene.Argument(node.QueryMemberInput, required=True))
    members = graphene.List(node.MemberNode, input=graphene.Argument(node.QueryMembersInput, required=True))

    def resolve_member(self, info, input=None):
        return member_interactor.func.get_member(id=input.id)

    def resolve_members(self, info, input=None):
        input = member_interactor.node.GetMembersInput(**input)
        return member_interactor.func.get_members(input)
