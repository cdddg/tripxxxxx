import enum


class GenderType(enum.IntEnum):
    UNKNOWN = 0
    MALE = 1
    FEMALE = 2


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


class TourGroupTag(enum.Enum):
    LATE_BACK = 'LATE_BACK'
    EARLY_GO = 'EARLY_GO'
    DIRECT_FLIGHT = 'DIRECT_FLIGHT'
    HOT_TOP = 'HOT_TOP'
    NO_SHOP = 'NO_SHOP'
    DOMESTIC_TRAVEL = 'DOMESTIC_TRAVEL'
    TRIPLE_STIMULUS_VOUCHER = 'TRIPLE_STIMULUS_VOUCHER'


class Currency(enum.IntEnum):
    TWD = 0


class TourGroupInputOrderBy(enum.Enum):
    PRICE_ASC = 'PRICE_ASC'
    PRICE_DESC = 'PRICE_DESC'
    SCORE_ASC = 'SCORE_ASC'
    SCORE_DESC = 'SCORE_DESC'

    def parse(self):
        orderby, sorting = self._name_.split('_')
        return orderby.lower(), sorting
