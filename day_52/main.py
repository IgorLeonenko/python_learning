from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

CHROME_DRIVER_PATH = "/Users/leon/projects/selenium"
SIMILAR_ACCOUNT = "olaenglund"
USERNAME = "igrleon@gmail.com"
PASSWORD = "Nd4spdmwqcpassed"

class InstaFollower:
  def __init__(self):
    self.driver = webdriver.Chrome(service=Service(CHROME_DRIVER_PATH))

  def login(self):
    self.driver.get("https://www.instagram.com/accounts/login/")
    self.driver.find_element_by_name("username").send_keys(USERNAME)
    self.driver.find_element_by_name("password").send_keys(PASSWORD)
    self.driver.find_element_by_xpath("//button[@type='submit']").click()

  def find_followers(self):
    self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")
    self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]").click()

  def follow(self):
    follow_buttons_xpath = (
      "//*/div[text()='Followers']/../../../../.."
      "/div[2]/div/div/div//*/div[text()='Follow']"
    )
    followers = self.driver.find_elements(By.XPATH, follow_buttons_xpath)
    for follower in followers:
      sleep(1)
      follower.click()