import requests
from twilio.rest import Client

params = {
  "lat": 51.107883,
  "lon": 17.038538,
  "exclude": "current,minutely,daily,alerts",
  "appid": "28570caad2f707dbc23e20749cb130e0"
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=params)
response.raise_for_status()
data = response.json()

print(data)

client = Client("AC483fc1a82272eaa0d724b46755dd617c", "e9fb0ee7b2e72a0efaae914e505b6384")

message = client.messages.create(
  body="Join Earth's mightiest heroes. Like Kevin Bacon.",
  from_='+16076526399',
  to='+48668726336'
)