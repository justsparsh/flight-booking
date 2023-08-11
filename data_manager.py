import requests


class DataManager:

    def __init__(self):
        self.PRICE_DATA_ENDPOINT = "https://api.sheety.co/2b87e9d7cf284ffeec63b76681c73363/flightDeals/prices"
        self.USER_DATA_ENDPOINT = "https://api.sheety.co/2b87e9d7cf284ffeec63b76681c73363/flightDeals/users"

    def get_sheet_data_flight(self):
        get_request = requests.get(url=self.PRICE_DATA_ENDPOINT)
        data_received = get_request.json()
        data_received = data_received['prices']

        return data_received

    def get_sheet_data_user(self):

        get_request = requests.get(url=self.USER_DATA_ENDPOINT)
        user_data_received = get_request.json()
        user_data_received = user_data_received['users']

        return user_data_received

    def edit_sheet_data(self, info_list):

        for row, city_data in enumerate(info_list):
            editing_endpoint = f"{self.PRICE_DATA_ENDPOINT}/{row+2}"
            data_to_be_sent = {
                "price": city_data
            }
            requests.put(url=editing_endpoint, json=data_to_be_sent)
