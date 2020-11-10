from ..base import models as base
from ..supplier import models as supplier
from django.db import models
import uuid


from core import constants


class TourGroupBase(base.BaseModel):
    id = models.CharField(primary_key=True, default=uuid.uuid4, editable=False, max_length=255)
    supplier = models.ForeignKey(supplier.SupplierBase, on_delete=models.CASCADE, null=False)
    supplier_tour_code = models.CharField(max_length=256)
    day_amount = models.IntegerField()
    name = models.CharField(max_length=256)
    is_recommend = models.IntegerField(constants.IsRecommendStatus.OFF)


class TourGroupLocation(base.BaseModel):
    id = models.AutoField(primary_key=True)
    tour_group = models.ForeignKey(TourGroupBase, on_delete=models.CASCADE, null=False)
    type = models.IntegerField()
    option = models.IntegerField()
