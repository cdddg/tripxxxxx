from django.http import HttpResponse
from project.di import InteractorFactory

tour = InteractorFactory().tour
