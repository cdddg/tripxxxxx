from ..base import models as base
from ..member import models as member

from django.db import models
import uuid


class SupplierBase(base.BaseModel):
    id = models.CharField(primary_key=True, default=uuid.uuid4, editable=False, max_length=255)
    name = models.CharField(max_length=256)
    score_amount = models.IntegerField()
    food_score = models.CharField(max_length=256)
    traffic_score = models.CharField(max_length=256)
    scheduler_score = models.CharField(max_length=256)
    tour_guide_score = models.CharField(max_length=256)
    stay_score = models.CharField(max_length=256)
    logo_url = models.CharField(max_length=1024)


class SupplierScoreLog(base.BaseModel):
    id = models.AutoField(primary_key=True)
    supplier = models.ForeignKey(SupplierBase, on_delete=models.CASCADE, null=False)
    member = models.ForeignKey(member.MemberBase, on_delete=models.CASCADE, null=False)
    tour_group = models.ForeignKey('tour.TourGroupBase', on_delete=models.CASCADE, null=False)
    category = models.IntegerField()
    food_score = models.CharField(max_length=256)
    traffic_score = models.CharField(max_length=256)
    scheduler_score = models.CharField(max_length=256)
    tour_guide_score = models.CharField(max_length=256)
    stay_score = models.CharField(max_length=256)
    description = models.CharField(max_length=2048)
