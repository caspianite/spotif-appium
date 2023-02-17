import auxiliary, init, actions, play, random, threading, time
from selenium.common.exceptions import NoSuchElementException
import random_prompts, spotify_locators

def start(driver, queue, email, password):

    print("started looping playlists")
    auxiliary.clear_app_data(driver, ["com.spotify.music"])
    time.sleep(0.1)
    init.application(driver, "com.spotify.music")
    time.sleep(10)
    actions.log_in(driver, email, password)
    driver.update_settings({"waitForIdleTimeout": 0})
    while True:
        for item in queue:
            play.playlist(driver, item)


accounts_dict_list = init.accounts_list("accounts.txt")
proxy_dict_list = init.proxies("proxies.txt")
queue = init.streaming_queue("queue.txt")

print(accounts_dict_list)
print()
for account in accounts_dict_list:
    print(account)
    is_free = False
    try:

        driver = init.driver("com.spotify.music", random.choice(proxy_dict_list))
        is_free = True
    except:
        time.sleep(100)
    if is_free == True:

        x = threading.Thread(target=start, args=(driver, queue, account["email"], account["password"],))
        x.start()

    time.sleep(10)







