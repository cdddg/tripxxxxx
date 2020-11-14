import random

from django.db import connection
from django.http import HttpResponse, JsonResponse

from core import constants
from orm import fake
from project.di import InteractorFactory

tour = InteractorFactory().tour


def insert(request):
    _members = [fake.MemberBase() for i in range(50)]

    _suppliers = [fake.SupplierBase() for i in range(50)]

    _tour_groups = [fake.TourGroupBase(supplier=random.choice(_suppliers)) for i in range(100)]

    _tags = []
    for row in _tour_groups:
        for tag in constants.TourGroupTag:
            if random.choice([1, 0]):
                _tags.append(fake.TourGroupTag(tour_group=row, tag=tag.value))

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

    for member in _members:
        for tour_group in _tour_groups:
            if random.choice([1, 0, 0]):
                fake.MemberFavorite(member=member, tour_group=tour_group)

    return JsonResponse(
        {
            "resp": {
                "members": len(_members),
                "suppliers": len(_suppliers),
                "tour_group": len(_tour_groups),
            }
        }
    )


def clear(request):
    with connection.cursor() as cursor:
        cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")

        cursor.execute("truncate member_base;")
        cursor.execute("truncate member_favorite;")
        cursor.execute("truncate supplier_base;")
        cursor.execute("truncate score_base_log;")
        cursor.execute("truncate tour_group_base;")
        cursor.execute("truncate tour_group_bucket;")
        cursor.execute("truncate tour_group_tag;")
        cursor.execute("truncate tour_group_location;")

        cursor.execute("SET FOREIGN_KEY_CHECKS = 1;")

    return HttpResponse(200)
