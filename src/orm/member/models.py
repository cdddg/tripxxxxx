from ..base import models as base

import uuid

from django.db import models
from core import constants



class MemberBase(base.BaseModel):
    id = models.CharField(primary_key=True, default=uuid.uuid4, editable=False, max_length=255)
    platform = models.IntegerField(default=constants.PlatformType.TRIPRESSO)
    account = models.CharField(max_length=256)
    surname = models.CharField(max_length=256)
    given_name = models.CharField(max_length=256)
    gender = models.CharField(max_length=256)
    birthday = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    phone = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    tripresso_coin = models.IntegerField(default=0)


class MemberFavorite(base.BaseModel):
    id = models.CharField(primary_key=True, default=uuid.uuid4, editable=False, max_length=255)
    member = models.ForeignKey(MemberBase, on_delete=models.CASCADE, null=False)
    tour_group = models.ForeignKey('tour.TourGroupBase', on_delete=models.CASCADE, null=False)
