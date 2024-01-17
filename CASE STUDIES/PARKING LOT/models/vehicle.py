from enum import Enum
from .base import BaseModel

class VehicleType(Enum):
    CAR  = 'car'
    BIKE = 'bike'
    SUV  = 'suv'
    OTHERS = 'others'
    
class Vehicle(BaseModel):
    def __init__(self) -> None:
        self._vehicle_num: str = None
        self._vehicle_type: VehicleType = None

    @property
    def vehicle_num(self) -> int:
        return self._vehicle_num

    @vehicle_num.setter
    def vehicle_num(self, value: int) -> None:
        self._vehicle_num = value

    @property
    def vehicle_type(self) -> VehicleType:
        return self._vehicle_type

    @vehicle_type.setter
    def vehicle_type(self, value: VehicleType) -> None:
        self._vehicle_type = value
