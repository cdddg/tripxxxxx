from collections import defaultdict
from datetime import date

from promise import Promise, dataloader

from orm import member, tour


class TourGroupBucketLoader(dataloader.DataLoader):
    def batch_load_fn(self, ids):
        results = defaultdict(list)
        for row in iter(tour.models.TourGroupBucket.op.filter(tour_group__id__in=ids, date__gte=date.today())):
            results[row.tour_group_id].append(row)
        return Promise.resolve([results.get(id, [])[0:4] for id in ids])


class TourGroupMemberFavoriteLoader(dataloader.DataLoader):
    def batch_load_fn(self, collections_ids):
        ids = []
        for member_id, tour_group_id in collections_ids:
            ids.append(tour_group_id)

        results = defaultdict(list)
        if member_id is not None:
            for row in iter(member.models.MemberFavorite.op.filter(tour_group__id__in=ids, member_id=member_id)):
                results[row.tour_group_id] = 1

        return Promise.resolve([results.get(id, 0) for id in ids])


class TourGroupTagLoader(dataloader.DataLoader):
    def batch_load_fn(self, ids):
        results = defaultdict(list)
        for row in iter(tour.models.TourGroupTag.op.filter(tour_group__id__in=ids)):
            results[row.tour_group_id].append(row.tag)
        return Promise.resolve([results.get(id, []) for id in ids])


class TourGroupLocationLoader(dataloader.DataLoader):
    def batch_load_fn(self, ids):
        results = defaultdict(list)
        for row in iter(tour.models.TourGroupLocation.op.filter(tour_group__id__in=ids)):
            results[row.tour_group_id].append(row.option)
        return Promise.resolve([results.get(id, []) for id in ids])
