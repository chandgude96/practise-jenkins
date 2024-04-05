import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class Test_screenshot:
    def test_screenshot(self):
        driver = webdriver.Chrome()
        driver.get("https://credence.in/")
        driver.maximize_window()
        if driver.title == "Credence":
            driver.save_screenshot("C:\\Users\\nikhi\\PycharmProjects\\practise jenkins\\Screenshots" + "Credence.png")
            driver.close()
            assert True
        else:
            print("you are at wrong place")
            driver.close()
            assert False



