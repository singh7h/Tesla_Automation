from selenium import webdriver


def drivers(driver):
    if driver.lower() == "chrome":
        return webdriver.Chrome("../Webdriver/chromedriver")
    else:
        print("No Driver")