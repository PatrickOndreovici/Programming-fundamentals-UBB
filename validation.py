from datetime import datetime


def validate_package_params(start_date, end_date, destination, price):
    validate_date(start_date, end_date)

    validate_destination(destination)

    validate_price(price)


def validate_date(start_date, end_date):
    try:
        if start_date is not None:
            datetime.strptime(start_date, "%Y-%m-%d")
        if end_date is not None:
            datetime.strptime(end_date, "%Y-%m-%d")
    except ValueError:
        raise Exception("start_date and end_date must be valid dates in the format YYYY-MM-DD")


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
            raise Exception("price should be a positive double")
    except ValueError:
        raise Exception("price should be a positive double")


def validate_destination(destination):
    if not isinstance(destination, str) or len(destination) < 1:
        raise Exception("destination should be a non-empty string")


def validate_month(month):
    try:
        month = int(month)
    except ValueError:
        raise Exception("Luna trebuie sa fie un numar intreg")
    if month < 1 or month > 12:
        raise Exception("Luna trebuie sa fie un numar intre 1 si 12")
