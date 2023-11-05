import service


def show_menu():
    while True:
        print("1. Adauga pachet de calatorie")
        print("2. Modifica pachet de calatorie")
        print("3. Sterge pachete pentru o destinatie data")
        print("4. Sterge pachete care au o durata de zile mai mica decat un numar dat")
        print("5. Sterge pachete care au o pretul mai mare decat o suma data")
        print("6. Tipareste pachete care au un sejur intr-un interval dat")
        print("7. Tipareste pachete care au o destinatie data si pret mai mic decat o suma data")
        print("8. Tipareste pachete cu o anumita data de sfarsit")
        print("9. Tipareste numarul de oferte pentru o destinatie data")
        command = input(">> ")
        if command == "1":
            create_package()
        if command == "2":
            update_package()
        if command == "3":
            remove_packages_by_destination()
        if command == "4":
            remove_packages_by_no_days()
        if command == "5":
            remove_packages_by_price()
        if command == "6":
            get_packages_by_interval()
        if command == "7":
            get_packages_by_destination_and_price()
        if command == "8":
            get_packages_by_end_date()
        if command == "9":
            get_no_packages_by_destination()
        if command == "10":
            get_packages_by_interval_sorted()
        if command == "11":
            get_average_price_by_destination()
        if command == "12":
            remove_packages_by_price_and_another_destination()


def create_package():
    input_package = read_new_package()
    try:
        package = service.service_create_package(input_package["start_date"], input_package["end_date"],
                                                 input_package["destination"], input_package["price"])
        print(f"A fost creat urmatorul pachet {package}")
    except Exception as e:
        print(str(e))


def update_package():
    input_index = read_position()
    input_package = read_new_package()
    try:
        package = service.service_update_package(input_index, input_package["start_date"],
                                                 input_package["end_date"],
                                                 input_package["destination"], input_package["price"])
        print(f"Pachetul de pe pozitia {input_index} a fost modificat in {package}")
    except Exception as e:
        print(str(e))


def remove_packages_by_destination():
    input_destination = read_destination()
    try:
        removed_packages = service.service_remove_packages_by_destination(input_destination)
        print_removed_packages(removed_packages)
    except Exception as e:
        print(str(e))


def remove_packages_by_no_days():
    input_no_days = read_no_days()
    try:
        removed_packages = service.service_remove_packages_by_days(input_no_days)
        print_removed_packages(removed_packages)
    except Exception as e:
        print(str(e))


def remove_packages_by_price():
    input_price = read_price()
    try:
        remove_packages = service.service_remove_packages_by_price(input_price)
        print_removed_packages(remove_packages)
    except Exception as e:
        print(str(e))


def get_packages_by_interval():
    input_start_date = read_start_date()
    input_end_date = read_end_date()
    try:
        packages = service.service_get_packages_by_date_interval(input_start_date, input_end_date)
        print_packages(packages)
    except Exception as e:
        print(str(e))


def get_packages_by_destination_and_price():
    input_destination = read_destination()
    input_price = read_price()
    try:
        packages = service.service_get_packages_by_destination_and_price(input_destination, input_price)
        print_packages(packages)
    except Exception as e:
        print(str(e))


def get_packages_by_interval_sorted():
    input_start_date = read_start_date()
    input_end_date = read_end_date()
    try:
        packages = service.service_get_packages_by_date_interval(input_start_date, input_end_date)
        packages.sort(key=lambda x: x.price)
        print_packages(packages)
    except Exception as e:
        print(str(e))


def get_packages_by_end_date():
    input_date = read_end_date()
    try:
        packages = service.service_get_packages_by_end_date(input_date)
        print_packages(packages)
    except Exception as e:
        print(str(e))


def get_no_packages_by_destination():
    input_destination = read_destination()
    try:
        no_packages = service.service_get_no_packages_by_destination(input_destination)
        print_no_packages(no_packages)
    except Exception as e:
        print(str(e))


def get_average_price_by_destination():
    input_destination = read_destination()
    try:
        average = service.service_get_average_price_by_destination(input_destination)
        print_average(average, input_destination)
    except Exception as e:
        print(str(e))


def remove_packages_by_price_and_another_destination():
    input_price = read_price()
    input_destination = read_destination()
    try:
        remove_packages = service.service_remove_packages_by_price_and_another_destination(input_price,
                                                                                           input_destination)
        print_removed_packages(remove_packages)
    except Exception as e:
        print(str(e))


def remove_packages_by_month():
    input_month = read_month()
    try:
        removed_packages = service.service_remove_packages_by_month(input_month)
        print_removed_packages(removed_packages)
    except Exception as e:
        print(str(e))


def read_start_date():
    start_date = input("Data start: ")
    return start_date


def read_month():
    month = input("Luna: ")
    return month


def print_average(average, destination):
    print(f"Pretul mediu pentru destinatia {destination} este {average}")


def read_end_date():
    end_date = input("Data sfarsit: ")
    return end_date


def print_removed_packages(removed_packages):
    print(f"Pachetele sterse sunt: ")
    for package in removed_packages:
        print(package)


def print_packages(packages):
    print(f"Pachete returnate: ")
    for package in packages:
        print(package)


def print_no_packages(no_packages):
    print(f"Numarul de pachete este {no_packages}")


def read_new_package():
    start_date = input("Data start: ")
    end_date = input("Data sfarsit: ")
    destination = input("Destinatie: ")
    price = input("Pret: ")
    package = {
        "start_date": start_date,
        "end_date": end_date,
        "destination": destination,
        "price": price
    }
    return package


def read_position():
    index = input("Numar pachet: ")
    return index


def read_price():
    price = input("Pret: ")
    return price


def read_destination():
    destination = input("Destinatie: ")
    return destination


def read_no_days():
    no_days = input("Durata zile: ")
    return no_days
