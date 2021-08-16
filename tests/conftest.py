import pytest
from selenium import webdriver


@pytest.fixture
def setup():
    PATH = "D:\Assessment\driver\chromedriver.exe"
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--test-type")
    driver = webdriver.Chrome(PATH, options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver


def pytest_configure(config):
    config._metadata['Project Name'] = 'Assessment'
    config._metadata['Module Name'] = 'Automation Test'
    config._metadata['Tester'] = 'Nitesh Gupta'

@pytest.mark.optinalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
