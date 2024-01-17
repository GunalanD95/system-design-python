from typing import List
from .ticket import Ticket
from .operator import Operator
from .payment import Payment
from datetime import datetime

class Bill:
    def __init__(self) -> None:
        self._exist_time: datetime  = None
        self._ticket: Ticket = None
        self._operator: Operator = None
        self._amount: int  = None
        self._payment: List[Payment] = []

    @property
    def exist_time(self) -> int:
        return self._exist_time

    @exist_time.setter
    def exist_time(self, value: int) -> None:
        self._exist_time = value

    @property
    def ticket(self) -> Ticket:
        return self._ticket

    @ticket.setter
    def ticket(self, value: Ticket) -> None:
        self._ticket = value

    @property
    def operator(self) -> Operator:
        return self._operator

    @operator.setter
    def operator(self, value: Operator) -> None:
        self._operator = value

    @property
    def amount(self) -> int:
        return self._amount

    @amount.setter
    def amount(self, value: int) -> None:
        self._amount = value

    @property
    def payment(self) -> List[Payment]:
        return self._payment

    @payment.setter
    def payment(self, value: List[Payment]) -> None:
        self._payment = value
