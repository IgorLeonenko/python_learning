import requests
import pprint
from flight_data import FlightData


API_KEY = "uMR8oE_XXmPCsZy1bV8dwQ2bnKUmbgbL"
URL = "https://api.tequila.kiwi.com/"

class FlightSearch:
  #This class is responsible for talking to the Flight Search API.

  def __init__(self):
    self.location_url = f"{URL}locations/query"
    self.search_url = f"{URL}v2/search"
    self.headers = { "apikey": API_KEY }

  def get_iata_code(self, city_name):
    city_params = { "term": city_name }

    search_response = requests.get(url=self.location_url, params=city_params, headers=self.headers)
    return search_response.json()["locations"][0]["code"]

  def search(self, ds_city_code, date_from, date_to):
    search_params = {
      "fly_from": "WRO",
      "fly_to": ds_city_code,
      "date_from": date_from.strftime("%d/%m/%Y"),
      "date_to": date_to.strftime("%d/%m/%Y"),
      "nights_in_dst_from": 7,
      "nights_in_dst_to": 28,
      "flight_type": "round",
      "one_for_city": 1,
      "max_stopovers": 0,
      "curr": "PLN"
    }
    response = requests.get(url=self.search_url, params=search_params, headers=self.headers)

    try:
      search_result = response.json()["data"][0]
    except IndexError:
      search_params["max_stopovers"] = 1
      response = requests.get(url=self.search_url, params=search_params, headers=self.headers)
      search_result = response.json()["data"][0]

      flight_data = FlightData(
        price=search_result["price"],
        origin_city=search_result["route"][0]["cityFrom"],
        origin_airport=search_result["route"][0]["flyFrom"],
        destination_city=search_result["route"][1]["cityTo"],
        destination_airport=search_result["route"][1]["flyTo"],
        out_date=search_result["route"][0]["local_departure"].split("T")[0],
        return_date=search_result["route"][1]["local_departure"].split("T")[0],
        stop_overs=1,
        via_city=search_result["route"][0]["cityTo"]
      )
      return flight_data
    else:
      flight_data = FlightData(
        price=search_result["price"],
        origin_city=search_result["route"][0]["cityFrom"],
        origin_airport=search_result["route"][0]["flyFrom"],
        destination_city=search_result["route"][0]["cityTo"],
        destination_airport=search_result["route"][0]["flyTo"],
        out_date=search_result["route"][0]["local_departure"].split("T")[0],
        return_date=search_result["route"][1]["local_departure"].split("T")[0]
      )
      return flight_data


