from core import constants
from orm import raw, tour

from . import node
from ..base import BaseInteractor


class TourInteractor(BaseInteractor):
    def get_tour_group(self, id):
        return tour.models.TourGroupBase(id)

    def get_tour_groups(self, input: node.GetTourGroupsInput):
        input = input.dict
        page = input.pop("page")
        size = input.pop("size")
        order_by = input.get("order_by")
        if order_by:
            field, sort_type = constants.TourGroupInputOrderBy(order_by).parse()
        else:
            field, sort_type = None, None

        rows = tour.models.TourGroupBase.op.raw(raw.get_tour_groups_rows(order_by_field=field, sort_type=sort_type))
        print(rows.query)
        # for row in rows:
        #     print(row.dict)

        return rows[size * (page - 1) : size * page]
