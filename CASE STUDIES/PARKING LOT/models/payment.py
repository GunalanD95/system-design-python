from enum import Enum

class PaymentMode(Enum):
    CASH = 'cash'
    CARD = 'card'
    ONLINE = 'online'

class PaymentStatus(Enum):
    PENDING = 'pending'
    SUCCESSFUL = 'successful'
    FAILED = 'failed'

class Payment:
    def __init__(self) -> None:
        self._ref_id: int = None
        self._mode_of_payment: PaymentMode = None
        self._amount: int = None
        self._status: PaymentStatus = None

    @property
    def ref_id(self) -> int:
        return self._ref_id

    @ref_id.setter
    def ref_id(self, value: int) -> None:
        self._ref_id = value

    @property
    def mode_of_payment(self) -> PaymentMode:
        return self._mode_of_payment

    @mode_of_payment.setter
    def mode_of_payment(self, value: PaymentMode) -> None:
        self._mode_of_payment = value

    @property
    def amount(self) -> int:
        return self._amount

    @amount.setter
    def amount(self, value: int) -> None:
        self._amount = value

    @property
    def status(self) -> PaymentStatus:
        return self._status

    @status.setter
    def status(self, value: PaymentStatus) -> None:
        self._status = value
