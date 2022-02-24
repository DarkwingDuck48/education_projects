"""
    Первый день вебинара 
"""

import json
from bs4 import BeautifulSoup
from pprint import pprint
import requests


# with open("webinars.json", "rb") as fp:
#     data_json = json.load(fp)

# speakers = [x["speaker"] for x in data_json]
# pprint(speakers)

# with open("skillbox.html", "rb") as fp:
#     data = fp.read()

# soup = BeautifulSoup(data, features="html.parser")
# links = soup.find_all("a")

# pprint([item.string.strip() for item in links])


r = requests.get("https://live.skillbox.ru/")

soup = BeautifulSoup(r.content, "html.parser")
# all_names = soup.findAll(class_="webinar-card__title")
# pprint([name.string.strip() for name in all_names])

more_info = soup.find_all(class_="webinars__item")
for webinar in more_info:
    title = webinar.find(class_ = "webinar-card__title").string.strip()
    date = webinar.find(class_ = "webinar-card__date").string.strip()
    print(f"Вебинар {title} пройдет {date}")