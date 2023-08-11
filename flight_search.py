import requests
from flight_data import FlightData

flight_inputs = FlightData()


class FlightSearch:
    def __init__(self):
        self.SEARCH_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"
        self.LOCATION_ENDPOINT = "https://api.tequila.kiwi.com/locations/query"
        self.TEQUILA_API_KEY = "ASjjQRHm2eYkqEinoXK2HGVnUMtAUeol"

    def search_location(self, city):
        location_header = {
            "apikey": self.TEQUILA_API_KEY
        }
        location_parameters = {
            "term": city,
            "locale": "en-US",
            "location_types": "city"
        }

        location_request = requests.get(url=self.LOCATION_ENDPOINT, headers=location_header, params=location_parameters)
        location_data = location_request.json()
        location_data = location_data['locations'][0]["code"]

        return location_data

    def flight_price(self, city_id, min_nights):
        price_header = {
            "apikey": self.TEQUILA_API_KEY
        }

        price_parameters = {
            "fly_from": flight_inputs.departure_city,
            "fly_to": f"city:{city_id}",
            "date_from": flight_inputs.date_range_start,
            "date_to": flight_inputs.date_range_end,
            "nights_in_dst_from": min_nights,
            "nights_in_dst_to": flight_inputs.nights_max,
            "stopover_to": flight_inputs.max_stopover_time,
            "flight_type": flight_inputs.flight_type,
            "adults": flight_inputs.adults,
            "curr": flight_inputs.currency,
            "conn_on_diff_airport": 0,
            "limit": 100
        }

        price_request = requests.get(url=self.SEARCH_ENDPOINT, headers=price_header, params=price_parameters)
        price_request.raise_for_status()

        price_data = price_request.json()
        return price_data
