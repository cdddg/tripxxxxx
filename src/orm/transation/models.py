from ..base import models as base
from ..member import models as member

from django.db import models


class TransationTourGroupBase(base.BaseModel):
    id = models.AutoField(primary_key=True)

    class Meta:
        db_table = 'transation_tour_group_base'


class TransationTourGroupBaseLog(base.BaseModel):
    id = models.AutoField(primary_key=True)

    class Meta:
        db_table = 'transation_tour_group_log'
