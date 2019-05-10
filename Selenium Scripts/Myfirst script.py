from selenium import webdriver

driver = webdriver.Chrome("C:\\Users\\Aditi\\Python_3\\chromedriver.exe")
driver.get("http://www.indiamart.com")
driver.maximize_window()
driver.implicitly_wait(20)
driver.get_screenshot_as_file("Indiamart.png")
driver.quit()
