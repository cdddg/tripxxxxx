import enum



class PlatformType(enum.IntEnum):
    TRIPRESSO = 0
    GOOGLE = 1
    FACEBOOK = 2
    LINE = 3


@enum.unique
class IsRecommendStatus(enum.IntEnum):
    OFF = 0
    ON = 1


class SupplierScoreCatagory(enum.IntEnum):
    PEER = 0
    SINGLE = 1
    COUPLE = 2
    FAMILY = 3
    HONEYMOON = 4
    EMPLOYEE = 5
    OTHER = 6


class TourGroupLocationType(enum.IntEnum):
    AREA = 0
    COUNTRY = 1
    CITY = 2


class TourGroupLocationOpition(enum.IntEnum):
    TAIWAN = 1001
    JAPAN = 1002

    TAIPEI = 2001
    TAINAN = 2002
