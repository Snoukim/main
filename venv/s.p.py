import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import json

def get_sourse_html(url):

    driver = webdriver.Chrome()
    def fetch(url, params):
        headers = params["headers"]
        body = params["body"]
        method = params["method"]
        if method == "POST":
            return requests.post(url, headers=headers, data=body)
        if method == "GET":
            return requests.get(url, headers=headers)



    products = fetch(
        "https://store.tildacdn.com/api/getproductslist/?storepartuid=580177428100&recid=253090920&c=1696252624823&getparts=true&getoptions=true&slice=1&filters%5Bcharact%3A921409%5D%5B0%5D=%D0%94%D0%BB%D1%8F%20%D0%BD%D1%8C%D0%BE%D0%B3%D0%BE&filters%5Bquantity%5D=y&filters%5Bstorepartuid%5D%5B0%5D=%D0%9E%D0%B4%D1%8F%D0%B3&filters%5Bbrand%5D%5B0%5D=LEVI%27S&filters%5Bbrand%5D%5B1%5D=M%2BRC%20NOIR&sort%5Bcreated%5D=desc&size=12",
        {
            "headers": {
                "accept": "*/*",
                "accept-language": "uk-UA,uk;q=0.9,ru-UA;q=0.8,ru;q=0.7,en-US;q=0.6,en;q=0.5",
                "sec-ch-ua": "\"Google Chrome\";v=\"117\", \"Not;A=Brand\";v=\"8\", \"Chromium\";v=\"117\"",
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "\"Windows\"",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "cross-site",
                "Referer": "https://strgstore.com/",
                "Referrer-Policy": "strict-origin-when-cross-origin"
            },
            "body": "products",
            "method": "GET"
        });
    print(products.headers)
    print(products.json())
    try:
        driver.get(url=url)
        time.sleep(5)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()




def main():
    get_sourse_html(url="https://strgstore.com/all?tfc_charact:921409[253090920]=%D0%94%D0%BB%D1%8F+%D0%BD%D1%8C%D0%BE%D0%B3%D0%BE&tfc_sort[253090920]=created:desc&tfc_quantity[253090920]=y&tfc_storepartuid[253090920]=%D0%9E%D0%B4%D1%8F%D0%B3&tfc_brand[253090920]=LEVI%27S:::M%2BRC+NOIR&tfc_div=:::&pageid=15440869&projectid=3008870")


if __name__ == '__main__':
    main()
