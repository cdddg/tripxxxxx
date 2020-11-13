import random

from django.http import JsonResponse

from core import constants
from orm import fake
from project.di import InteractorFactory

tour = InteractorFactory().tour


def insert_fake_data(request):

    _members = [fake.MemberBase() for i in range(50)]

    _suppliers = [fake.SupplierBase() for i in range(50)]

    _tour_groups = [fake.TourGroupBase(supplier=random.choice(_suppliers)) for i in range(100)]

    _tags = []
    for row in _tour_groups:
        for tag in random.choices(list(constants.TourGroupTag)):
            _tags.append(fake.TourGroupTag(tour_group=row, tag=tag))

    _locations = []
    for row in _tour_groups:
        for i in range(random.randint(1, 5)):
            _locations.append(fake.TourGroupLocation(tour_group=row))

    _buckets = []
    for row in _tour_groups:
        from datetime import date, timedelta

        today = date.today()
        for i in range(random.randint(15, 30)):
            if random.choice([1, 1, 0]):
                _buckets.append(fake.TourGroupBucket(tour_group=row, date=today + timedelta(days=i)))

    return JsonResponse(
        {
            "resp": {
                "members": len(_members),
                "suppliers": len(_suppliers),
                "tour_group": len(_tour_groups),
            }
        }
    )
