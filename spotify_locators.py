import random, time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions




def random_initial_musician_xpath(number):
  return "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[" + str(number) + "]"

def date_of_birth_locator(driver):
  print() #unused



xpath = {

  "navigation_wheel": '//android.widget.ProgressBar',
  "signup": {
    "signup_btn": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout/android.widget.Button[1]",
    "android_acc_signup_deny_btn": '//android.widget.LinearLayout[@resource-id="com.google.android.gms:id/credential_picker_layout"]/android.widget.LinearLayout/android.widget.Button',
    "email_textfield": '//android.widget.EditText[@resource-id="com.spotify.music:id/email"]', # not really used as is directly engaged by spotify app
    "email_next_btn": '//android.widget.Button[@resource-id="com.spotify.music:id/email_next_button"]',
    "password_textfield": '//android.widget.EditText[@resource-id="com.spotify.music:id/input_password"]', # not really used as is directly engaged by spotify app
    "show_password_textfield_btn": '//android.widget.ImageButton[@resource-id="com.spotify.music:id/text_input_end_icon"]',
    "password_next_btn": '//android.widget.Button[@resource-id="com.spotify.music:id/password_next_button"]',
    "dob_editable_text_btns": "//android.widget.LinearLayout/android.widget.NumberPicker/android.widget.EditText",
    "dob_clickable_btns": "//android.widget.LinearLayout/android.widget.NumberPicker/android.widget.Button",
    "dob_next_btn": '//android.widget.Button[@resource-id="com.spotify.music:id/age_next_button"]',
    "gender_btns": '//android.view.ViewGroup/android.view.ViewGroup/android.widget.Button',
    "username_textfield": '//android.widget.EditText[@resource-id="com.spotify.music:id/name"]',
    "privacy_checkbox_btns": '//android.widget.CheckBox[@resource-id="com.spotify.music:id/switch_agree"]',
    "signup_next_btn": '//android.widget.Button[@resource-id="com.spotify.music:id/name_next_button"]',
    "recaptcha_disclosure": '//android.widget.TextView[@resource-id="com.spotify.music:id/recaptcha_disclosure"]'
  },
  "login": {
    "login_btn": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout/android.widget.Button[4]",
    "username_textfield": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.ScrollView/android.view.ViewGroup/android.widget.EditText",
    "password_textfield": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.EditText",
    "submit_login_btn": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.ScrollView/android.view.ViewGroup/android.widget.Button[1]",
    "dismiss_premium_btn": '//android.widget.TextView[@resource-id="com.spotify.music:id/dismiss_text"]'
  },
  "intro": {
    "something_went_wrong_try_again_btn": '//android.widget.Button[@resource-id="com.spotify.music:id/button_positive"]',
    "search_bar_root_btn": '//android.widget.Button[@resource-id="com.spotify.music:id/search_placeholder"]',
    "initial_musicians_follow_random_xpath": "not used", # "for pick 3 initial artists that you like" random_initial_artist_xpath()
    "initial_musicians_follow_done_btn": '//android.widget.Button[@resource-id="com.spotify.music:id/actionButton"]',
    "initial_musicians_follow_secondary_done_btn": '//android.widget.Button[@resource-id="com.spotify.music:id/secondaryActionButton"]', # when the podcast btn appears
    "great_list_listen_notnow_btn": '//android.widget.Button[2]', # '//android.widget.Button[@resource-id="com.spotify.music:id/contextual_audio_secondary_btn"]',
    "done_musicians_facepile_row": '//android.widget.LinearLayout[@resource-id="com.spotify.music:id/contextual_audio_facepile"]',
    "intro_done_btns": "//android.widget.Button",
    "intro_skip_btn": '//android.widget.Button[@resource-id="com.spotify.music:id/allboarding_skip_dialog_skip_button"]'
  },
  "bottom_bar": {
    "btns": '//android.widget.LinearLayout',
    "home_btn": '//android.widget.LinearLayout[@resource-id="com.spotify.music:id/home_tab"]',
    "search_btn": '//android.widget.LinearLayout[@resource-id="com.spotify.music:id/search_tab"]',
    "your_library_btn": '//android.widget.LinearLayout[@resource-id="com.spotify.music:id/your_library_tab"]',
    "premium_btn": '//android.widget.LinearLayout[@resource-id="com.spotify.music:id/premium_tab"]',
    "is_premium": False

  },
  "search_tab": {
    "search_bar_btn": '//android.widget.Button[@resource-id="com.spotify.music:id/find_search_field"]',
    "search_page": {
      "search_textfield": '//android.widget.frameLayout[@resource-id="com.spotify.music:id/search_placeholder"]',
      "search_results_btns": '//android.view.ViewGroup[@resource-id="com.spotify.music:id/row_root"]',
      "clear_search_btn_or_scancode": '//android.widget.ImageButton[@resource-id="com.spotify.music:id/search_right_button"]'
    },
  },
    "music_info": {
      "play_btn": '//android.view.ViewGroup[@resource-id="com.spotify.music:id/header_play_button"]',
      "like_btn": '//android.widget.ImageButton[@resource-id="com.spotify.music:id/heart_button"]',
      "shuffle_btn": '//android.widget.ImageButton[@resource-id="com.spotify.music:id/shuffle_button"]'
    },
    "music_bottom_bar": {
      "like_btn": '//android.widget.ImageButton[@resource-id="com.spotify.music:id/animated_heart_button"]',
      'stop_play_btn': '//android.widget.ImageButton[@resource-id="com.spotify.music:id/play_pause_button"]',
      "music_cover_btn": '//android.widget.ImageView[@resource-id="com.spotify.music:id/cover_image"]'
    }, # '//[@resource-id=""]'
    "music_cover_page": {
      "song_text": '//android.widget.TextView[@resource-id="com.spotify.music:id/track_info_view_title"]',
      "artist_text_btn": '//android.widget.TextView[@resource-id="com.spotify.music:id/track_info_view_subtitle"]',
      "next_btn": '//android.widget.ImageButton[@resource-id="com.spotify.music:id/next_button"]',
      "like_btn": '//android.widget.ImageButton[@resource-id="com.spotify.music:id/animated_heart_button"]'

    },
    "blocking_prompts_dismiss_btns": {
      "dismiss_premium_btn": '//android.widget.TextView[@resource-id="com.spotify.music:id/dismiss_text"]',
      "something_went_wrong_try_again_btn": '//android.widget.Button[@resource-id="com.spotify.music:id/button_positive"]'


    }
}

def update_to_prem_xpath(driver, locators: dict):
  WebDriverWait(driver, 40).until(expected_conditions.presence_of_element_located((By.XPATH, locators["bottom_bar"]["home_btn"])))
  print("checking if account is premium")
  driver.find_element(By.XPATH, xpath["bottom_bar"]["home_btn"])
  time.sleep(0.2)
  if len(driver.find_elements(By.XPATH, xpath["bottom_bar"]["premium_btn"])) == 0:
    print("user is premium")
    locators["music_info"]["play_btn"] = '//android.widget.ImageButton[@resource-id="com.spotify.music:id/button_play_and_pause"]'
    print("updated xpath selectors to premium user interface")
    locators["bottom_bar"]["is_premium"] = True # this is useless even if it was to be used, must initialize xpath as an obj instance eg class



