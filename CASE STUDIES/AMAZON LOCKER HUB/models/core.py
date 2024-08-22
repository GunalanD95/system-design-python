from typing import List
from .enums import CustomerStatus , LockerStatus , OrderStatus , PackageStatus , NotificationType , NotificationTargetType , TimeSlot

class Customer():
    def __init__(self) -> None:
        self.customer_id = None
        self.customer_name = None
        self.customer_location = None
        self.customer_status : CustomerStatus = None
        self.email_address = None
        self.phone_number = None

class AmazonLockerHub(): 
    def __init__(self) -> None:
        self.hub_id = None
        self.location = None
        self.amazon_lockers : List[AmazonLocker] = []
        self.start_time = None
        self.end_time = None

class AmazonLocker():
    def __init__(self) -> None:
        self.locker_id = None
        self.location_id : AmazonLockerHub = None
        self.locker_code = None
        self.package_id = None
        self.locker_status : LockerStatus = None
        
class OrderItem():
    def __init__(self) -> None:
        self.item_id = None
        self.quantity = None
        self.price = None
        self.order_id = None

class Order():
    def __init__(self) -> None:
        self.id = None
        self.customer_id = None
        self.order_status : OrderStatus = None
        self.order_items : List[OrderItem] = [] 


class Package():
    def __init__(self) -> None:
        self.package_id = None
        self.package_status : PackageStatus = None
        self.package_items : List[Order] = []
        self.locker_id = None


class Notification:
    def __init__(self):
        self.notification_id = None
        self.notification_type : NotificationType  = None
        self.notification_text = None
        self.target_id = None
        self.target_type : NotificationTargetType  = None


