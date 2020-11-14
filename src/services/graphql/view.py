from django.utils.functional import cached_property
from graphene_django.views import GraphQLView

from . import dataloaders


class GQLContext:
    def __init__(self, request):
        self.request = request

    @cached_property
    def user(self):
        return self.request.user

    @cached_property
    def tour_group_bucket_loader(self):
        return dataloaders.TourGroupBucketLoader()

    @cached_property
    def tour_group_member_favorite_loader(self):
        return dataloaders.TourGroupMemberFavoriteLoader()

    @cached_property
    def tour_group_tag_loader(self):
        return dataloaders.TourGroupTagLoader()

    @cached_property
    def tour_group_location_loader(self):
        return dataloaders.TourGroupLocationLoader()


class BaseGraphQLView(GraphQLView):
    def get_context(self, request):
        return GQLContext(request)
