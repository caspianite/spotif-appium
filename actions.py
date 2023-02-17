import threading

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
import random
import auxiliary
import keycodes
import spotify_locators
import time, random_prompts

def error_retry(driver):
    driver.implicitly_wait(5)
    try:
        driver.find_element(By.XPATH, spotify_locators.xpath["intro"]["something_went_wrong_try_again_btn"]).click()
    except NoSuchElementException:
        pass
    driver.implicitly_wait(5)  # very likely to fail

def skip_intro(driver):
    try:
        driver.find_element(By.XPATH, spotify_locators.xpath["intro"]["search_bar_root_btn"])
    except NoSuchElementException:
        error_retry(driver)

    driver.press_keycode(keycodes.index["BACK"])
    time.sleep(0.2)
    driver.find_element(By.XPATH, spotify_locators.xpath["intro"]["intro_skip_btn"])
    time.sleep(1)


def close_intro(driver):
    driver.implicitly_wait(10)
    try:
        error_retry(driver)
    except NoSuchElementException:
        pass
    driver.implicitly_wait(60)
    try:
        driver.find_element(By.XPATH, spotify_locators.xpath["intro"]["search_bar_root_btn"])
    except NoSuchElementException:
        error_retry(driver)








    #WebDriverWait(driver, 40).until(expected_conditions.presence_of_element_located((By.XPATH, spotify_locators.xpath["intro"]["search_bar_root_btn"])))

    musician_xpath_id_list = []
    for i in range(1, 6):
        musician_id = random.randint(1, 12)
        while musician_id in musician_xpath_id_list:
            musician_id = random.randint(1, 12)
        musician_xpath_id_list.append(musician_id)

    for musician in musician_xpath_id_list:

        driver.find_element(By.XPATH, spotify_locators.random_initial_musician_xpath(musician)).click()
        time.sleep(0.3)
    driver.implicitly_wait(5)
    time.sleep(1)
    try:
        driver.find_element(By.XPATH, spotify_locators.xpath["intro"]["initial_musicians_follow_secondary_done_btn"]).click()
    except NoSuchElementException:
        driver.implicitly_wait(40)
        skip_intro(driver)
    driver.implicitly_wait(40)

    driver.implicitly_wait(5)
    try: # check if it also asks for podcasts
        done = driver.find_element(By.XPATH, spotify_locators.xpath["intro"]["initial_musicians_follow_done_btn"])
        done.click()
    except:
        pass

    driver.implicitly_wait(40)




    driver.find_element(By.XPATH, spotify_locators.xpath["intro"]["done_musicians_facepile_row"])
    time.sleep(10)
    driver.find_element(By.XPATH, spotify_locators.xpath["intro"]["great_list_listen_notnow_btn"]).click()
    time.sleep(3)








def sign_up(driver, email, password):
    cancel_android_prompt_coords = driver.find_element(By.XPATH, spotify_locators.xpath["login"]["login_btn"]).location
    driver.find_element(By.XPATH, spotify_locators.xpath["signup"]["signup_btn"]).click()
    time.sleep(5)
    print(cancel_android_prompt_coords)
    driver.implicitly_wait(10)
    # android_acc_login = driver.find_element(By.XPATH, spotify_locators.xpath["signup"]["android_acc_signup_deny_btn"])
    # if android_acc_login == True:
    #
    #     android_acc_login.click()

    try:
        driver.find_element(By.XPATH, spotify_locators.xpath["signup"]["email_next_btn"])
    except NoSuchElementException:
        try:

            TouchAction(driver).press(None, cancel_android_prompt_coords["x"], cancel_android_prompt_coords["y"], 1).wait(50).release().perform()
            #driver.press_keycode(keycodes.index["BACK"])
        except:
            print("threw")
            pass # touchaction will throw due to none selector argument
        time.sleep(1) # better than checking for "NONE OF THE ABOVE" selectors as it throws, backing will only hide the keyboard if the android account selection screen is not present
    driver.implicitly_wait(40)



    auxiliary.native_keyboard_type(driver, email) # next button won't work without the app detecting actual keyboard actions
    driver.find_element(By.XPATH, spotify_locators.xpath["signup"]["email_next_btn"]).click()
    #driver.update_settings({"waitForIdleTimeout": 0}) breaks DOM

    time.sleep(5)
    driver.find_element(By.XPATH, spotify_locators.xpath["signup"]["show_password_textfield_btn"]).click()
    auxiliary.native_keyboard_type(driver, password)
    driver.find_element(By.XPATH, spotify_locators.xpath["signup"]["password_next_btn"]).click()


    for btn in driver.find_elements(By.XPATH, spotify_locators.xpath["signup"]["dob_editable_text_btns"]):
        if len(btn.get_attribute("text")) == 4:
            btn.click()
            auxiliary.native_keyboard_type(driver, str(random.randint(1992, 2000)))
        if len(btn.get_attribute("text")) == 2:
            btn.click()
            auxiliary.native_keyboard_type(driver, str(random.randint(1, 27)))

    for i in range(1, random.randint(2, 10)):
        for btn in driver.find_elements(By.XPATH, spotify_locators.xpath["signup"]["dob_clickable_btns"]):
                if btn.get_attribute("text").isalpha() and len(btn.get_attribute("text")) == 3:
                    clickable_months = []
                    clickable_months.append(btn)
        random.choice(clickable_months).click()

    driver.find_element(By.XPATH, spotify_locators.xpath["signup"]["dob_next_btn"]).click()

    random.choice(driver.find_elements(By.XPATH, spotify_locators.xpath["signup"]["gender_btns"])).click()
    WebDriverWait(driver, 40).until(expected_conditions.presence_of_element_located((By.XPATH, spotify_locators.xpath["signup"]["recaptcha_disclosure"]))) # find_elements method will not throw if none found
    username_box = driver.find_element(By.XPATH, spotify_locators.xpath["signup"]["username_textfield"])

    if len(username_box.get_attribute("text")) == 0:
        username_box.send_keys(email.split("@")[0])

    privacy_checkboxes = driver.find_elements(By.XPATH, spotify_locators.xpath["signup"]["privacy_checkbox_btns"])
    if len(privacy_checkboxes) < 3: # some countries do not have the newsletter
        for checkbox in privacy_checkboxes:
            checkbox.click()
    else:

        privacy_checkboxes[0].click() # avoid the newsletter checkbox
        privacy_checkboxes[2].click()

    driver.find_element(By.XPATH, spotify_locators.xpath["signup"]["signup_next_btn"]).click()
    close_intro(driver)
    return True









