from base import chromedriver
import locators
import time


def signup():
    """Sign Up test"""
    url = "https://app.onupkeep.com/#/login/signup"
    email = "urvi@yopmail.com"
    password = "Test1234*$"
    firstname = "Urvi"
    lastname = "Pare"
    phoneno = "09065646163"
    companyname = "JKL"
    title = "Manager"

    chromedriver.get(url)  # Get signup URL
    print(f"Signup test started")
    chromedriver.find_element_by_id(locators.signup_email).send_keys(email)  # Enter user's email
    chromedriver.find_element_by_id(locators.signup_password).send_keys(password)  # Enter user's password
    chromedriver.find_element_by_id(locators.signup_firstname).send_keys(firstname)  # Enter user's firstname
    chromedriver.find_element_by_id(locators.signup_lastname).send_keys(lastname)  # Enter user's lastname
    chromedriver.find_element_by_id(locators.signup_phoneno).send_keys(phoneno)  # Enter user's phone number
    chromedriver.find_element_by_id(locators.signup_companyname).send_keys(companyname)  # Enter user's company name
    chromedriver.find_element_by_id(locators.signup_title).send_keys(title)  # Enter user's designation
    time.sleep(2)
    chromedriver.find_element_by_xpath(locators.signup_btn).click()  # Click on signup button to signup the user
    print(f"Signup test completed")
    time.sleep(9)
