from pydantic.dataclasses import dataclass
from datetime import date

from .. import base


@dataclass
class GetMembersInput(base.BaseInput):
    platform: int = None
    surname: str = None
    given_name: str = None
    gender: str = None
    birthday: date = None
    email: str = None
    phone: str = None
    address: str = None
    tripresso_coin: int = None
