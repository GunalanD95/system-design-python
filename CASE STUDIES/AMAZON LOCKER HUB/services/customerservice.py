from models.core import Customer
from models.enums import CustomerStatus

class CustomerService():
    
    def __init__(self):
        self._customers = []
        
        
    def create_customer(self,customer: Customer) -> Customer:
        customer.customer_id = len(self._customers)
        customer.customer_status = CustomerStatus.ACTIVE
        self._customers.append(customer)
        return customer
    
    def get_customer_by_id(self,customer_id) -> Customer:
        for customer in self._customers:
            if customer.customer_id == customer_id:
                return customer
        return None
    
    def update_customer(self, customer):
        # Dummy implementation for updating the customer
        for idx, existing_customer in enumerate(self._customers):
            if existing_customer.customer_id == customer.customer_id:
                self._customers[idx] = customer
                return customer
        return None