from models.core import Order
from services.orderservice import OrderService

class OrderController():
    def __init__(self):
        self.service = OrderService()
        
    def create_order(self, customer_id, order_items) -> Order:
        if not customer_id or not order_items:
            raise ValueError("Customer ID and order items are required")
        order = Order()
        order.customer_id = customer_id
        order.order_items = order_items
        return self.service.create_order(order)