from enum import Enum

from enum import Enum

# Enum for Customer Status
class CustomerStatus(Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    SUSPENDED = "suspended"

# Enum for Locker Status
class LockerStatus(Enum):
    FREE = "free"
    BOOKED = "booked"
    OUT_OF_SERVICE = "out_of_service"

# Enum for Order Status
class OrderStatus(Enum):
    PENDING = "pending"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELED = "canceled"
    RETURNED = "returned"

# Enum for Package Status
class PackageStatus(Enum):
    AWAITING_PICKUP = "awaiting_pickup"
    DELIVERED = "delivered"
    RETURNED = "returned"
    LOST = "lost"

# Enum for Notification Type
class NotificationType(Enum):
    PACKAGE_READY = "package_ready"
    PACKAGE_PICKED_UP = "package_picked_up"
    PACKAGE_RETURNED = "package_returned"
    ORDER_PLACED = "order_placed"
    ORDER_CANCELED = "order_canceled"

# Enum for Notification Target Type
class NotificationTargetType(Enum):
    CUSTOMER = "customer"
    LOCKER = "locker"
    ORDER = "order"
    PACKAGE = "package"

# Enum for Time Slots (Optional: for hub operating hours)
class TimeSlot(Enum):
    MORNING = "morning"
    AFTERNOON = "afternoon"
    EVENING = "evening"
    NIGHT = "night"
