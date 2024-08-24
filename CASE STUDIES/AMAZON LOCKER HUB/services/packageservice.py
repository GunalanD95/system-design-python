from models.core import Package
from models.enums import PackageStatus



class PackageService():

    def __init__(self): 
        self._packages = []
        
    def create_package(self, package):
        package.package_id = len(self._packages)
        self._packages.append(package)
        return package
    
    def get_package_by_id(self, package_id):
        for package in self._packages:
            if package.package_id == package_id:
                return package
        return None
    
    def update_package(self, package):
        for idx, existing_package in enumerate(self._packages):
            if existing_package.package_id == package.package_id:
                self._packages[idx] = package
                return package
        return None


