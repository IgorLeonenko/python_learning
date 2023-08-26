from bs4 import BeautifulSoup
import requests, smtplib

URL = "https://www.amazon.com/GoPro-Waterproof-Action-Accessory-Commerce/dp/B091G1TJ32/"

headers = {
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
  "Accept-Language": "en-US,en;q=0.9"
}
amazon_page = requests.get(URL, headers=headers)

soup = BeautifulSoup(amazon_page.text, "lxml")

price = soup.find(class_="a-offscreen").get_text()
price = float(price.split("$")[1])

price = 170

if price < 190:
  with smtplib.SMTP("smtp.gmail.com", 587, timeout=120) as connection:
    connection.starttls()
    connection.login(user="icovers88@gmail.com", password="bcgrvlstuyongvwv")
    connection.sendmail(from_addr="icovers88@gmail.com", to_addrs="igrleon@gmail.com", msg=f"Subject:GoPro8 now lower then 190$\n{URL}".encode("utf-8"))