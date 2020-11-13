# from .. importBaseModel

# from django.db import models
# import uuid
# from core import constants

from datetime import datetime

from django.db import models


class BaseManager(models.Manager):
    def bulk_insert(self, *args, **kwargs):
        return super().bulk_create(*args, **kwargs)

    def insert(self, *args, **kwargs):
        return super().create(*args, **kwargs)

    def all(self):
        return super().all()

    def get(self, *args, **kwargs):
        return super().get(deleted_at=None, *args, **kwargs)

    def filter(self, **kwargs):
        kwargs = {k: v for k, v in kwargs.items() if v is not None}
        return super().filter(deleted_at=None, **kwargs)

    def update(self, id, **kwargs):
        return self.filter(id=id).update(**kwargs)

    def delete(self, id):
        return self.filter(id=id).update(deleted_at=datetime.utcnow())

    def hard_delete(self, id):
        return super.filter(id=id).delete()

    def order_by(self, **kwargs):
        return super().order_by(**kwargs)

    def sort(self, sort_type: str, **kwargs):
        sort_type = sort_type.upper()
        if sort_type == "ASC":
            return self
        elif sort_type == "DESC":
            return super().desc(**kwargs)
        else:
            raise ValueError("orm.base.models.BaseManager.sort.sort_type")


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    objects = models.Manager()
    op = BaseManager()  # operation

    class Meta:
        abstract = True

    @property
    def dict(self):
        return {k: v for k, v in vars(self).items() if not k.startswith("_")}
