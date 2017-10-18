from selenium import webdriver
from selenium.webdriver.common.keys import keys

driver = webdriver.Friefox()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
