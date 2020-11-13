import factory
import factory.fuzzy

from core import constants
from orm import member, score, supplier, tour


class Faker:
    @classmethod
    def name(cls):
        return factory.Faker("name", locale="zh_TW")

    @classmethod
    def email(cls):
        return factory.Faker("email", locale="zh_TW")

    @classmethod
    def first_name(cls):
        return factory.Faker("first_name", locale="zh_TW")

    @classmethod
    def last_name(cls):
        return factory.Faker("last_name", locale="zh_TW")

    @classmethod
    def date(cls):
        return factory.Faker("date", locale="zh_TW")

    @classmethod
    def phone_number(cls):
        return factory.Faker("phone_number", locale="zh_TW")

    @classmethod
    def pyint(cls, min_value=1, max_value=9999):
        return factory.Faker("pyint", locale="zh_TW", min_value=min_value, max_value=max_value)

    @classmethod
    def address(cls):
        return factory.Faker("address", locale="zh_TW")

    @classmethod
    def url(cls):
        return factory.Faker("url", locale="zh_TW")

    @classmethod
    def company(cls):
        return factory.Faker("company", locale="zh_TW")

    @classmethod
    def lexify(cls, text=None):
        return factory.Faker("lexify", text=text, locale="zh_TW")

    @classmethod
    def text(cls):
        return factory.Faker("text", locale="zh_TW")

    @classmethod
    def random_element(cls, elements):
        return factory.Faker("random_element", elements=elements, locale="zh_TW")

    @classmethod
    def uuid4(cls):
        return factory.Faker("uuid4")


class MemberBase(factory.django.DjangoModelFactory):
    class Meta:
        model = member.models.MemberBase

    # id = Faker.uuid4()
    platform = Faker.random_element([row.value for row in constants.PlatformType])
    account = Faker.email()
    email = Faker.email()
    surname = Faker.last_name()
    given_name = Faker.first_name()

    gender = Faker.random_element([row.value for row in constants.GenderType])
    birthday = Faker.date()
    phone = Faker.phone_number()
    address = Faker.address()
    tripresso_coin = Faker.pyint()


class SupplierBase(factory.django.DjangoModelFactory):
    class Meta:
        model = supplier.models.SupplierBase

    name = Faker.company()
    score_amount = Faker.pyint()
    food_score = Faker.pyint(1, 100)
    traffic_score = Faker.pyint(1, 100)
    scheduler_score = Faker.pyint(1, 100)
    tour_guide_score = Faker.pyint(1, 100)
    stay_score = Faker.pyint(1, 100)
    logo_url = Faker.url()


class TourGroupBase(factory.django.DjangoModelFactory):
    class Meta:
        model = tour.models.TourGroupBase

    supplier = factory.SubFactory(SupplierBase)
    supplier_tour_code = Faker.lexify(text="????????")
    day_amount = Faker.pyint(1, 10)
    name = Faker.text()
    is_recommend = Faker.random_element([row.value for row in constants.IsRecommendStatus])
    score = Faker.pyint(1, 5)
    default_price = Faker.pyint()


class MemberFavorite(factory.django.DjangoModelFactory):
    class Meta:
        model = member.models.MemberFavorite

    member = factory.SubFactory(MemberBase)
    tour_group = factory.SubFactory(TourGroupBase)


class ScoreBaseLog(factory.django.DjangoModelFactory):
    class Meta:
        model = score.models.ScoreBaseLog

    supplier = factory.SubFactory(SupplierBase)
    member = factory.SubFactory(MemberBase)
    tour_group = factory.SubFactory(TourGroupBase)
    category = Faker.random_element([row.value for row in constants.SupplierScoreCatagory])
    food_score = Faker.pyint(1, 100)
    traffic_score = Faker.pyint(1, 100)
    scheduler_score = Faker.pyint(1, 100)
    tour_guide_score = Faker.pyint(1, 100)
    stay_score = Faker.pyint(1, 100)
    description = Faker.text()


class TourGroupLocation(factory.django.DjangoModelFactory):
    class Meta:
        model = tour.models.TourGroupLocation

    tour_group = factory.SubFactory(TourGroupBase)
    type = Faker.random_element([row.value for row in constants.TourGroupLocationType])
    option = Faker.random_element([row.value for row in constants.TourGroupLocationOpition])


class TourGroupTag(factory.django.DjangoModelFactory):
    class Meta:
        model = tour.models.TourGroupTag

    tour_group = factory.SubFactory(TourGroupBase)
    tag = Faker.random_element([row.value for row in constants.TourGroupTag])


class TourGroupBucket(factory.django.DjangoModelFactory):
    class Meta:
        model = tour.models.TourGroupBucket

    tour_group = factory.SubFactory(TourGroupBase)
    date = Faker.date()
    currency = Faker.random_element([row.value for row in constants.Currency])
    sku = Faker.pyint(500, 1000)
    sell = Faker.pyint(1, 499)
    adult_price = Faker.pyint()
    child_price = Faker.pyint()
    baby_price = Faker.pyint()
    remark = Faker.text()
    transfer = Faker.pyint(0, 10)
    go_from = constants.TourGroupLocationOpition.TAINAN
    back_from = constants.TourGroupLocationOpition.TAINAN
