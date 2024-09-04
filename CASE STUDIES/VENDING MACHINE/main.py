from .controllers import VendingMachineController
from .models import Product, ProductType
from .services import VendingMachineService

vending_service = VendingMachineService()
vending_machine = vending_service.create_vending_machine(5)

controller = VendingMachineController(vending_machine)

# Load products
products = [
    Product(id=1, name="Coke", price=1.5, type=ProductType.DRINK),
    Product(id=2, name="Pepsi", price=1.5, type=ProductType.DRINK),
    Product(id=3, name="Snickers", price=2.0, type=ProductType.FOOD),
]
vending_service.load_inventory(vending_machine, products)

# Operate the vending machine
controller.insert_money(2.0)
controller.press_button(1)
controller.return_change()
