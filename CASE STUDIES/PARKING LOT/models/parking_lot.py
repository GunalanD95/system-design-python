from typing import List
from .parking_floor import ParkingFloor
from .parking_gate import ParkingGate
from .base import BaseModel

class ParkingLot(BaseModel):

    def __init__(self) -> None:
        self._parking_floors: List[ParkingFloor] = []
        self._parking_gates:  List[ParkingGate] = []
        self._capacity: int = 0

    @property
    def parking_floors(self) -> List[ParkingFloor]:
        return self._parking_floors

    @parking_floors.setter
    def parking_floors(self, parking_floors: List[ParkingFloor]) -> None:
        self._parking_floors = parking_floors

    @property
    def parking_gates(self) -> List[ParkingGate]:
        return self._parking_gates

    @parking_gates.setter
    def parking_gates(self, parking_gates: List[ParkingGate]) -> None:
        self._parking_gates = parking_gates

    @property
    def capacity(self) -> int:
        return self._capacity

    @capacity.setter
    def capacity(self, capacity: int) -> None:
        self._capacity = capacity
