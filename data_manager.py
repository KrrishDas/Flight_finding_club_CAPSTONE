import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self, sheety_endpoint):
        self.sheet_URL = sheety_endpoint

    def get_sheet_data(self):
        self.response = requests.get(url=self.sheet_URL).json()
        return self.response

    def put_sheet_data(self, sheet_data, sheet_name):
        data = {}
        for entry in sheet_data[sheet_name]:
            data['price'] = entry
            endpoint = f"/{str(entry['id'])}"
            self.put_URL = self.sheet_URL + endpoint
            self.response = requests.put(url=self.put_URL, json=data)


