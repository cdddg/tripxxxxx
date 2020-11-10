import interactors


class InteractorFactory:
    @classmethod
    def tour_interactor(cls):
        return interactors.tour.TourInteractor()
