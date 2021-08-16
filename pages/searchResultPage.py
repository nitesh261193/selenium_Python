from selenium.webdriver.common.keys import Keys
from locators.locators import *
from selenium.webdriver.common.action_chains import ActionChains




class searchResult:

    def __init__(self, driver):
        self.driver = driver

    def clickOnNextButton(self):
        self.driver.find_element(*testcase_2.next_page_button).click()

    def clickOnSearchingLink(self):
        self.driver.find_element(*testcase_2.searchingLink).click()

    def clickOnButtonWithScroll(self, element_xpath):
        element = self.driver.find_element(*element_xpath)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()

    def switchWindow(self):
        window = self.driver.window_handles[1]
        self.driver.switch_to.window(window)
        return window







