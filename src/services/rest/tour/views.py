from django.http import HttpResponse
from project.di import InteractorFactory

tour_interactor = InteractorFactory.tour_interactor()


def hello_world(request):
    text = tour_interactor._hello_world()
    return HttpResponse(text)
