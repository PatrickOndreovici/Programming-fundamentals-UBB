from datetime import datetime

import repository
import validation


class Service:
    def __init__(self):
        self._undo = []
        self._repository = repository.Repository()

    def service_create_package(self, start_date, end_date, destination, price):
        validation.validate_package_params(0, start_date, end_date, destination, price)
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        price = float(price)
        package = self._repository.create_package(start_date, end_date, destination, price)
        self._undo.append({"type": "delete", "package": package})
        return package

    def service_update_package(self, package_id, start_date, end_date, destination, price):
        validation.validate_package_params(package_id, start_date, end_date, destination, price)
        package_id = int(package_id)
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        price = float(price)
        package = self._repository.get_package_by_id(package_id)
        if package is None:
            raise Exception("Pachetul nu exista")
        self._undo.append({"type": "update", "package": package})
        return self._repository.update_package(package_id, start_date, end_date, destination, price)

    def service_remove_packages_by_destination(self, destination):
        validation.validate_destination(destination)
        removed_packages = self._repository.remove_packages_by_destination(destination)
        self._undo.append({"type": "add", "packages": removed_packages})
        return removed_packages

    def service_remove_packages_by_days(self, no_days):
        validation.validate_no_days(no_days)
        no_days = int(no_days)
        removed_packages = self._repository.remove_packagse_by_days(no_days)
        self._undo.append({"type": "add", "packages": removed_packages})
        return removed_packages

    def service_remove_packages_by_price(self, price):
        validation.validate_price(price)
        price = float(price)
        removed_packages = self._repository.remove_packages_by_price(price)
        self._undo.append({"type": "add", "packages": removed_packages})
        return removed_packages

    def service_get_packages_by_date_interval(self, start_date, end_date):
        validation.validate_date(start_date, end_date)
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        return self._repository.get_packages_by_date_interval(start_date, end_date)

    def service_get_packages_by_destination_and_price(self, destination, price):
        validation.validate_destination(destination)
        validation.validate_price(price)
        price = float(price)
        return self._repository.get_packages_by_destination_and_price(destination, price)

    def service_get_packages_by_end_date(self, end_date):
        validation.validate_date(None, end_date)
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        return self._repository.get_packages_by_end_date(end_date)

    def service_get_no_packages_by_destination(self, destination):
        validation.validate_destination(destination)
        return self._repository.get_no_packages_by_destination(destination)

    def service_get_average_price_by_destination(self, destination):
        validation.validate_destination(destination)
        return self._repository.get_average_price_by_destination(destination)

    def service_remove_packages_by_price_and_another_destination(self, price, destination):
        validation.validate_price(price)
        validation.validate_destination(destination)
        price = float(price)
        removed_packages = self._repository.remove_packages_by_price_and_another_destination(price, destination)
        self._undo.append({"type": "add", "packages": removed_packages})
        return removed_packages

    def service_remove_packages_by_month(self, month):
        validation.validate_month(month)
        month = int(month)
        removed_packages = self._repository.remove_packages_by_month(month)
        self._undo.append({"type": "add", "packages": removed_packages})
        return removed_packages

    def undo_operation(self):
        if len(self._undo) == 0:
            raise Exception("Nu exista operatii de undo")
        last_operation = self._undo.pop()
        if last_operation["type"] == "add":
            self._repository.re_add_packages(last_operation["packages"])
        elif last_operation["type"] == "delete":
            package = last_operation["package"]
            self._repository.remove_by_id(package.get_package_id())
        elif last_operation["type"] == "update":
            package = last_operation["package"]
            self._repository.update_package(package.get_package_id(), package.get_start_date(),
                                            package.get_end_date(),
                                            package.get_destination(), package.get_price())
        return self._repository.get_packages()
