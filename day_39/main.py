#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from datetime import datetime, timedelta
from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager

data_manager = DataManager()
data = data_manager.get_data()

flight_search = FlightSearch()

for row in data:
  if row['iataCode'] == '':
    iata = flight_search.get_iata_code(row['city'])
    iata_data = {
      "price": {
        "iataCode": iata,
      }
    }
    data_manager.update_data(iata_data, row['id'])

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for depart_city in data:
  flight = flight_search.search(depart_city['iataCode'], tomorrow, six_month_from_today)
  if flight is not None:
    flight_data = {
      "price": {
        "iataCode": depart_city["iataCode"],
        "lowestPrice": flight.price,
      }
    }

    if flight.price < depart_city['lowestPrice']:
      notification_manager = NotificationManager()
      notification_manager.send_sms(f"Low price alert! ${flight.price} to fly from {depart_city['city']} to {flight.destination_city}, from {flight.out_date} to {flight.return_date}.")

    data_manager.update_data(flight_data, depart_city['id'])
    print(flight_data)