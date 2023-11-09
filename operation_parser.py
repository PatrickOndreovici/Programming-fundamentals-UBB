from service import Service

service = Service()


def parseAdd(operationElements):
    if len(operationElements) < 5:
        raise Exception("Invalid Operation")
    service.service_create_package(operationElements[1], operationElements[2], operationElements[3],
                                   operationElements[4])


def parseUpdate(operationElements):
    if len(operationElements) < 6:
        raise Exception("Invalid Operation")
    service.service_update_package(operationElements[1], operationElements[2], operationElements[3],
                                   operationElements[4], operationElements[5])


def parseDelete(operationElements):
    if len(operationElements) == 1:
        raise Exception("Invalid Operation")
    if operationElements[1] == "BY_DESTINATION":
        if len(operationElements) < 3:
            raise Exception("Invalid Operation")
        service.service_remove_packages_by_destination(operationElements[2])
    elif operationElements[1] == "BY_DAYS":
        if len(operationElements) < 3:
            raise Exception("Invalid Operation")
        service.service_remove_packages_by_days(operationElements[2])
    elif operationElements[1] == "BY_PRICE":
        if len(operationElements) < 3:
            raise Exception("Invalid Operation")
        service.service_remove_packages_by_price(operationElements[2])
    elif operationElements[1] == "BY_PRICE_AND_ANOTHER_DESTINATION":
        if len(operationElements) < 4:
            raise Exception("Invalid Operation")
        service.service_remove_packages_by_price_and_another_destination(operationElements[2], operationElements[3])
    elif operationElements[1] == "BY_MONTH":
        if len(operationElements) < 3:
            raise Exception("Invalid Operation")
        service.service_remove_packages_by_month(operationElements[2])


def undo():
    service.undo_operation()


def parse(operation):
    operationElements = operation.split(" ")
    if operationElements[0] == "ADD":
        parseAdd(operationElements)
    elif operationElements[0] == "UPDATE":
        parseUpdate(operationElements)
    elif operationElements[0] == "DELETE":
        parseDelete(operationElements)
    elif operationElements[0] == "UNDO":
        undo()
