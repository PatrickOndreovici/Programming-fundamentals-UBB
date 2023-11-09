from package import Package


class Repository:

    def __init__(self):
        self._id_counter = 0
        self._packages = []

    def get_packages(self):
        return self._packages

    def create_package(self, start_date, end_date, destination, price):
        package = Package(self._id_counter, start_date, end_date, destination, price)
        self._id_counter = self._id_counter + 1
        self._packages.append(package)
        return package

    def re_add_packages(self, packages_to_re_add):
        for package in packages_to_re_add:
            self._packages.append(package)

    def remove_by_id(self, package_id):
        new_packages = []
        for package in self._packages:
            if package.get_package_id() != package_id:
                new_packages.append(package)
        self._packages[:] = new_packages

    def update_package(self, package_id, start_date, end_date, destination, price):
        package = self.get_package_by_id(package_id)
        package.set_start_date(start_date)
        package.set_end_date(end_date)
        package.set_destination(destination)
        package.set_price(price)
        return package

    def get_package_by_id(self, package_id):
        for package in self._packages:
            if package.get_package_id() == package_id:
                return package
        return None

    def remove_packages_by_destination(self, destination):
        new_packages = []
        removed_packages = []
        for package in self._packages:
            if package.get_destination() != destination:
                new_packages.append(package)
            else:
                removed_packages.append(package)
        self._packages[:] = new_packages
        return removed_packages

    def remove_packagse_by_days(self, no_days):
        new_packages = []
        removed_packages = []
        for package in self._packages:
            delta = package.get_end_date() - package.get_start_date()
            if delta.days >= no_days:
                new_packages.append(package)
            else:
                removed_packages.append(package)
        self._packages[:] = new_packages
        return removed_packages

    def remove_packages_by_price(self, price):
        new_packages = []
        removed_packages = []
        for package in self._packages:
            if package.get_price() <= price:
                new_packages.append(package)
            else:
                removed_packages.append(removed_packages)
        self._packages[:] = new_packages
        return removed_packages

    def get_packages_by_date_interval(self, start_date, end_date):
        packages_to_return = []
        for package in self._packages:
            if package.get_start_date() >= start_date and package.get_end_date() <= end_date:
                packages_to_return.append(package)
        return packages_to_return

    def get_packages_by_destination_and_price(self, destination, price):
        packages_to_return = []
        for package in self._packages:
            if package.get_destination() == destination and package.get_price() < price:
                packages_to_return.append(package)
        return packages_to_return

    def get_packages_by_end_date(self, end_date):
        packages_to_return = []
        for package in self._packages:
            if package.get_end_date() == end_date:
                packages_to_return.append(package)
        return packages_to_return

    def get_no_packages_by_destination(self, destination):
        no_packages = 0
        for package in self._packages:
            if package.get_destination() == destination:
                no_packages += 1
        return no_packages

    def get_average_price_by_destination(self, destination):
        no_packages = 0
        sum_price = 0
        for package in self._packages:
            if package.get_destination() == destination:
                no_packages += 1
                sum_price += package.get_price()
        if no_packages == 0:
            return 0
        return sum_price / no_packages

    def remove_packages_by_price_and_another_destination(self, price, destination):
        new_packages = []
        removed_packages = []
        for package in self._packages:
            if package.get_destination() == destination and package.get_price() <= price:
                new_packages.append(package)
            else:
                removed_packages.append(package)
        self._packages[:] = new_packages
        return removed_packages

    def remove_packages_by_month(self, month):
        new_packages = []
        removed_packages = []
        for package in self._packages:
            if package.get_start_date().year == package.get_end_date.year:
                if month < package.get_start_date().month or month > package.get_end_date().month:
                    new_packages.append(package)
                else:
                    removed_packages.append(package)
            elif package.get_end_date().year - package.get_start_date().year == 1:
                if month < min(package.get_start_date().month, package.get_end_date().month) or month > max(
                        package.get_start_date().month, package.get_end_date().month):
                    new_packages.append(package)
                else:
                    removed_packages.append(package)
            else:
                removed_packages.append(package)
        self._packages[:] = new_packages
        return removed_packages
