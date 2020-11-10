import abc


class BaseInteractor(abc.ABC):
    def __init__(self, orm=None):
        self.orm = orm
