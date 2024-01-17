from typing import List
from .operator import Operator
from enum import Enum 
from .base import BaseModel

class GateStatus(Enum):
    OPEN    = 'open'
    CLOSED  = 'closed'
    
class GateType(Enum):
    pass

class ParkingGate(BaseModel):
    def __init__(self) -> None:
        self._gate_num: int = None
        self._operator: Operator = None 
        self._status:  GateStatus = None 
        self._gate_type : GateType = None

    @property
    def gate_num(self) -> int:
        return self._gate_num

    @gate_num.setter
    def gate_num(self, value: int) -> None:
        self._gate_num = value

    @property
    def operator(self) -> Operator:
        return self._operator

    @operator.setter
    def operator(self, value: Operator) -> None:
        self._operator = value

    @property
    def status(self) -> GateStatus:
        return self._status

    @status.setter
    def status(self, value: GateStatus) -> None:
        self._status = value

    @property
    def gate_type(self) -> int:
        return self._gate_type

    @gate_type.setter
    def gate_type(self, value: int) -> None:
        self._gate_type = value