from ..base import models as base

import uuid

from django.db import models
from core import constants
from ..supplier import models as supplier
from ..member import models as member
from ..tour import models as tour


class ScoreBaseLog(base.BaseModel):
    id = models.AutoField(primary_key=True)
    supplier = models.ForeignKey(supplier.SupplierBase, on_delete=models.CASCADE, null=False)
    member = models.ForeignKey(member.MemberBase, on_delete=models.CASCADE, null=False)
    tour_group = models.ForeignKey(tour.TourGroupBase, on_delete=models.CASCADE, null=False)
    category = models.IntegerField()
    food_score = models.CharField(max_length=256)
    traffic_score = models.CharField(max_length=256)
    scheduler_score = models.CharField(max_length=256)
    tour_guide_score = models.CharField(max_length=256)
    stay_score = models.CharField(max_length=256)
    description = models.CharField(max_length=2048)

    class Meta:
        db_table = 'score_base_log'
