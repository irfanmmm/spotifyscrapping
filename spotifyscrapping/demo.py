from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pyperclip

browser = webdriver.Firefox()
# browser = webdriver.Chrome(
#     executable_path="C:/Users/irfan/Videos/chrome-win64/chrome_proxy"
# )

browser.get("https://open.spotify.com/")
# time.sleep(5)

serch_container = browser.find_element(
    By.XPATH,
    "//a[@aria-label='Search']",
)
serch_container.click()

time.sleep(5)
search_input = browser.find_element(
    By.XPATH,
    "//input[@maxlength='800']",
)

tab = "//a[@role='presentation']"


content = open("response.txt", "r", encoding="utf-8")
data = content.readlines()

# time.sleep(5)

playist_tab = browser.find_element(
    By.XPATH,
    "//div[@role='presentation']",
)

for item in data:
    search_input.send_keys(item)
    search_input.send_keys(Keys.ENTER)
    time.sleep(5)
    tabs = playist_tab.find_elements(By.XPATH, "//a[@class='UnwG2v9ISmcUhnjKj22Y']")
    tabs[3].click()

    time.sleep(5)
    playlists = browser.find_elements(
        By.XPATH,
        "//div[@data-encore-id='card'][@role='group'][@class='Box__BoxComponent-sc-y4nds-0 fqjnfn Box-sc-1njtxi4-0 hscyXl aAYpzGljXQv1_zfopxaH XiVwj5uoqqSFpS4cYOC6']",
    )

    for playlist in playlists:
        print(playlist)
        time.sleep(5)
        playlist.click()
        time.sleep(5)
        clicktreedots = browser.find_element(
            By.XPATH, "//button[@aria-haspopup='menu']"
        )
        clicktreedots.click()
        time.sleep(2)
        share_button = browser.find_elements(
            By.XPATH, "//li[@role='presentation'][@class='rQ6LXqVlEOGZdGIG0LgP']"
        )
        # print(share_button)
        share_button[3].click()

        time.sleep(2)

        clip_parent = browser.find_element(By.XPATH, "//div[@id='tippy-5']")

        time.sleep(2)
        copy_clipbord = clip_parent.find_elements(
            By.XPATH,
            "//button[@class='mWj8N7D_OlsbDgtQx5GW']",
        )

        # print(copy_clipbord)

        copy_clipbord[3].click()

        clipboard_content = pyperclip.paste()

        with open("playlist_content.txt", "a") as file:
            file.write(clipboard_content + "\n")

        # Go Back ...
        back_button = browser.find_element(
            By.XPATH,
            "//button[@data-testid='top-bar-back-button'][@aria-label='Go back']",
        )

        back_button.click()

        browser.refresh()

    time.sleep(50)


# print(serch_container)
# serch_container.send_keys("Hellow World")

# time.sleep(2)

# browser.find_element(By.CLASS_NAME, "gNO89b").click()

"""<button data-testid="top-bar-back-button" aria-label="Go back" class="ql0zZd7giPXSnPg75NR0"><svg data-encore-id="icon" role="img" aria-hidden="true" class="Svg-sc-ytk21e-0 cAMMLk IYDlXmBmmUKHveMzIPCF" viewBox="0 0 16 16"><path d="M11.03.47a.75.75 0 0 1 0 1.06L4.56 8l6.47 6.47a.75.75 0 1 1-1.06 1.06L2.44 8 9.97.47a.75.75 0 0 1 1.06 0z"></path></svg></button>"""
