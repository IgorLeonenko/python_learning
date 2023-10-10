from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://steamdb.info/")

rows = driver.find_elements(By.CSS_SELECTOR, ".span6:first-of-type table:nth-of-type(1) tbody tr")

data = {}

data = {
  "name": [row.find_element(By.CSS_SELECTOR, ".css-truncate").text for row in rows[:15]],
  "image": [row.find_element(By.CSS_SELECTOR, "img").get_attribute('src') for row in rows[:15]],
  "people_online": [row.find_element(By.CSS_SELECTOR,"td:nth-of-type(3)").text for row in rows[:15]],
  "daily_peak": [row.find_element(By.CSS_SELECTOR,"td:nth-of-type(4)").text for row in rows[:15]],
}

df = pd.DataFrame(data)
df.to_csv('output.csv', index=False)

driver.quit()