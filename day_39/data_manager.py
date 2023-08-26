import requests
SHEETY_URL = "https://api.sheety.co/5962479fe1d6217563c0a2f7bda5526e/flightDeals/prices"
SHEETY_API_TOKEN = "Bearer 9188b6e3f9c9a577322a"

class DataManager:
  #This class is responsible for talking to the Google Sheet.
  def __init__(self):
    self.sheety_headers = {
      "content-type": "application/json",
      "Authorization": f"{SHEETY_API_TOKEN}"
    }

  def get_data(self):
    response = requests.get(url=SHEETY_URL, headers=self.sheety_headers)
    data = response.json()
    return data["prices"]

  def update_data(self, data, id):
    response = requests.put(url=f"{SHEETY_URL}/{id}", json=data, headers=self.sheety_headers)
    print(response.json())