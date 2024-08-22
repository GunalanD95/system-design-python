from models.core import Customer
from models.enums import CustomerStatus
from services.customerservice import CustomerService

class CustomerController():
    def __init__(self) -> None:
        self.service = CustomerService()
    
    def creater_customer(self,name, location, email, phone_number) -> Customer:
        if not name or not email:
            raise ValueError("Name and email are required")
        
        customer = Customer()
        customer.customer_name = name
        customer.customer_location = location
        customer.email_address = email
        customer.phone_number = phone_number
        
        return self.service.create_customer(customer)  
    
    def update_customer(self, customer_id, name=None, location=None, email=None, phone_number=None):
        # Fetch the customer
        customer = self.customer_service.get_customer_by_id(customer_id)
        if not customer:
            raise ValueError("Customer not found")
        # Update fields
        if name:
            customer.name = name
        if location:
            customer.location = location
        if email:
            customer.email = email
        if phone_number:
            customer.phone_number = phone_number
        # Call the service layer to update the customer
        return self.customer_service.update_customer(customer)
    
    def get_customer(self, customer_id):
        # Retrieve a customer by ID
        return self.customer_service.get_customer_by_id(customer_id)