# main.py

from controllers.ordercontroller import OrderController
from controllers.packagecontroller import PackageController
from controllers.lockercontroller import LockerController
from controllers.customercontroller import CustomerController
from models.core import Customer, AmazonLockerHub, AmazonLocker
from models.enums import CustomerStatus, TimeSlot, LockerStatus


def main():
    # Initialize controllers
    order_controller = OrderController()
    package_controller = PackageController()
    locker_controller = LockerController()
    customer_controller = CustomerController()
    
    
    # create a customer
    customer = customer_controller.creater_customer(
        name="Gojo Satoru",
        location="123 Main St",
        email="gojo@bu.edu",
        phone_number="555-555-5555"
    )
    
    # create an order
    order = order_controller.create_order(
        customer_id=customer.customer_id,
        order_items=[
            {
                "item_id": 1,
                "quantity": 1,
                "price": 10
            },
            {
                "item_id": 2,
                "quantity": 2,
                "price": 20
            },
        ]
    )
    
    # create a package
    package = package_controller.create_package(
        locker_id=1,
        order_items=order.order_items
    )
    
    # create a locker
    locker = locker_controller.assign_locker(
        locker_id = package.locker_id,
        package_id = package.package_id,
        location = 1
    )
    
    print(f"Assigned locker {locker.locker_id} to package {package.package_id} for customer {customer.customer_id}")
    return locker
    
    
if __name__ == "__main__":
    main()