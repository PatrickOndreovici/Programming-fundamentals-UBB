class Package:
    def __init__(self, package_id, start_date, end_date, destination, price):
        self._package_id = package_id
        self._start_date = start_date
        self._end_date = end_date
        self._destination = destination
        self._price = price

    def get_package_id(self):
        return self._package_id

    def get_start_date(self):
        return self._start_date

    def get_end_date(self):
        return self._end_date

    def get_destination(self):
        return self._destination

    def get_price(self):
        return self._price

    def set_start_date(self, start_date):
        self._start_date = start_date

    def set_end_date(self, end_date):
        self._end_date = end_date

    def set_destination(self, destination):
        self._destination = destination

    def set_price(self, price):
        self._price = price

    def __str__(self):
        return f'Data start: {self._start_date}, Data sfarsit: {self._end_date}, Destinatie: {self._destination}, Pret: {self._price}'
