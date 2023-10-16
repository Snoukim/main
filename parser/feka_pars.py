# import json
import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
driver = webdriver.Chrome(options=options)
URL = "https://ktc.ua/"
response = requests.get(URL)
soup = BeautifulSoup(response.content, "lxml")


def pars():
    driver.get(url=URL)
    time.sleep(4)
    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/ul/li[1]").click()
    time.sleep(3)
    driver.find_element(By.CLASS_NAME, "drawer__menuli").click()
    time.sleep(3)
    catalog = driver.find_elements(By.CLASS_NAME, "drawer__menulichild")
    for i in catalog:
# urls = i.find_element(By.TAG_NAME, "a").get_attribute("href")
        # print(urls)
        
    driver.find_element(By.CLASS_NAME, "drawer__menulimain").click()
    time.sleep(4)
    apple = driver.find_elements(By.CLASS_NAME, "loop__container")
    for item in apple:
        iphone = item.find_element(By.CLASS_NAME, "loop__image").get_attribute("href")

    items = driver.find_elements(By.CLASS_NAME, "loop__container")
    for an in items:
        name = an.find_element(By.CLASS_NAME, "loop__title").text
        descr = an.find_element(By.CLASS_NAME, "loop__config").text
        price = an.find_element(By.CLASS_NAME, "loop__price  ").text
        print(f"{name} | {descr} | {price} | {iphone}")

    with open("urls.txt", "w") as file:
        file.write(name, descr, price, iphone)

# name = driver.find_elements(By.CLASS_NAME, "")

    # urls = []
    # for item in catalog:
    #     item_url = item.get_attribute("href")
    #     .append(item_url)
    #     print(item_url)
    #
    # with open() as file:
    #     for url in catalog:
    #         json.dump(url, file, indent=4, ensure_ascii=False)


def main():
    pars()


if __name__ == '__main__':
    main()