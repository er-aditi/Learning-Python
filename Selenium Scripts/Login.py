from selenium import webdriver
from selenium.webdriver import ActionChains


driver = webdriver.Chrome("C:\\Users\\Aditi\\Python_3\\chromedriver.exe")
driver.get("https://www.indiamart.com/")


actions = ActionChains(driver)
SignIn = driver.find_element_by_class_name('ico-usr')
onclick = driver.find_element_by_class_name('cont_s')

actions.move_to_element(SignIn).move_to_element(onclick).click().perform()

driver.find_element_by_name('mobile').send_keys('7000219516')
driver.find_element_by_name('start').click()


