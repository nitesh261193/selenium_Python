import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.contactPage import contactPage
from pages.homePage import homePage
from utils.logger import LogGen
from utils.readProperties import readConfig


class Test001:
    baseURL = readConfig.getBaseURL()
    log = LogGen.logGen()

    def test_case_01(self, setup):
        self.log.info("***********  Test001 Start  **********")
        self.log.info("***********  Verify Thank You Message after completing contact Form **********")
        self.driver = setup
        self.hp = homePage(self.driver)
        self.cp = contactPage(self.driver)
        self.driver.get(self.baseURL)
        self.hp.clickOnAlert()
        self.hp.clickOnContactButton()
        self.cp.enterFirstName("Nitesh")
        self.cp.enterLastName("Gupta")
        self.cp.enterCompanyName("Infogix HR")
        self.cp.enterPhoneNumber("0894162509")
        self.cp.enterEmail("nitesh261193@gmail.com")
        self.cp.enterLocation('United States')
        self.cp.enterIndustry('Media & Communication')
        self.cp.enterComment("This is a coding challenge for Test Automation position. Please disregard this message")
        self.cp.clickOnCheckBox()
        self.cp.submitButton()
        time.sleep(5)
        message = WebDriverWait(self.driver, 10000).until(EC.visibility_of_element_located((By.TAG_NAME, "h1")))
        if message.text == "Thank You!":
            self.driver.close()
            assert True
            self.log.info("***********  Test001 passed  **********")
            self.log.info("***********  Test001 finished  **********")
        else:
            self.driver.save_screenshot("D:\Assessment\screenShot\\" + "testcase_1.png")
            self.driver.close()
            self.log.error("***********  Test001 Failed  **********")
            self.log.error("***********  Test001 finished  **********")
            assert False



