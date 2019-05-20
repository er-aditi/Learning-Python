from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome("C:\\Users\\Aditi\\Python_3\\chromedriver.exe")
driver.set_page_load_timeout(10)
driver.get("https://www.google.com/")
driver.find_element_by_name("q").send_keys("Automation step by step")
driver.find_element_by_name("btnK").submit()

time.sleep(5)
driver.close()
