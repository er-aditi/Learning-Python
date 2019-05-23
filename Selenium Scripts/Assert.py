from selenium import webdriver

import unittest


class AssertTitle(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Chrome("C:\\Users\\Aditi\\Python_3\\chromedriver.exe")
        # driver.implicitly_wait(10)
        driver.get("https://travelingtony.weebly.com")

    def test_AssertTitle(self):
        self.assertEqual(driver.title, "Traveling Tony's Photography - Welcome")

    def tearDown(self):
        driver.quit()


if __name__ == "__main__":
    unittest.main()
print("Very Good")
    