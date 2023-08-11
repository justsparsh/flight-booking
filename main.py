from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

manager = DataManager()
search_engine = FlightSearch()
database = FlightData()
notify = NotificationManager()


def update_codes():

    sheet_data = manager.get_sheet_data_flight()

    for city_data in sheet_data:
        city_name = city_data['city']
        city_code = search_engine.search_location(city_name)
        city_data['iataCode'] = city_code

    manager.edit_sheet_data(sheet_data)


def search_flights():
    flight_sheet_data = manager.get_sheet_data_flight()
    user_sheet_data = manager.get_sheet_data_user()
    emails = [user_data["email"] for user_data in user_sheet_data]

    for city_data in flight_sheet_data:
        city_id = city_data['iataCode']
        min_nights = city_data['minNights']
        price = database.decipher_data(search_engine.flight_price(city_id, min_nights))
        print(price)

        if price < city_data['lowestPrice']:

            message = f"Flight found from {database.cityfrom} to {database.cityto} for ${database.price}."\
                      f" There are {database.availability} seats left. Flight leaves on {database.departure_date} and you will be back on {database.arrival_date}.\n"\
                      f"There are {database.layover_to} layovers to {database.cityto} and {database.layover_from} layovers on the return.\n\n"\
                      f"Check it out: {database.url}\n"
            notify.notify(message, emails)

search_flights()
