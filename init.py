import random

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.by import By

import parse
import spotify_locators
import auxiliary, actions, proxy
from faker import Faker


def driver(package, initial_proxy_dict):
    print("starting driver")

    desired_caps = {
        'platformName': 'Android', 'automationName': 'UiAutomator2',
        'newCommandTimeout': 1000  # debug
    }
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    #driver.update_settings({"waitForIdleTimeout": 0})


    driver.implicitly_wait(40)



    auxiliary.clear_app_data(driver, package)
    if type(initial_proxy_dict) == dict:
        proxy.set(driver, initial_proxy_dict)



    return driver


def proxies(file_path):
    proxies = []
    with open(file_path) as file:
        for line in file:
            proxies.append(line.rstrip())
    # print(proxies)
    return proxy.parse(proxies)

def application(driver, package):
    driver.execute_script('mobile: shell', {
        'command': 'monkey -p' + package,
        'args': 1,
        'includeStderr': True,
        'timeout': 5000
    })
    time.sleep(5)
    auxiliary.lock_orientation(driver)

def account_to_create(faker, domain_list):
    return {
        "email": str.lower(faker.simple_profile()["username"] + str(random.randint(11, 999)) + "@" + random.choice(domain_list)),
        "password": str(faker.password(length=8, special_chars=False, upper_case=False))
    }

def streaming_queue(file):
    #link;random_duration?;desired_duration_secs;shuffle?;skip_rate;like_rate#comment
    stream_queue = []
    with open(file) as f:
        for line in f:
            if not "(do not delete this line)" in line:

                x = line.rstrip().split("#")[0].split(";")
                print(x)
                link = x[0]
                random_duration = True if x[1].lower() == "true" else False
                desired_duration = int(x[2])
                shuffle = True if x[3].lower() == "true" else False
                skip_rate = int(x[4])
                like_rate = int(x[5])



                stream_queue.append({
                    "link": link.split("?")[0],
                    "random_duration": random_duration,
                    "desired_duration": desired_duration,
                    "shuffle": shuffle,
                    "skip_rate": skip_rate,
                    "like_rate": like_rate,
                    "info": parse.song(link.split("?")[0]) if not "playlist" in link else parse.playlist(link.split("?")[0])

                })
    return stream_queue

def accounts_list(file):
    accounts_dict_list = []
    with open(file) as file:
        for line in file:
            accounts_dict_list.append({"email":line.rstrip().split(":")[0], "password": line.rstrip().split(":")[1]})
    return accounts_dict_list




