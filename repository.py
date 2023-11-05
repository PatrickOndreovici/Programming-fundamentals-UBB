from package import Package


def create_package(packages, start_date, end_date, destination, price):
    package = Package(start_date, end_date, destination, price)
    packages.append(package)
    return package


def update_package(packages, index, start_date, end_date, destination, price):
    package = packages[index]
    package.set_start_date(start_date)
    package.set_end_date(end_date)
    package.set_destination(destination)
    package.set_price(price)
    return package


def remove_packages_by_destination(packages, destination):
    new_packages = []
    removed_packages = []
    for package in packages:
        if package.get_destination() != destination:
            new_packages.append(package)
        else:
            removed_packages.append(package)
    packages[:] = new_packages
    return removed_packages


def remove_packagse_by_days(packages, no_days):
    new_packages = []
    removed_packages = []
    for package in packages:
        delta = package.get_end_date() - package.get_start_date()
        if delta.days >= no_days:
            new_packages.append(package)
        else:
            removed_packages.append(package)
    packages[:] = new_packages
    return removed_packages


def remove_packages_by_price(packages, price):
    new_packages = []
    removed_packages = []
    for package in packages:
        if package.get_price() <= price:
            new_packages.append(package)
        else:
            removed_packages.append(removed_packages)
    packages[:] = new_packages
    return removed_packages


def get_packages_by_date_interval(packages, start_date, end_date):
    packages_to_return = []
    for package in packages:
        if package.get_start_date() >= start_date and package.get_end_date() <= end_date:
            packages_to_return.append(package)
    return packages_to_return


def get_packages_by_destination_and_price(packages, destination, price):
    packages_to_return = []
    for package in packages:
        if package.get_destination() == destination and package.get_price() < price:
            packages_to_return.append(package)
    return packages_to_return


def get_packages_by_end_date(packages, end_date):
    packages_to_return = []
    for package in packages:
        if package.get_end_date() == end_date:
            packages_to_return.append(package)
    return packages_to_return


def get_no_packages_by_destination(packages, destination):
    no_packages = 0
    for package in packages:
        if package.get_destination() == destination:
            no_packages += 1
    return no_packages


def get_average_price_by_destination(packages, destination):
    no_packages = 0
    sum_price = 0
    for package in packages:
        if package.get_destination() == destination:
            no_packages += 1
            sum_price += package.get_price()
    if no_packages == 0:
        return 0
    return sum_price / no_packages


def remove_packages_by_price_and_another_destination(packages, price, destination):
    new_packages = []
    removed_packages = []
    for package in packages:
        if package.get_destination() == destination and package.get_price() <= price:
            new_packages.append(package)
        else:
            removed_packages.append(package)
    packages[:] = new_packages
    return removed_packages


def remove_packages_by_month(packages, month):
    new_packages = []
    removed_packages = []
    for package in packages:
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
    return removed_packages
