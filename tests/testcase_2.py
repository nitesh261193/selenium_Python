import time
from utils.readProperties import readConfig
from pages.homePage import homePage
from pages.searchResultPage import searchResult
from locators.locators import testcase_2
from utils.logger import LogGen


class Test002:
    baseURL = readConfig.getBaseURL()
    logger = LogGen.logGen()

    def test_case_02(self, setup):
        self.logger.info("***********  Test002 Start  **********")
        self.logger.info("***********  Verify Regulator link after navigating Pages **********")
        self.driver = setup
        self.hp = homePage(self.driver)
        self.sp = searchResult(self.driver)
        self.driver.get(self.baseURL)
        self.hp.clickOnAlert()
        self.hp.clickOnSearchButton()
        self.hp.enterSearchText("govern")
        self.sp.clickOnButtonWithScroll(testcase_2.next_page_button)
        self.sp.clickOnButtonWithScroll(testcase_2.searchingLink)
        self.sp.clickOnButtonWithScroll(testcase_2.regulatory_link)
        self.sp.switchWindow()
        if self.driver.title == "Solutions | Leverage configuration accelerators Infogix":
            self.driver.close()
            self.driver.quit()
            self.logger.info("***********  Test001 passed  **********")
            self.logger.info("***********  Test001 Finished  **********")
            assert True
        else:
            self.driver.save_screenshot("D:\Assessment\screenShot\\" + "testcase_2.png")
            self.driver.close()
            self.driver.quit()
            self.logger.error("***********  Test001 Failed  **********")
            self.logger.error("***********  Test001 Finished  **********")
            assert False

