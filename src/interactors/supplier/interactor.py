from ..base import BaseInteractor
from orm import supplier

from django.db import transaction

class SupplierInteractor(BaseInteractor):
    def get_supplier(self, id):
        return supplier.models.SupplierBase.get(id)

    def get_suppliers(self, input):
        return supplier.models.SupplierBase.filter(**dict(input))

    def __calculate_avg(self, avg, quantity, new):
        return int((avg * quantity + new) / (quantity + 1))

    def add_score(self, input):
        with transaction.atomic():
            row = supplier.models.SupplierScoreLog.create(**dict(input))

            obj = supplier.models.SupplierBase.get(input.supplier_id)
            obj.food_score = self.__calculate_avg(obj.food_score, obj.score_amount, row.food_score)
            obj.traffic_score = self.__calculate_avg(obj.traffic_score, obj.score_amount, row.traffic_score)
            obj.scheduler_score = self.__calculate_avg(obj.scheduler_score, obj.score_amount, row.scheduler_score)
            obj.tour_guide_score = self.__calculate_avg(obj.tour_guide_score, obj.score_amount, row.tour_guide_score)
            obj.stay_score = self.__calculate_avg(obj.stay_score, obj.score_amount, row.stay_score)
            obj.score_amount += 1
            obj.save()

            return row
