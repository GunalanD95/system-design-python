from models.core import Package
from models.enums import PackageStatus
from services.packageservice import PackageService

class PackageController():
    def __init__(self) -> None:
        self.service = PackageService()
    
    def create_package(self, locker_id, order_items) -> Package:
        if not locker_id or not order_items:
            print("here",locker_id, order_items)
            raise ValueError("Locker ID and package items are required")
        package = Package()
        
        package.locker_id = locker_id
        package.package_items = order_items
        return self.service.create_package(package)
    
    def update_package(self, package_id, package_items):
        package = self.service.get_package_by_id(package_id)
        if not package:
            raise ValueError("Package not found")
        package.package_items = package_items
        return self.service.update_package(package)
    
    def get_package_by_id(self, package_id):
        return self.service.get_package_by_id(package_id)