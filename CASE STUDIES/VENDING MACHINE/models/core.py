from enum import Enum
from dataclasses import dataclass
from typing import  List , Optional
from .state import State

class ProductType(Enum):
    DRINK = 1
    FOOD = 2
    

@dataclass
class Product:
    id : int
    name : str
    price : int
    prod_type : ProductType

@dataclass
class Rack:
    rack_number : int
    product : Product 
    
@dataclass
class Inventory:
    products: List[Product]  # The inventory holds a list of products

    def add_product(self, product: Product) -> None:
        self.products.append(product)

    def remove_product(self, product_id: int) -> None:
        self.products = [product for product in self.products if product.id != product_id]


@dataclass
class VendingMachine:
    current_state: State  # You may want to use an Enum for states in the future
    amount: float
    no_of_racks: int
    racks: List[Rack]  # List of racks in the vending machine
    available_racks: List[int]  # List of available rack numbers

    def get_product_id_at_rack(self, rack_number: int) -> Optional[int]:
        for rack in self.racks:
            if rack.rack_number == rack_number and rack.product:
                return rack.product.id
        return None
    

