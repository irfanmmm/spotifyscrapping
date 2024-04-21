from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

browser = webdriver.Edge()
# browser = webdriver.Chrome(
#     executable_path="C:/Users/irfan/Videos/chrome-win64/chrome_proxy"
# )

browser.get("https://open.spotify.com/")
time.sleep(5)

serch_container = browser.find_elements(
    By.CLASS_NAME,
    "XiVwj5uoqqSFpS4cYOC6",
)

for item in serch_container:
    content = item.find_element(
        By.CLASS_NAME,
        "kLALqL",
    )
    print(content.text)

# print(serch_container)
# serch_container.send_keys("Hellow World")

# time.sleep(2)

# browser.find_element(By.CLASS_NAME, "gNO89b").click()

"""<span class="CardTitle__LineClamp-sc-1h38un4-0 bFhcPb">Pritam</span>"""
