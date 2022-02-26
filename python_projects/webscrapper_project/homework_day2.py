import time

from selenium import webdriver
from selenium.webdriver.common.by import By



browser = webdriver.Chrome()

# Заходим на сайт 
browser.get("https://auto.ru/")

# Находим кнопку LADA в главных 
LADA_XPATH = '//*[@id="LayoutIndex"]/div/div/div[1]/div/div[1]/div[3]/div/div[1]/a[1]'
lada_link = browser.find_element(by=By.XPATH, value=LADA_XPATH)
lada_link.click()
time.sleep(3)


# Чекбокс "В кредит"
CRED_XPATH = '/html/body/div[2]/div/div[2]/div[3]/div[2]/div/div[2]/div/div[2]/div[1]/div[2]/label'
cred_link = browser.find_element(by=By.XPATH, value=CRED_XPATH)
cred_link.click()
time.sleep(2)

# Находим кнопку Показать предложения через брата
parent_div = cred_link.find_element(by=By.XPATH, value="..//..")
button_show_prices = parent_div.find_element(by=By.XPATH, value="following-sibling::div[2]/div[3]/button")
button_show_prices.click()
time.sleep(2)

# Парсим цены на странице
offers = browser.find_elements(by=By.CLASS_NAME, value="ListingItem")
for offer in offers:
    price = offer.find_element(by=By.XPATH, value="div/div[2]/div[1]/div[1]/div[2]/div[1]/div")
    print(price.text)

# Сортируем выдачу по возрастанию
current_url = browser.current_url
browser.get(current_url+"?sort=price-asc")
time.sleep(1)
offer_first = browser.find_element(by=By.CLASS_NAME, value="ListingItem")
title = offer_first.find_element(by=By.TAG_NAME, value="h3")
price = offer_first.find_element(by=By.XPATH, value="div/div[2]/div[1]/div[1]/div[2]/div[1]/div")
print(f"Самая низкая цена {title.text} - {price.text}")

browser.close()
