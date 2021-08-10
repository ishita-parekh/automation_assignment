from selenium import webdriver

driver_path = "E:/AutomationDriver/chromedriver_win32/chromedriver.exe"
# Creating driver instance
chromedriver = webdriver.Chrome(executable_path=driver_path)


def set_up():
    """Set up function"""
    chromedriver.implicitly_wait(10)  # Set implicit wait of 10 secs
    chromedriver.maximize_window()  # Maximize browser window


def tear_down():
    """Tear down function"""
    chromedriver.close()  # Close browser tabs if only one tab will close browser
    chromedriver.quit()  # Close browser
