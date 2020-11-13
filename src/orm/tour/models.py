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
    score = models.FloatField()
    default_price = models.FloatField()

    class Meta:
        db_table = 'tour_group_base'


class TourGroupLocation(base.BaseModel):
    id = models.AutoField(primary_key=True)
    tour_group = models.ForeignKey(TourGroupBase, on_delete=models.CASCADE, null=False)
    type = models.IntegerField()
    option = models.IntegerField()

    class Meta:
        db_table = 'tour_group_location'


class TourGroupTag(base.BaseModel):
    id = models.AutoField(primary_key=True)
    tour_group = models.ForeignKey(TourGroupBase, on_delete=models.CASCADE, null=False)
    tag = models.CharField(max_length=128)

    class Meta:
        db_table = 'tour_group_tag'
        unique_together = ('tour_group_id', 'tag')


class TourGroupBucket(base.BaseModel):
    id = models.CharField(primary_key=True, default=uuid.uuid4, editable=False, max_length=255)
    tour_group = models.ForeignKey(TourGroupBase, on_delete=models.CASCADE, null=False)
    date = models.DateField()
    currency = models.IntegerField()
    sku = models.IntegerField()
    sell = models.IntegerField()
    adult_price = models.FloatField()
    child_price = models.FloatField()
    baby_price = models.FloatField()
    remark = models.CharField(max_length=1024)
    transfer = models.IntegerField()
    go_from = models.IntegerField()
    back_from = models.IntegerField()

    class Meta:
        db_table = 'tour_group_bucket'
        unique_together = ('tour_group_id', 'date')


class TourBase(base.BaseModel):
    id = models.AutoField(primary_key=True)

    class Meta:
        db_table = 'tour_base'
