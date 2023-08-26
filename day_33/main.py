import requests, smtplib, datetime as dt, time

MY_LAT = 51.107883
MY_LNG = 17.038538


def iss_on_position():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()["iss_position"]

    iss_lat = float(data["latitude"])
    iss_lng = float(data["longitude"])

    return MY_LAT - 5 <= iss_lat <= MY_LAT + 5 and MY_LNG - 5 <= iss_lng <= MY_LNG + 5


def is_dark():
  params = {
      "lat": MY_LAT,
      "lng": MY_LNG,
      "formatted": 0,
  }

  response = requests.get(url="https://api.sunrise-sunset.org/json", params=params)
  response.raise_for_status()
  data = response.json()

  sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
  sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
  time_now = dt.datetime.now().hour

  return sunset > time_now and sunrise < time_now


while True:
  time.sleep(60)
  if is_dark() and iss_on_position():
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user="icovers88@gmail.com", password="bcgrvlstuyongvwv")
    connection.sendmail(from_addr="icovers88@gmail.com", to_addrs="igrleon@gmail.com", msg="ISS over your head")
    connection.close()
