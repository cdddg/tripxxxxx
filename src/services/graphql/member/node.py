import graphene
from .. import base


class QueryMemberInput(graphene.InputObjectType):
    id = graphene.String()


class QueryMembersInput(graphene.InputObjectType):
    platform = graphene.Field(base.constants.PlatformType)
    account = graphene.String()
    surname = graphene.String()
    given_name = graphene.String()
    gender = graphene.Field(base.constants.GenderType)
    birthday = base.TimeStampScalar()
    email = graphene.String()
    phone = graphene.String()
    address = graphene.String()
    tripresso_coin = graphene.Int()


class MemberNode(graphene.ObjectType):
    platform = graphene.Field(base.constants.PlatformType)
    account = graphene.String()
    surname = graphene.String()
    given_name = graphene.String()
    gender = graphene.Field(base.constants.GenderType)
    birthday = base.TimeStampScalar()
    email = graphene.String()
    phone = graphene.String()
    address = graphene.String()
    tripresso_coin = graphene.Int()
