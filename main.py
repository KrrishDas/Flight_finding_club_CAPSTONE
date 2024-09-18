#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from datetime import datetime,timedelta
from flight_search import FlightSearch

sheety_endpoint = 'https://api.sheety.co/22396092cf99c2e666dac8386a891b3e/flightDeals/prices'
ORIGIN_CITY_IATA = "BLR"

sheet = DataManager(sheety_endpoint)
sheet_data = sheet.get_sheet_data()

if sheet_data['prices'][0]["iataCode"] == "":
    from flight_search import FlightSearch
    flight_search = FlightSearch(sheet_data, "prices")
    for row in sheet_data['prices']:
        row["iataCode"] = flight_search.return_IATACode(row["city"])
sheet.put_sheet_data(sheet_data, "prices")

flight_search = FlightSearch(sheet_data, "prices")

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data['prices']:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )