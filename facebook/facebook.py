import os
from selenium import webdriver

chromedriver = "chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("https://www.facebook.com/")
elem = driver.find_element_by_name("email")
elem.send_keys("username")
elem1 = driver.find_element_by_name("pass")
elem1.send_keys("password")
button = driver.find_element_by_id("loginbutton")
button.click()
