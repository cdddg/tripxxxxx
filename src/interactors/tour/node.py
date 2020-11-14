from pydantic.dataclasses import dataclass

from ..base import BaseInput


@dataclass
class GetTourGroupsInput(BaseInput):
    page: int
    size: int
    order_by: str = None
    member_id: str = None
