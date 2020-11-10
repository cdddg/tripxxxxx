import graphene

from . import node

from project.di import InteractorFactory

tour_interactor = InteractorFactory.tour_interactor()


class Query(graphene.ObjectType):
    pass
