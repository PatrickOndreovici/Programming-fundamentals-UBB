class Package:
    def __init__(self, start_date, end_date, destination, price):
        self.start_date = start_date
        self.end_date = end_date
        self.destination = destination
        self.price = price

    def get_start_date(self):
        return self.start_date

    def get_end_date(self):
        return self.end_date

    def get_destination(self):
        return self.destination

    def get_price(self):
        return self.price

    def set_start_date(self, start_date):
        self.start_date = start_date

    def set_end_date(self, end_date):
        self.end_date = end_date

    def set_destination(self, destination):
        self.destination = destination

    def set_price(self, price):
        self.price = price

    def __str__(self):
        return f'Data start: {self.start_date}, Data sfarsit: {self.end_date}, Destinatie: {self.destination}, Pret: {self.price}'
