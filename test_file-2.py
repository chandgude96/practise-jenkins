import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class Test_login:
    def test_loginurl_01(self):
        driver = webdriver.Chrome()
        driver.get("https://automation.credence.in//login")
        driver.maximize_window()

        driver.find_element(By.XPATH, "//input[@id='email']").send_keys("Credence@1test.com")
        driver.find_element(By.XPATH, "//input[@id='password']").send_keys("Credence@9656")
        time.sleep(5)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
