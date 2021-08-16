from selenium.webdriver.common.keys import Keys
from locators.locators import *


class homePage:

    def __init__(self, driver):
        self.driver = driver

    def clickOnContactButton(self):
        self.driver.find_element(*testcase_1.contact_button).click()

    def clickOnSearchButton(self):
        self.driver.find_element(*testcase_2.search_button).click()

    def clickOnAlert(self):
        self.driver.find_element(*testcase_1.alert_button).click()

    def enterSearchText(self, text):
        self.driver.find_element(*testcase_2.search_text).send_keys(text)
        self.driver.find_element(*testcase_2.search_text).send_keys(Keys.RETURN)



