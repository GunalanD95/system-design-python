from abc import ABC , abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .core import VendingMachine
    
    
class State(ABC):
    @abstractmethod
    def insert_money(self, vending_machine: 'VendingMachine', amount: float) -> None:
        pass

    @abstractmethod
    def press_button(self, vending_machine: 'VendingMachine', rack_number: int) -> None:
        pass

    @abstractmethod
    def return_change(self, vending_machine: 'VendingMachine') -> float:
        pass

    @abstractmethod
    def dispense_product(self, vending_machine: 'VendingMachine', rack_number: int) -> None:
        pass

    @abstractmethod
    def update_inventory(self, vending_machine: 'VendingMachine', rack_number: int) -> None:
        pass
    
class NoMoneyInsertedState(State):
    def insert_money(self, vending_machine: 'VendingMachine', amount: float) -> None:
        vending_machine.amount += amount
        vending_machine.cur_state = 'MoneyInsertedState'
        print(f"Inserted {amount}, total amount is now {vending_machine.amount}")

    def press_button(self, vending_machine: 'VendingMachine', rack_number: int) -> None:
        print("Insert money first!")
    
    def return_change(self, vending_machine: 'VendingMachine') -> float:
        print("No money to return!")
        return 0.0
    
    def dispense_product(self, vending_machine: 'VendingMachine', rack_number: int) -> None:
        print("Cannot dispense, no money inserted!")
    
    def update_inventory(self, vending_machine: 'VendingMachine', rack_number: int) -> None:
        print("Inventory update not allowed in this state!")
        
class MoneyInsertedState(State):
    def insert_money(self, vending_machine: 'VendingMachine', amount: float) -> None:
        vending_machine.amount += amount
        print(f"Inserted additional {amount}, total amount is now {vending_machine.amount}")
        
    def press_button(self, vending_machine: 'VendingMachine', rack_number: int) -> None:
        product_id = vending_machine.get_product_id_at_rack(rack_number)
        if product_id and vending_machine.amount >= vending_machine.racks[rack_number - 1].product.price:
            self.dispense_product(vending_machine, rack_number)
        else:
            print("Insufficient funds or empty rack!")  
              
    def return_change(self, vending_machine: 'VendingMachine') -> float:
        change = vending_machine.amount
        vending_machine.amount = 0.0
        vending_machine.current_state = "NoMoneyInsertedState"
        print(f"Returning change: {change}")
        return change
    
    def dispense_product(self, vending_machine: 'VendingMachine', rack_number: int) -> None:
        product = vending_machine.racks[rack_number - 1].product
        vending_machine.amount -= product.price
        print(f"Dispensing product {product.name} from rack {rack_number}")
        vending_machine.current_state = "DispenseState"
        self.update_inventory(vending_machine, rack_number)
        
    def update_inventory(self, vending_machine: 'VendingMachine', rack_number: int) -> None:
        vending_machine.racks[rack_number - 1].product = None
        print(f"Updated inventory for rack {rack_number}")   
        
class DispenseState(State):
    def insert_money(self, vending_machine: 'VendingMachine', amount: float) -> None:
        print("Please take the dispensed product first!")

    def press_button(self, vending_machine: 'VendingMachine', rack_number: int) -> None:
        print("Please take the dispensed product first!")

    def return_change(self, vending_machine: 'VendingMachine') -> float:
        print("Please take the dispensed product first!")
        return 0.0

    def dispense_product(self, vending_machine: 'VendingMachine', rack_number: int) -> None:
        print("Product already dispensed!")

    def update_inventory(self, vending_machine: 'VendingMachine', rack_number: int) -> None:
        vending_machine.current_state = "NoMoneyInsertedState"
        print("Inventory updated, returning to no money inserted state.") 