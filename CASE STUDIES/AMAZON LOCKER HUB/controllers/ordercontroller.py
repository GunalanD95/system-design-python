from models.core import Order , Notification
from services.orderservice import OrderService
from services.notificationservice import NotificationService

class OrderController():
    def __init__(self):
        self.service = OrderService()
        self.notification_service = NotificationService()
        
    def create_order(self, customer_id, order_items) -> Order:
        print(f"Creating order for customer {customer_id} with items {order_items}")
        if customer_id is  None or not order_items:
            raise ValueError("Customer ID and order items are required")
        order = Order()
        order.customer_id = customer_id
        order.order_items = order_items
        notification = self.notification_service.create_notification(Notification())
        self.notification_service.send_notification(notification)
        return self.service.create_order(order)
    
    def update_order(self, order_id, order_items):
        order = self.service.get_order_by_id(order_id)
        if not order:
            raise ValueError("Order not found")
        order.order_items = order_items
        return self.service.update_order(order)
    
    def get_order_by_id(self, order_id):
        return self.service.get_order_by_id(order_id)