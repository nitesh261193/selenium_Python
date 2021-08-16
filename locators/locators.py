from selenium.webdriver.common.by import By


class testcase_1:
    contact_button = (By.XPATH, "//a[text()='Contact']")
    alert_button = (By.XPATH, "//div[text()='Allow All']")
    first_Name = (By.XPATH, "//input[@id='FirstName']")
    Last_name = (By.XPATH, "//input[@id='LastName']")
    company_name = (By.XPATH, "//input[@id='Company']")
    email = (By.XPATH, "//input[@id='Email']")
    phone_number = (By.XPATH, "//input[@id='Phone']")
    location = (By.XPATH, "//select[@id='HQ_Location_Country__c']")
    industry = (By.XPATH, "//select[@id='Industry__c']")
    comment = (By.XPATH, "//textarea[@id='Next_Step_Comments__c']")
    checkbox_button = (By.XPATH, "//label[@id='LblConsent_to_Processing__c']")
    submit_button = (By.XPATH, "//button[@class='mktoButton']")


class testcase_2:
    search_button = (By.XPATH, "//a[@class='search-site']")
    search_text = (By.XPATH, "//input[@class='searchfor']")
    next_page_button = (By.XPATH, "//a[text()='Next Page']")
    scroll_text = (By.XPATH, "//a[text()='What is Data Governance?']")
    searchingLink = (By.XPATH, "//a[text()='Building Data Trust with Strategic Data Governance']")
    regulatory_link = (By.XPATH, "//a[text()='regulatory compliance']")
