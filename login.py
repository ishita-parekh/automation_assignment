from base import chromedriver
import locators
import time


def login():
    """Login test"""
    login_status = False
    url = "https://app.onupkeep.com/#/login"
    email = "ishitaparekh78@yopmail.com"
    password = "Test1234*$"

    chromedriver.get(url)  # Get login URL
    print("Login test started")
    chromedriver.find_element_by_id(locators.email).send_keys(email)  # Enter user's login email
    chromedriver.find_element_by_id(locators.password).send_keys(password)  # Enter user's login password
    chromedriver.find_element_by_css_selector(locators.login_btn).click()  # Click on login button to login the user
    time.sleep(12)
    # Verify login status of an user logged in
    if chromedriver.current_url == locators.landing_page_url:
        login_status = True
    return login_status
