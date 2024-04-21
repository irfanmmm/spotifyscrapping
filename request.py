import requests
from bs4 import BeautifulSoup

htmltags = "new.txt"
new = "filterd.txt"


USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
LANGUAGE = "en-US,en;q=0.5"
session = requests.Session()
session.headers["User-Agent"] = USER_AGENT
session.headers["Accept-Language"] = LANGUAGE
session.headers["Content-Language"] = LANGUAGE

response = session.get("https://www.bing.com/search?q=india+weather&FORM=AWRE")


op = BeautifulSoup(response.text, "html.parser")

place = op.find("span", attrs={"class": "wtr_foreGround"}).text
heat = op.find("div", attrs={"class": "wtr_currTemp b_focusTextLarge"}).text
wind = op.find("div", attrs={"class": "wtr_currWind"}).text
humidity = op.find("div", attrs={"class": "wtr_currHumi"}).text


print(place, heat, wind, humidity)

# filtered_file = open(new, "w", encoding="utf-8")


# for index in range(len(elements)):
#     print(index)

# for element in elements:
#     filtered_file.write(element.text + "\n")
#     a=element.find_all(target='_top')
#     print(a)
#     l=a.find('<a>')
#     print(l)

# filtered_file.write(str(b) + '\n')
