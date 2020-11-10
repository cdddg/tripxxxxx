# from .. importBaseModel

# from django.db import models
# import uuid
# from core import constants

from django.db import models


class BaseManager(models.Manager):
    pass


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    objects = BaseManager()

    class Meta:
        abstract = True