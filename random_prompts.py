from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
import random
import auxiliary
import keycodes
import spotify_locators
import time

def poll_for_prompts(driver, elements_xpaths):
    print("started random prompt handler")
    while True:

        # for element in elements_xpaths:
        #     e = driver.find_elements(By.XPATH, element)
        #     len(e)
        #     if len(e) > 0:
        #         for el in e:
        #             auxiliary.native_click(driver, el)
        #             print("closed prompt")

        elements = driver.find_elements(By.XPATH, '//*[@resource-id]')

        for element in elements:

            for key in elements_xpaths.values():
                # print(element.get_attribute("resource-id"))
                # print(key)
                if element.get_attribute("resource-id") == key.split('[@resource-id="')[1].strip('"]'):
                    auxiliary.native_click(driver, element)

        time.sleep(25) # need way to make non-blocking

