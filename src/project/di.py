import types

import interactors


class InteractorFactory:
    @property
    def member(self):
        obj = types.SimpleNamespace()
        obj.func = interactors.member.MemberInteractor()
        obj.node = interactors.member.node
        return obj

    @property
    def supplier(self):
        obj = types.SimpleNamespace()
        obj.func = interactors.supplier.TourInteractor()
        obj.node = interactors.supplier.node
        return obj

    @property
    def tour(self):
        obj = types.SimpleNamespace()
        obj.func = interactors.tour.TourInteractor()
        obj.node = interactors.tour.node
        return obj
