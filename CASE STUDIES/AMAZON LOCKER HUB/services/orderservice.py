
class OrderService():

    def __init__(self):
        self._orders = []
        
    def create_order(self, order):
        order.order_id = len(self._orders)
        self._orders.append(order)
        return order
    
    def get_order_by_id(self, order_id):
        for order in self._orders:
            if order.order_id == order_id:
                return order
        return None
    
    def update_order(self, order):
        for idx, existing_order in enumerate(self._orders):
            if existing_order.order_id == order.order_id:
                self._orders[idx] = order
                return order
        return None