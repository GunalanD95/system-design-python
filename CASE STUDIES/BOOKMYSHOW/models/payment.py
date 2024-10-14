from models.basemodel import BaseModel
from enum import Enum 

class PaymentType(str, Enum):
    CREDITCARD = "CREDITCARD"
    DEBITCARD = "DEBITCARD"
    NETBANKING = "NETBANKING"
    UPI = "UPI"
    CASH = "CASH"
    
class PaymentStatus(Enum):
    COMPLETED = 1
    PENDING = 2
    FAILED = 3

class Payment(BaseModel):
    def __init__(self) -> None:
        self._ref_id: int = None
        self._user_id: int = None   
        self._amount : int = None
        self._type : PaymentType = None
        self._status : PaymentStatus = None
        
    @property
    def ref_id(self):
        return self._ref_id
    
    @property
    def user_id(self):
        return self._user_id
    
    @property
    def amount(self):
        return self._amount
    
    @property
    def type(self):
        return self._type
    
    @ref_id.setter
    def ref_id(self, value: int):
        self._ref_id = value
        
    @user_id.setter
    def user_id(self, value: int):
        self._user_id = value
        
    @amount.setter
    def amount(self, value: int):
        self._amount = value
        
    @type.setter
    def type(self, value: PaymentType):
        self._type = value
        
    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self, value: PaymentStatus):
        self._status = value
        
    def __str__(self) -> str:
        return f"< Payment : {self.ref_id} | {self.user_id} | {self.amount} | {self.type} >" 
