from datetime import datetime


def validate_package_params(package_id, start_date, end_date, destination, price):
    validate_date(start_date, end_date)

    validate_destination(destination)

    validate_price(price)

    validate_package_id(package_id)


def validate_package_id(package_id):
    try:
        package_id = int(package_id)
    except ValueError:
        raise Exception("Id-ul este invalid")
def validate_date(start_date, end_date):
    try:
        if start_date is not None:
            datetime.strptime(start_date, "%Y-%m-%d")
        if end_date is not None:
            datetime.strptime(end_date, "%Y-%m-%d")
    except ValueError:
        raise Exception("data nu este valida")


def validate_no_days(no_days):
    try:
        no_days = int(no_days)
    except ValueError:
        raise Exception("Numarul de zile ar trebui sa fie un numar intreg")
    if no_days <= 0:
        raise Exception("Numarul de zile ar trebui sa fie mai mare ca 0")


def validate_price(price):
    try:
        price = float(price)
        if price <= 0:
            raise Exception("Pretul trebuie sa fie pozitiv")
    except ValueError:
        raise Exception("Pretul trebuie sa fie un numar real")


def validate_destination(destination):
    if not isinstance(destination, str) or len(destination) < 1:
        raise Exception("Destinatie invalida")


def validate_month(month):
    try:
        month = int(month)
    except ValueError:
        raise Exception("Luna trebuie sa fie un numar intreg")
    if month < 1 or month > 12:
        raise Exception("Luna trebuie sa fie un numar intre 1 si 12")
