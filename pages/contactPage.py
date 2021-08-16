from selenium.webdriver.support.select import Select
from locators.locators import testcase_1


class contactPage:

    def __init__(self, driver):
        self.driver = driver

    def enterFirstName(self, firstName):
        self.driver.find_element(*testcase_1.first_Name).send_keys(firstName)

    def enterLastName(self, lastName):
        self.driver.find_element(*testcase_1.Last_name).send_keys(lastName)

    def enterCompanyName(self, company):
        self.driver.find_element(*testcase_1.company_name).send_keys(company)

    def enterPhoneNumber(self, phoneNumber):
        self.driver.find_element(*testcase_1.phone_number).send_keys(phoneNumber)

    def enterEmail(self, email):
        self.driver.find_element(*testcase_1.email).send_keys(email)

    def enterLocation(self, location):
        Select(self.driver.find_element(*testcase_1.location)).select_by_value(location)

    def enterIndustry(self, media):
        Select(self.driver.find_element(*testcase_1.industry)).select_by_value(media)

    def enterComment(self, comment):
        self.driver.find_element(*testcase_1.comment).send_keys(comment)

    def clickOnCheckBox(self):
        self.driver.find_element(*testcase_1.checkbox_button).click()

    def submitButton(self):
        self.driver.find_element(*testcase_1.submit_button).click()


