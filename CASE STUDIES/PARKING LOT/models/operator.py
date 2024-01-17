from .base import BaseModel

class Operator(BaseModel):
    def __init__(self) -> None:
        self._name: str = None
        self._emp_id: int = None

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    @property
    def emp_id(self) -> int:
        return self._emp_id

    @emp_id.setter
    def emp_id(self, value: int) -> None:
        self._emp_id = value
