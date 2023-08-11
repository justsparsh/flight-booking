from datetime import *


class FlightData:
    def __init__(self):

        # REQUIREMENTS

        self.departure_city = "city:SIN"
        self.now = datetime.now()
        self.range_start = date(2023, 6, 24)
        self.range_end = self.range_start + timedelta(days=10)
        self.date_range_start = self.range_start.strftime("%d/%m/%Y")
        self.date_range_end = self.range_end.strftime("%d/%m/%Y")
        self.nights_min = 7
        self.nights_max = 14
        self.max_stopover_time = "24:00"
        self.currency = "SGD"
        self.flight_type = "round"
        self.adults = 1

        # DATA FOUND

        self.price = None
        self.bags_price = None
        self.availability = None
        self.departure_date = None
        self.departure_time = None
        self.arrival_date = None
        self.arrival_time = None
        self.cityfrom = None
        self.cityto = None
        self.layover_to = None
        self.layover_from = None
        self.totalPrice = None
        self.url= None

    def decipher_data(self, flight_details):
        exchange_rate = flight_details['fx_rate']

        for i in range(5):
            self.availability = flight_details['data'][i]['availability']['seats']
            if self.availability is not None:
                flight_details = flight_details['data'][i]
                break

        if self.availability is not None:
            self.price = flight_details['price']
            self.bags_price = round(flight_details['bags_price']['1']*exchange_rate, 2)

            departure_details = flight_details['route'][0]['local_departure']
            self.departure_date = departure_details.split("T")[0]
            self.departure_time = departure_details.split("T")[1].split(".")[0]

            arrival_details = flight_details['route'][-1]['local_arrival']
            self.arrival_date = arrival_details.split("T")[0]
            self.arrival_time = arrival_details.split("T")[1].split(".")[0]

            to_route = [flights_to_destination for flights_to_destination in flight_details['route'] if flights_to_destination['return'] == 0]
            self.layover_to = len(to_route) - 1
            return_route = [return_flights for return_flights in flight_details['route'] if return_flights['return'] == 1]
            self.layover_from = len(return_route) - 1

            self.cityfrom = flight_details['cityFrom']
            self.cityto = flight_details['cityTo']

            self.url = flight_details['deep_link']

        # self.totalPrice = self.price + self.bags_price

        if self.price is not None:
            return self.price
