from base import chromedriver
from selenium.webdriver.common.keys import Keys
import locators
import time


def create():
    """Workorder create test"""
    title = "Freezer Issue"
    desc = "This workorder is for Refrigerator asset. Not able to deep freeze"
    duration = 56

    time.sleep(3)
    print(f"Workorder create started")
    chromedriver.find_element_by_css_selector(locators.workorder_create_btn).click()  # Click on Workorder create button
    chromedriver.find_element_by_xpath(locators.workorder_create_title).send_keys(title)  # Enter title of the workorder
    chromedriver.find_element_by_xpath(locators.workorder_create_desc).send_keys(desc)  # Enter description of the workorder

    chromedriver.find_element_by_xpath(locators.workorder_create_duration).send_keys(duration)  # Enter duration of workorder
    chromedriver.find_element_by_css_selector(locators.workorder_create_submit).click()  # Click on workorder submit button
    print(f"Workorder create finished")
    time.sleep(4)
    chromedriver.find_element_by_xpath(locators.workorder_menu).click()  # Click on Workorder menu from left side of the page


def search():
    """Workorder search test"""
    search_keyword = "freeze"

    time.sleep(11)
    search_element = chromedriver.find_element_by_name(locators.workorder_search)
    print("Search test started")
    search_element.send_keys(search_keyword)  # Search a keyword
    search_element.send_keys(Keys.ENTER)
    time.sleep(3)
    search_result = chromedriver.find_element_by_xpath(locators.searched_result)
    print(f"Work orders after performing search: {search_result.text}")  # Printing count after searching

    search_element.send_keys(Keys.CONTROL, 'a')
    search_element.send_keys(Keys.BACKSPACE)  # Clear search
    print(f"Search test finished")
    search_element.send_keys(Keys.ENTER)
    time.sleep(3)
    search_result = chromedriver.find_element_by_xpath(locators.searched_result)
    print(f"Total Work orders: {search_result.text}")  # Printing total count after clearing search


def filter_opt():
    """Workorder more option test"""

    time.sleep(2)
    print(f"Filter test started")
    chromedriver.find_element_by_css_selector(locators.bookmark_filter).click()  # Select bookmark filter to show bookmarked results
    time.sleep(3)
    chromedriver.find_element_by_css_selector(locators.bookmark_filter).click()  # Unselect bookmark filter to show all results
    time.sleep(3)
    chromedriver.find_element_by_css_selector(locators.more_filter).click()  # Clicking on additional filters option
    chromedriver.find_element_by_xpath(locators.more_filter_opt).click()  # Selecting Repeating Only option from first selection
    time.sleep(2)
    chromedriver.find_element_by_xpath(locators.filter_show_results).click()  # Clicking on show results button to apply selected filter
    time.sleep(3)
    chromedriver.find_element_by_xpath(locators.reset_filter).click()  # Click to reset filter option to default
    print(f"Filter test finished")
    time.sleep(4)

