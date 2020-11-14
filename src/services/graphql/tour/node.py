import graphene

from project import di

from .. import base

member_interactor = di.InteractorFactory().member


class _QueryOrderByInput(graphene.InputObjectType):
    by = graphene.String(required=True)
    sort = graphene.Int()


class QueryTourGroupsInput(graphene.InputObjectType):
    page = graphene.Int(required=True)
    size = graphene.Int(required=True)
    order_by = graphene.Field(base.constants.TourGroupInputOrderBy)
    member_id = graphene.String()


class TourGroupBucketNode(graphene.ObjectType):
    date = base.TimeStampScalar()
    sku = graphene.Int()
    sell = graphene.Int()
    adult_price = graphene.Float()
    child_price = graphene.Float()
    baby_price = graphene.Float()
    remark = graphene.String()
    go_from = graphene.Field(base.constants.TourGroupLocationOpition)
    back_from = graphene.Field(base.constants.TourGroupLocationOpition)


class TourGroupNode(graphene.ObjectType):
    id = graphene.String()
    supplier_id = graphene.String()
    supplier_tour_code = graphene.String()
    day_amount = graphene.Int()
    name = graphene.String()
    is_recommend = graphene.Field(base.constants.IsRecommendStatus)
    default_price = graphene.Float()
    price = graphene.Float()
    score = graphene.Float()
    member_favorite = graphene.Field(base.constants.IsMemberFavorit)
    bucket = graphene.List(lambda: TourGroupBucketNode)
    tags = graphene.List(base.constants.TourGroupTag)
    locations = graphene.List(base.constants.TourGroupLocationOpition)

    def resolve_bucket(root, info):
        return info.context.tour_group_bucket_loader.load(root.id)

    def resolve_member_favorite(root, info):
        return info.context.tour_group_member_favorite_loader.load((info.context.member_id, root.id))

    def resolve_tags(root, info):
        return info.context.tour_group_tag_loader.load(root.id)

    def resolve_locations(root, info):
        return info.context.tour_group_location_loader.load(root.id)
