from typing import List
from .parking_spot import ParkingSpot
from .base import BaseModel

class ParkingFloor(BaseModel):
    def __init__(self) -> None:
        self._floor_number: int = 0
        self._parking_gates: List[ParkingSpot] = []

    @property
    def floor_number(self) -> int:
        return self._floor_number

    @floor_number.setter
    def floor_number(self, value: int) -> None:
        self._floor_number = value

    @property
    def parking_gates(self) -> List[ParkingSpot]:
        return self._parking_gates

    @parking_gates.setter
    def parking_gates(self, value: List[ParkingSpot]) -> None:
        self._parking_gates = value
