from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

import keycodes
import time
def clear_app_data(driver, packages: list):

  driver.execute_script('mobile: shell', {
    'command': 'pm clear',
    'args': packages,
    'includeStderr': True,
    'timeout': 5000
  })
  print("executed data reset on " + str(packages))

def native_keyboard_type(driver, text): # be aware cannot handle many special characters, mostly only alphabet and numbers / edit: do not suggest, just copy/paste track name, will type lowercaps only
  for char in [*text]:
    driver.press_keycode(keycodes.index[char.upper()])
    #time.sleep(0.1)
  time.sleep(1)

def native_clipboard_type(driver, text):
  driver.set_clipboard_text("")
  time.sleep(0.1)
  driver.set_clipboard_text(text)
  time.sleep(0.1)
  driver.press_keycode(keycodes.index["PASTE"])
  time.sleep(0.7)


def native_click(driver, element):
  try:
    element_coords = driver.find_element(By.XPATH, element).location
    TouchAction(driver).press(None, element_coords["x"], element_coords["y"], 1).wait(50).release().perform()
  except:
    print("threw native click")
  time.sleep(0.5)

def lock_orientation(driver):

  for settings_command in [
    #"content insert --uri content://settings/system --bind name:s:accelerometer_rotation --bind value:i:0",
    #"content insert --uri content://settings/system --bind name:s:user_rotation --bind value:i:0"]:
    "settings put system accelerometer_rotation 0", "settings put system user_rotation 0"
    ]:

    driver.execute_script('mobile: shell', {
      'command': settings_command,
      'args': [],
      'includeStderr': True,
      'timeout': 5000
    })
    time.sleep(0.1)

  driver.orientation = "PORTRAIT"
  print("locked orientation")
