import random

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.by import By

import proxy
import spotify_locators
import auxiliary, actions, init

global lock
print("attempting to start thread")
proxy_dict_list = init.proxies("proxies.txt")

driver = init.driver("com.spotify.music", random.choice(proxy_dict_list))

print()

# this file is not really used anymore


