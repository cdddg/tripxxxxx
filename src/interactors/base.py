import abc


class BaseInput(abc.ABC):
    @property
    def dict(self):
        return {k: v for k, v in vars(self).items() if not k.startswith("_")}


class BaseInteractor(abc.ABC):
    def __init__(self, orm=None):
        self.orm = orm
