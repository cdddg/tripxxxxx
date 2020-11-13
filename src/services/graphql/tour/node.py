import graphene
from .. import base

from core import constants



class _QueryOrderByInput(graphene.InputObjectType):
    by = graphene.String(required=True)
    sort = graphene.Int()

class QueryTourGroupsInput(graphene.InputObjectType):
    page = graphene.Int(required=True)
    size = graphene.Int(required=True)
    order_by = graphene.Field(base.constants.TourGroupInputOrderBy)


class TourGroupNode(graphene.ObjectType):
    id = graphene.String()
    supplier_id = graphene.String()
    supplier_tour_code = graphene.String()
    day_amount = graphene.Int()
    name = graphene.String()
    is_recommend = graphene.Int()
    default_price = graphene.Float()
    score = graphene.Float()
    date = base.TimeStampScalar()
    sku = graphene.Int()
    sell = graphene.Int()
    adult_price = graphene.Float()
    child_price = graphene.Float()
    baby_price = graphene.Float()
    remark = graphene.String()
    go_from = graphene.Field(base.constants.TourGroupLocationOpition)
    back_from = graphene.Field(base.constants.TourGroupLocationOpition)
