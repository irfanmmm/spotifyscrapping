from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pyperclip
from selenium.common.exceptions import StaleElementReferenceException

browser = webdriver.Firefox()
# browser = webdriver.Chrome(
#     executable_path="C:/Users/irfan/Videos/chrome-win64/chrome_proxy"
# )

PLAYLIST_XPATH = "//div[@data-encore-id='card'][@role='group'][@class='Box__BoxComponent-sc-y4nds-0 fqjnfn Box-sc-1njtxi4-0 hscyXl aAYpzGljXQv1_zfopxaH XiVwj5uoqqSFpS4cYOC6']"

BACK_BUTTO_XPATH = "//button[@data-testid='top-bar-back-button'][@aria-label='Go back']"


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
        PLAYLIST_XPATH,
    )

    for count in range(len(playlists)):
        time.sleep(2)
        try:
            # Attempt to click on the playlist
            playlist = playlists[count]
            playlist.click()
            time.sleep(2)

            # Click To Menu Icone (:)
            clicktreedots = browser.find_element(
                By.XPATH, "//button[@aria-haspopup='menu']"
            )
            clicktreedots.click()

            time.sleep(2)

            # Click To Share Button
            share_button = browser.find_elements(
                By.XPATH, "//li[@role='presentation'][@class='rQ6LXqVlEOGZdGIG0LgP']"
            )
            share_button[3].click()

            time.sleep(2)

            # Copyd Clip Board
            # clip_parent = browser.find_element(By.XPATH, "//div[@id='tippy-5']")
            copy_clipbord = browser.find_elements(
                By.XPATH,
                "//button[@class='mWj8N7D_OlsbDgtQx5GW']",
            )
            copy_clipbord[3].click()

            # Past Url
            clipboard_content = pyperclip.paste()
            with open("playlist_content.txt", "a") as file:
                file.write(clipboard_content + "\n")

            # Back Navigation
            back_button = browser.find_element(
                By.XPATH,
                BACK_BUTTO_XPATH,
            )
            back_button.click()
            time.sleep(2)
        except StaleElementReferenceException:  # type: ignore
            # If the element becomes stale, re-find the playlists
            playlists = browser.find_elements(
                By.XPATH,
                PLAYLIST_XPATH,
            )
            if count < len(playlists):
                # Retry clicking on the playlist
                playlist = playlists[count]
                playlist.click()
                time.sleep(2)

                # Click To Menu Icone (:)
                clicktreedots = browser.find_element(
                    By.XPATH, "//button[@aria-haspopup='menu']"
                )
                clicktreedots.click()

                time.sleep(2)

                # Click To Share Button
                share_button = browser.find_elements(
                    By.XPATH,
                    "//li[@role='presentation'][@class='rQ6LXqVlEOGZdGIG0LgP']",
                )
                share_button[3].click()

                time.sleep(2)

                # Copyd Clip Board
                # clip_parent = browser.find_element(By.XPATH, "//div[@id='tippy-5']")
                copy_clipbord = browser.find_elements(
                    By.XPATH,
                    "//button[@class='mWj8N7D_OlsbDgtQx5GW']",
                )
                copy_clipbord[3].click()

                # Past Url
                clipboard_content = pyperclip.paste()
                with open("playlist_content.txt", "a") as file:
                    file.write(clipboard_content + "\n")

                # Back Navigation
                back_button = browser.find_element(
                    By.XPATH,
                    BACK_BUTTO_XPATH,
                )

                back_button.click()
                time.sleep(2)
            else:
                print("Index out of range. Skipping.")
                time.sleep(2)
                continue
        except IndexError:
            print("Index out of range. Skipping.")
            time.sleep(2)
            continue

    time.sleep(50)


# print(serch_container)
# serch_container.send_keys("Hellow World")

# time.sleep(2)

# browser.find_element(By.CLASS_NAME, "gNO89b").click()

"""<button data-testid="top-bar-back-button" aria-label="Go back" class="ql0zZd7giPXSnPg75NR0"><svg data-encore-id="icon" role="img" aria-hidden="true" class="Svg-sc-ytk21e-0 cAMMLk IYDlXmBmmUKHveMzIPCF" viewBox="0 0 16 16"><path d="M11.03.47a.75.75 0 0 1 0 1.06L4.56 8l6.47 6.47a.75.75 0 1 1-1.06 1.06L2.44 8 9.97.47a.75.75 0 0 1 1.06 0z"></path></svg></button>"""
