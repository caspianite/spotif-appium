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
import actions



def playlist(driver, queue_item: dict):
    duration_polling_delay = 25
    # queue_item["link"].split("/")[1]
    actions.go_to(driver, queue_item["link"])
    time.sleep(5)

    if spotify_locators.xpath["bottom_bar"]["is_premium"] == True:
        if queue_item["shuffle"] == True:
            driver.find_element(By.XPATH, spotify_locators.xpath["music_info"]["shuffle_btn"]).click()
            time.sleep(0.3)

    print(spotify_locators.xpath["music_info"]["play_btn"])
    auxiliary.native_click(driver, spotify_locators.xpath["music_info"]["play_btn"])
    driver.implicitly_wait(130) # advertisements
    time.sleep(50)
    auxiliary.native_click(driver, spotify_locators.xpath["music_bottom_bar"]["music_cover_btn"])



    # if random.randint(1, 100) <= queue_item["like_rate"]:
    #     driver.find_element(By.XPATH, spotify_locators.xpath["music_info"]["like_btn"]).click()
    #     print("like action on " + queue_item["link"])

    # if random.randint(1, 100) <= queue_item["skip_rate"]:
    #     driver.find_element(By.XPATH, spotify_locators.xpath["music_info"]["like_btn"]).click() # change
    #     print("skip action on " + queue_item["link"])




    if queue_item["random_duration"] == True:
        duration = random.randint(270, queue_item["info"]["duration"] + 350)
        print("playing " + queue_item["link"] + " for " + str(duration) + " seconds")
    else:
        duration = queue_item["desired_duration"]
        print("playing " + queue_item["link"] + " for " + queue_item["desired_duration"] + " seconds")

    playing_elapsed = 0
    last_current_song = driver.find_element(By.XPATH, spotify_locators.xpath["music_cover_page"]["song_text"]).get_attribute("text")
    last_current_artist = driver.find_element(By.XPATH, spotify_locators.xpath["music_cover_page"]["artist_text_btn"]).get_attribute("text")


    while playing_elapsed < duration:
        current_song = driver.find_element(By.XPATH, spotify_locators.xpath["music_cover_page"]["song_text"]).get_attribute("text")
        current_artist = driver.find_element(By.XPATH, spotify_locators.xpath["music_cover_page"]["artist_text_btn"]).get_attribute("text")
        seed = random.randint(1, 100)


        time.sleep(duration_polling_delay)
        if last_current_song != current_song:
            print("last playing: " + last_current_song)
            last_current_song = current_song
            print("now playing: " + current_song)

            if seed <= queue_item["like_rate"]:
                driver.find_element(By.XPATH, spotify_locators.xpath["music_cover_page"]["like_btn"]).click()
                print("like action on " + current_song)

            if seed <= queue_item["skip_rate"]:
                driver.find_element(By.XPATH, spotify_locators.xpath["music_cover_page"]["next_btn"]).click()  # change
                print("skip action on " + current_song)

            # random behavior


        playing_elapsed += duration_polling_delay







    print("finished playing " + queue_item["link"])


