import repository
import validation

packages = []


def service_create_package(start_date, end_date, destination, price):
    validation.validate_package_params(start_date, end_date, destination, price)
    return repository.create_package(packages, start_date, end_date, destination, price)


def service_update_package(index, start_date, end_date, destination, price):
    validation.validate_package_params(start_date, end_date, destination, price)
    if index > len(packages) or index < 1:
        raise Exception("Nu exista pachetul de pe pozitia " + index)
    return repository.update_package(packages, index, start_date, end_date, destination, price)


def service_remove_packages_by_destination(destination):
    return repository.remove_packages_by_destination(packages, destination)


def service_remove_packages_by_days(no_days):
    validation.validate_no_days(no_days)
    return repository.remove_packagse_by_days(packages, no_days)


def service_remove_packages_by_price(price):
    validation.validate_price(price)
    return repository.remove_packages_by_price(packages, price)


def service_get_packages_by_date_interval(start_date, end_date):
    validation.validate_date(start_date, end_date)
    return repository.get_packages_by_date_interval(packages, start_date, end_date)
