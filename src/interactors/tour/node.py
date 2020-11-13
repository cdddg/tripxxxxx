from pydantic.dataclasses import dataclass
import pydantic
from datetime import date

from ..base import BaseInput
from pydantic import BaseModel, ValidationError, validator




@dataclass
class GetTourGroupsInput(BaseInput):
    page: int
    size: int
    order_by: str = None
