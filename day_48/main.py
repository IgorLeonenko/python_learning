from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


chrome_driver_path = "/Users/leon/projects/selenium"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://www.python.org/")
event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget li")

dict = {}

for el in event_times:
  dict[event_times.index(el)] = {
    "time": el.find_element(By.CSS_SELECTOR, "time").text,
    "event": el.find_element(By.CSS_SELECTOR, "a").text
  }

print(dict)

driver.quit()