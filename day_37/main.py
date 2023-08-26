import requests, time, datetime as dt

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = "leon88"
GRAPHNAAME = "graph1"
PIXELA_TOKEN = "ndfrtasdp4546;as223"
headers = { "X-USER-TOKEN": PIXELA_TOKEN }

get_user = requests.get(f"https://pixe.la/@{USERNAME}")
time.sleep(1)

get_graph = requests.get(f"https://pixe.la/@{USERNAME}/graphs/{USERNAME}/graph-def", headers=headers)
time.sleep(1)

if get_user.status_code != 200:
  user_params = {
    "token": PIXELA_TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
  }
  requests.post(url=PIXELA_ENDPOINT, json=user_params)

if get_graph.status_code != 200:
  graph_params = {
    "id": USERNAME,
    "name": "Test Graph",
    "unit": "commit",
    "type": "int",
    "color": "shibafu"
  }

  graph_headers = { "X-USER-TOKEN": PIXELA_TOKEN }
  requests.post(url=f"{PIXELA_ENDPOINT}/{USERNAME}/graphs", json=graph_params, headers=headers)


pixel_params = {
  "date": dt.datetime.now().strftime("%Y%m%d"),
  "quantity": "1"
}

resp = requests.post(url=f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPHNAAME}", json=pixel_params, headers=headers)
print(resp.text)