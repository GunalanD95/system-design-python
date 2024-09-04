from dataclasses import dataclass
from typing import List
from models.core import VendingMachine
from models.state import NoMoneyInsertedState, MoneyInsertedState


@dataclass
class VendingMachineController:
    vending_machine: VendingMachine

    def insert_money(self,amount : float):
        self.vending_machine.current_state.insert_money(amount)

    def press_button(self,rack_number : int):
        self.vending_machine.current_state.press_button(rack_number)

    def return_change(self) -> float:
        return self.vending_machine.current_state.return_change(self.vending_machine)
    
    def dispense_product(self, rack_number: int) -> None:
        self.vending_machine.current_state.dispense_product(self.vending_machine, rack_number)

    def update_inventory(self, rack_number: int) -> None:
        self.vending_machine.current_state.update_inventory(self.vending_machine, rack_number)