import smtplib
import datetime as dt
import random

my_mail = "icovers88@gmail.com"
now = dt.datetime.now()

if now.weekday() == 5:
  with open("quotes.txt", "r") as file:
    read_quotes = file.readlines()
    quotes = [el.replace("\n", "") for el in read_quotes]

  random_quote = random.choice(quotes)
  with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_mail, password="bcgrvlstuyongvwv")
    connection.sendmail(from_addr=my_mail, to_addrs="igrleon@gmail.com", msg=f"{random_quote}")
