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
import threading, time
from email_domains import domains as email_domains
from faker import Faker
from email_domains import domains as email_domains


lock = threading.Lock()


def loop():
    global lock
    print("attempting to start thread")
    fake = Faker()
    proxy_dict_list = init.proxies("proxies.txt")
    try:

        driver = init.driver("com.spotify.music", random.choice(proxy_dict_list))
    except Exception as e:
        time.sleep(100)
        raise Exception("cannot connect to a driver, most likely all devices taken, sleeping")


    while True:
        time.sleep(2)
        start_loop_time = time.perf_counter()

        print("thread loop")
        proxy.set(driver, random.choice(proxy_dict_list))
        account = init.account_to_create(fake, email_domains)
        print(account)
        auxiliary.clear_app_data(driver, ["com.spotify.music"])
        time.sleep(1)
        init.application(driver, "com.spotify.music")



        actions.sign_up(driver, account["email"], account["password"])
        proxy.reset(driver)
        proxy.set(driver, random.choice(proxy_dict_list))


        lock.acquire()
        open("accounts.txt", "a").write(account["email"] + ":" + account["password"] + "\n")
        lock.release()
        print("created in " + str(time.perf_counter() - start_loop_time) + " seconds, process time: " + str(time.process_time()))



while True:

    for _ in range(1):
        x = threading.Thread(target=loop, args=())
        x.start()
        time.sleep(5)

    time.sleep(300)

