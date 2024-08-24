# strategies/package_handling_strategy.py

from models import Package

class PackageHandlingStrategy:
    def handle_package(self, package: Package):
        raise NotImplementedError("This method should be overridden by subclasses")

class MorningSlotHandlingStrategy(PackageHandlingStrategy):
    def handle_package(self, package: Package):
        print(f"Handling package in the morning slot: {package.package_id}")

class AfternoonSlotHandlingStrategy(PackageHandlingStrategy):
    def handle_package(self, package: Package):
        print(f"Handling package in the afternoon slot: {package.package_id}")

class NightSlotHandlingStrategy(PackageHandlingStrategy):
    def handle_package(self, package: Package):
        print(f"Handling package in the night slot: {package.package_id}")
