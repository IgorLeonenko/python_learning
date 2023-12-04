import smtplib
import schedule
import time
import phonenumbers
import os
import shutil
from phonenumbers import geocoder
from opencage.geocoder import OpenCageGeocode
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

## Automate an email to your boss to ask for a raise every 3 months

def send_email():
  with smtplib.SMTP("smtp.gmail.com", 587, timeout=120) as connection:
    connection.starttls()
    connection.login(user="icovers88@gmail.com", password="")
    connection.sendmail(from_addr="icovers88@gmail.com", to_addrs="myboss@gmail.com", msg=f"I want more money for my job")

schedule.every(90).days.do(send_email)

while True:
  schedule.run_pending()
  time.sleep(10)


## Automate your lights so they switch on when your phone is within the radius of your house.

HOUSE_COORDINATES = (40.7128, -74.0060)
PHONE_NUMBER = ""
RADIUS = 5

def get_phone_coords():
  my_number = phonenumbers.parse(PHONE_NUMBER)
  my_location = geocoder.description_for_number(my_number, "en")
  geocoder = OpenCageGeocode("eb05cd935de140ef8e48f9c3df48bfdc")
  query = str(my_location)
  results = geocoder.geocode(query)
  lat = results[0]['geometry']['lat']
  lng = results[0]['geometry']['lng']
  return [lat, lng]

def is_phone_nearby():
  phone_coords = get_phone_coords()
  return abs(phone_coords[0] - HOUSE_COORDINATES[0]) < RADIUS and abs(phone_coords[1] - HOUSE_COORDINATES[1]) < RADIUS

def main():
  if is_phone_nearby():
    print("Lights ON")
  else:
    print("Lights OFF")

if __name__ == "__main__":
  main()


## Automatically organise the files in your downloads folder based on file type

def organize_directory(path):
  for item in os.listdir(path):
    item_full_path = os.path.join(path, item)

    if os.path.isfile(item_full_path):
      file_extension = os.path.splitext(item)[1][1:].lower()

      if not file_extension:
        file_extension = 'Other'

      extension_dir = os.path.join(path, file_extension)
      if not os.path.exists(extension_dir):
          os.makedirs(extension_dir)

      shutil.move(item_full_path, os.path.join(extension_dir, item))

## Automate your gym class bookings

gym_url = 'http://dummygymwebsite.com/book-class'
class_to_book = 'Yoga'
your_username = 'your_username'
your_password = 'your_password'

driver = webdriver.Chrome()
driver.get(gym_url)
time.sleep(2)

username_field = driver.find_element(By.ID, 'username')
password_field = driver.find_element(By.ID, 'password')
username_field.send_keys(your_username)
password_field.send_keys(your_password)
password_field.send_keys(Keys.RETURN)
time.sleep(2)

classes = driver.find_elements(By.CLASS_NAME, 'class-item')
for gym_class in classes:
  if class_to_book in gym_class.text:
    book_button = gym_class.find_element(By.TAG_NAME, 'button')
    book_button.click()
    break

driver.quit()


## Automate books renewals
login_url = 'https://yourlibrarywebsite.com/login'
books_url = 'https://yourlibrarywebsite.com/yourbooks'

username = 'your_username'
password = 'your_password'

driver = webdriver.Chrome('/path/to/chromedriver')

driver.get(login_url)

username_field = driver.find_element(By.ID, 'username_field_id')
username_field.send_keys(username)

password_field = driver.find_element(By.ID, 'password_field_id')
password_field.send_keys(password)

password_field.send_keys(Keys.RETURN)

time.sleep(5)

driver.get(books_url)

time.sleep(5)

renew_buttons = driver.find_elements(By.CLASS_NAME, 'renew_button_class')
for button in renew_buttons:
    button.click()
    time.sleep(1)

driver.quit()

print("Books renewed successfully!")