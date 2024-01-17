from typing import List
from .vehicle import VehicleType, Vehicle
from enum import Enum
from .base import BaseModel

class ParkingSpotStatus(Enum):
    OPEN    = 'open'
    CLOSED  = 'closed'

class ParkingSpot(BaseModel):
    def __init__(self) -> None:
        self._spot_num: int = None
        self._vehicle_types: List[VehicleType] = []
        self._spot_status: ParkingSpotStatus = None
        self._vehicle: Vehicle = None

    @property
    def spot_num(self) -> int:
        return self._spot_num

    @spot_num.setter
    def spot_num(self, value: int) -> None:
        self._spot_num = value

    @property
    def vehicle_types(self) -> List[VehicleType]:
        return self._vehicle_types

    @vehicle_types.setter
    def vehicle_types(self, value: List[VehicleType]) -> None:
        self._vehicle_types = value

    @property
    def spot_status(self) -> ParkingSpotStatus:
        return self._spot_status

    @spot_status.setter
    def spot_status(self, value: ParkingSpotStatus) -> None:
        self._spot_status = value

    @property
    def vehicle(self) -> Vehicle:
        return self._vehicle

    @vehicle.setter
    def vehicle(self, value: Vehicle) -> None:
        self._vehicle = value
