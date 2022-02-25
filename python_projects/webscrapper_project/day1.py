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
more_info = soup.find_all(class_="webinars__item")
# Домашнее задание
for webinar in more_info:
    duration = webinar.select("span.duration.webinar-card__duration").string.strip()
    title = webinar.find(class_ = "webinar-card__title").string.strip()
    date = webinar.find(class_ = "webinar-card__date").string.strip()
    views = webinar.select("span.webinar-views.webinar-card__views").string.strip()
    print(f"Вебинар {title} длительностью {duration} прошел {date}. Его просмотрели {views} раз." )

# test = more_info[0]
# views = test.select("span.webinar-views.webinar-card__views")
# print(views[0].text.strip())