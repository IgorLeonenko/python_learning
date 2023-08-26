import requests
SHEETY_URL = "https://api.sheety.co/5962479fe1d6217563c0a2f7bda5526e/flightDeals/users"
SHEETY_API_TOKEN = "Bearer 9188b6e3f9c9a577322a"

class UsersManager:
  def __init__(self):
    self.sheety_headers = {
      "content-type": "application/json",
      "Authorization": f"{SHEETY_API_TOKEN}"
    }

  def add_user(self, data):
    response = requests.post(url=f"{SHEETY_URL}", json=data, headers=self.sheety_headers)
    print(response.json())