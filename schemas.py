from pydantic import BaseModel
from typing import Optional

class ExcavationPointCreate(BaseModel):
    point_type: str
    latitude: float
    longitude: float
    altitude: Optional[float]
    srid: Optional[str]
    description: Optional[str]
    registered_by: Optional[str]
