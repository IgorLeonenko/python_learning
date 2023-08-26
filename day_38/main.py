import requests, datetime as dt

NUTRITION_API_ID = "98ad4a0d"
NUTRITION_API_KEY = "d0eaeeec2c221a64ef5631ac5005f9be"
NUTRITION_URL = "https://trackapi.nutritionix.com"
SHEETY_URL = "https://api.sheety.co/5962479fe1d6217563c0a2f7bda5526e/workoutTracking/workouts"
SHEETY_API_TOKEN = "b9ae157b0f926e116d7a"


def get_nutririon_data():
  user_input = input("Tell me which exercises you did: ")
  exercise_endpoint = "/v2/natural/exercise"
  exercise_endpoint_headers = {
    "x-app-id": NUTRITION_API_ID,
    "x-app-key": NUTRITION_API_KEY,
    "content-type": "application/json"
  }

  exercise_body = {
    "query": user_input,
  }

  exercises_response = requests.post(f"{NUTRITION_URL}{exercise_endpoint}", json=exercise_body, headers=exercise_endpoint_headers)
  exercises_response.raise_for_status()
  return exercises_response.json()



exercises_data = get_nutririon_data()
for exercises_response in exercises_data["exercises"]:
  sheety_body = {
    "workout": {
      "date": dt.datetime.now().strftime("%d/%m/%Y"),
      "time": dt.datetime.now().strftime("%H:%M:%S"),
      "duration": exercises_response["duration_min"],
      "exercise": exercises_response["user_input"].title(),
      "calories": exercises_response["nf_calories"],
    }
  }

  sheety_headers = {
    "content-type": "application/json",
    "Authorization": f"Bearer {SHEETY_API_TOKEN}"
  }
  requests.post(SHEETY_URL, json=sheety_body,  headers=sheety_headers)