def log_in(driver, email, password):
    driver.find_element(By.XPATH, spotify_locators.xpath["login"]["login_btn"]).click()
    driver.find_element(By.XPATH, spotify_locators.xpath["login"]["username_textfield"]).send_keys(email)
    driver.find_element(By.XPATH, spotify_locators.xpath["login"]["password_textfield"]).send_keys(password)
    driver.find_element(By.XPATH, spotify_locators.xpath["login"]["submit_login_btn"]).click()

    time.sleep(1)
    while len(driver.find_elements(By.XPATH, spotify_locators.xpath["navigation_wheel"])) == 1:
        driver.implicitly_wait(10)  # not sure if this even makes sense as find_elements does not throw after and won't implicitly wait
        time.sleep(1.5)
    driver.implicitly_wait(40)      # ^
    threading.Thread(target=random_prompts.poll_for_prompts, args=(driver, spotify_locators.xpath["blocking_prompts_dismiss_btns"],)).start()
    check_for_account_intro(driver, True)
    time.sleep(5)
    driver.implicitly_wait(15)
    try:
        driver.find_element(By.XPATH, spotify_locators.xpath["login"]["dismiss_premium_btn"]).click()
    except NoSuchElementException:
        pass
    driver.implicitly_wait(40)
    spotify_locators.update_to_prem_xpath(driver, spotify_locators.xpath)



def check_for_account_intro(driver, skip_if_found: bool):
    print("checking for intro")
    driver.implicitly_wait(14)
    try:
        error_retry(driver)
    except NoSuchElementException:
        pass
    driver.implicitly_wait(40)
    try:
        driver.find_element(By.XPATH, spotify_locators.xpath["intro"]["search_bar_root_btn"])
        if skip_if_found == False:

            close_intro(driver)
        else:
            skip_intro(driver)

    except NoSuchElementException:
        pass
    driver.implicitly_wait(40)


def handle_error(driver, error_dict):
    for item in error_dict:
        try:
            print()
        except:
            pass



def go_to(driver, link: str):
    # adb shell am start -a android.intent.action.VIEW spotify:playlist:4bfj9Go9YnSq7L4YeWTWeY
    # adb shell am start -a android.intent.action.VIEW spotify:playlist:4bfj9Go9YnSq7L4YeWTWeY
    print("intention to " + link)
    command_arg = "-a android.intent.action.VIEW " + link.split("?")[0].split("https://open.")[1].replace("/", ":").replace(".com", "") # this is so stupid
    x = driver.execute_script('mobile: shell', {
        'command': "am start",
        'args': [command_arg],
        'includeStderr': True,
        'timeout': 5000
    })
    print(x["stdout"])



def browse_to(driver, track_id: str): # needs exact track id
    print(track_id)
    auxiliary.native_click(driver, spotify_locators.xpath["bottom_bar"]["search_btn"]) # .click() doesn't work apparently
    time.sleep(0.1)
    driver.find_element(By.XPATH, spotify_locators.xpath["search_tab"]["search_bar_btn"]).click()
    time.sleep(1)
    driver.find_element(By.XPATH, spotify_locators.xpath["search_tab"]["search_page"]["clear_search_btn_or_scancode"])
    auxiliary.native_clipboard_type(driver, track_id)
    time.sleep(5)
    driver.find_elements(By.XPATH, spotify_locators.xpath["search_tab"]["search_page"]["search_results_btns"])[0].click()
    time.sleep(5)


