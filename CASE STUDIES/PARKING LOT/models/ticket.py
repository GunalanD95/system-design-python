from .parking_spot import ParkingSpot
from .parking_gate import ParkingGate
from .operator import Operator
from .vehicle  import Vehicle
from datetime import datetime
from .base import BaseModel

class Ticket(BaseModel):
    def __init__(self) -> None:
        self._ticket_num: int = None
        self._enter_time : datetime  = None
        self._parking_spot: ParkingSpot = None
        self._parking_gate: ParkingGate = None
        self._operator: Operator = None
        self._vehicle : Vehicle = None

    @property
    def ticket_num(self) -> int:
        return self._ticket_num

    @ticket_num.setter
    def ticket_num(self, value: int) -> None:
        self._ticket_num = value

    @property
    def enter_time(self) -> int:
        return self._enter_time

    @ticket_num.setter
    def enter_time(self, value: int) -> None:
        self._enter_time = value

    @property
    def parking_spot(self) -> ParkingSpot:
        return self._parking_spot

    @parking_spot.setter
    def parking_spot(self, value: ParkingSpot) -> None:
        self._parking_spot = value

    @property
    def parking_gate(self) -> ParkingGate:
        return self._parking_gate

    @parking_gate.setter
    def parking_gate(self, value: ParkingGate) -> None:
        self._parking_gate = value

    @property
    def operator(self) -> Operator:
        return self._operator

    @operator.setter
    def operator(self, value: Operator) -> None:
        self._operator = value
        

    @property
    def vehicle(self) -> Vehicle:
        return self._vehicle

    @vehicle.setter
    def vehicle(self, value: Vehicle) -> None:
        self._vehicle = value

