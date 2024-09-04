from dataclasses import dataclass
from typing import List
from models.core import *
from models.state import *

@dataclass
class VendingMachineService:
    def create_vending_machine(self, num_racks: int) -> VendingMachine:
        racks = [Rack(rack_number=i + 1, product=None) for i in range(num_racks)]
        available_racks = [rack.rack_number for rack in racks]
        vending_machine = VendingMachine(
            current_state=NoMoneyInsertedState(),
            amount=0.0,
            no_of_racks=num_racks,
            racks=racks,
            available_racks=available_racks,
        )
        return vending_machine

    def load_inventory(self, vending_machine: VendingMachine, products: List[Product]) -> None:
        for i, product in enumerate(products):
            if i < vending_machine.no_of_racks:
                vending_machine.racks[i].product = product
                print(f"Loaded {product.name} into rack {i + 1}")
            else:
                print("Not enough racks for all products!")
                break
