from pydantic import BaseModel
from typing import Dict

class ColoredAreas(BaseModel):
    colored_areas: Dict[str, int]
    min_colors: int


class Carpet(BaseModel):
    name: str
    price: int


class Route(BaseModel):
    start_point: str
    destination: str
    route: str
    distance: int
