import asyncio

import aiohttp
from bs4 import BeautifulSoup as BS
from fake_useragent import UserAgent

BASE_URL = "https://ktc.ua/notebook/brand-dream_machines/?sort-price-asc"
HEADERS = {"User-Agent": UserAgent().random}


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get(BASE_URL, headers=HEADERS) as response:
            r = await aiohttp.StreamReader.read(response.content)
            soup = BS(r,"html.parser")

            items = soup.find_all("div", {"class": "loop"})
            for item in items:
                title = item.find("a", {"class": "loop__title"})
                link = title.get("href")
                price = item.find("div", {"class": "loop__pb"}).text.strip()
                img = item.find("source").get('srcset')
                price1 = item.find("del")
                if price1 != None:
                    print(f"TITLE: {title.text.strip()} | {str(price1.text)+'/'+price[len(price1.text):]} | https://ktc.ua{link} | {img}")
                # short_price = Shortener().tinyurl.short(f"https://ktc.ua{link}")
                else:
                    print(f"TITLE: {title.text.strip()} | {price} | https://ktc.ua{link} | {img}")


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())




































# import requests
# from bs4 import BeautifulSoup as BS
#
# r = requests.get("https://ktc.ua/notebook/brand-dream_machines/?sort-price-asc/page=1")
# html = BS(r.content, 'html.parser')

# for el in html.select(".js-looplist > .loop__container"):
#     title = el.select('.caption > a')
#     print(title[0].text)

# cookies = {
#     '_kd': 'sG88q2UKFpsE+XnZBFJhAg==',
#     '_gcl_au': '1.1.1657284352.1695159965',
#     'g_state': '{"i_l":0}',
#     'user_phone': '%2B380687745727',
#     'user_name': '%D0%9F%D0%BB%D0%B5%D1%82%D0%BD%D1%8C%D0%BE%D0%B2%20%D0%9E%D0%BB%D0%B5%D0%BA%D1%81%D1%96%D0%B9%20%D0%AE%D1%80%D1%96%D0%B9%D0%BE%D0%B2%D0%B8%D1%87',
#     'c': 'fe5bfdd02587d18c85a329b8fe29b269_23542233_1695159970',
#     'c_u': '2',
#     'city_id': '29713%3A%D0%9A%D0%B8%D1%97%D0%B2',
#     'sbjs_migrations': '1418474375998%3D1',
#     'sbjs_current_add': 'fd%3D2023-10-10%2012%3A48%3A06%7C%7C%7Cep%3Dhttps%3A%2F%2Fktc.ua%2F%7C%7C%7Crf%3D%28none%29',
#     'sbjs_first_add': 'fd%3D2023-10-10%2012%3A48%3A06%7C%7C%7Cep%3Dhttps%3A%2F%2Fktc.ua%2F%7C%7C%7Crf%3D%28none%29',
#     'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29',
#     'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29',
#     '_gid': 'GA1.2.473008948.1696931291',
#     'city': '29713:%D0%9A%D0%B8%D1%97%D0%B2',
#     '_ga_ss': '2cc01e08675cdc5e74693965f37e8a4a',
#     'c_l': '2cc01e08675cdc5e74693965f37e8a4a_%2B380687745727_loshapletnov01%40gmail.com',
#     '_gcl_al': 'MTI1MjU5Mi8vYjZjNDM0MDI4NjhhNzA0Njk3N2Y3ZTMxNGFkYzM4Mjc%3D',
#     'sbjs_udata': 'vst%3D12%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F117.0.0.0%20Safari%2F537.36',
#     'ccnt': '0',
#     'open_supportman': '2',
#     'sbjs_session': 'pgs%3D4%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fktc.ua%2Fnotebook%2Fbrand-dream_machines%2F%3Fsort-price-asc',
#     '_ga_4TCE34ZT6D': 'GS1.1.1697095522.10.1.1697096420.50.0.0',
#     '_ga': 'GA1.2.1243782994.1695159965',
#     '_gat_UA-20310467-1': '1',
# }
#
# headers = {
#     'authority': 'ktc.ua',
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#     'accept-language': 'uk-UA,uk;q=0.9,ru-UA;q=0.8,ru;q=0.7,en-US;q=0.6,en;q=0.5',
#     'cache-control': 'max-age=0',
#     # 'cookie': '_kd=sG88q2UKFpsE+XnZBFJhAg==; _gcl_au=1.1.1657284352.1695159965; g_state={"i_l":0}; user_phone=%2B380687745727; user_name=%D0%9F%D0%BB%D0%B5%D1%82%D0%BD%D1%8C%D0%BE%D0%B2%20%D0%9E%D0%BB%D0%B5%D0%BA%D1%81%D1%96%D0%B9%20%D0%AE%D1%80%D1%96%D0%B9%D0%BE%D0%B2%D0%B8%D1%87; c=fe5bfdd02587d18c85a329b8fe29b269_23542233_1695159970; c_u=2; city_id=29713%3A%D0%9A%D0%B8%D1%97%D0%B2; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2023-10-10%2012%3A48%3A06%7C%7C%7Cep%3Dhttps%3A%2F%2Fktc.ua%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2023-10-10%2012%3A48%3A06%7C%7C%7Cep%3Dhttps%3A%2F%2Fktc.ua%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29; _gid=GA1.2.473008948.1696931291; city=29713:%D0%9A%D0%B8%D1%97%D0%B2; _ga_ss=2cc01e08675cdc5e74693965f37e8a4a; c_l=2cc01e08675cdc5e74693965f37e8a4a_%2B380687745727_loshapletnov01%40gmail.com; _gcl_al=MTI1MjU5Mi8vYjZjNDM0MDI4NjhhNzA0Njk3N2Y3ZTMxNGFkYzM4Mjc%3D; sbjs_udata=vst%3D12%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F117.0.0.0%20Safari%2F537.36; ccnt=0; open_supportman=2; sbjs_session=pgs%3D4%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fktc.ua%2Fnotebook%2Fbrand-dream_machines%2F%3Fsort-price-asc; _ga_4TCE34ZT6D=GS1.1.1697095522.10.1.1697096420.50.0.0; _ga=GA1.2.1243782994.1695159965; _gat_UA-20310467-1=1',
#     'dnt': '1',
#     'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
#     'sec-fetch-dest': 'document',
#     'sec-fetch-mode': 'navigate',
#     'sec-fetch-site': 'none',
#     'sec-fetch-user': '?1',
#     'upgrade-insecure-requests': '1',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
# }
#
# response = requests.get(
#     "https://ktc.ua/notebook/brand-dream_machines/?sort-price-asc",
#          cookies=cookies,
#          headers=headers,
#
# )
# html = response.text
# print(html)
# def parsing():
#     names = []
#     response = requests.get('https://ktc.ua/notebook/brand-dream_machines/?sort-price-asc',
#         cookies=cookies, headers=headers)
#     html = response.text
#     soup = BeautifulSoup(html,"lxml")
#     catalog = soup.find_all("div", class_="loop__container")
#     for block in catalog:
#         name = block.find_all("a", class_="loop__title")
#         price = block.find_all("div", "loop__price")
#         print(f"name: {name}\n"
#               f"price: {price}\n")
        # print(price)

   # for item in name:
     #    k = names.append(i)
    #    for s in price:
    #        print(item.text, s.text)
        # data_brand = soup.find("a", class_="loop__title")
        # data_price = soup.find("div", class_="loop__price")
    # for i in data_brand, data_price:
    #    all_info = i
    #    print(all_info.text)


    # products = response["products"]
    # for item in products:
    #     data_brand = item["data-brand"]
    #     data_name = item["data-name"]
    #     data_price = item["data-price"]
    #     data_images = item["data-images"]
    #
    #     lines = [f"data-brand:{data-brand}\n"
    #              f"data-name: {data-name}\n"
    #              f"data-price: {data-price}\n"
    #              f"data-images:{data-images}\n"]
    #
    #     with open(r"dream.machines.py.txt", "w") as file:
    #         for line in lines:
    #             file.write(line + '\n')


# def main():
#     parsing()
#
#
# if __name__ == '__main__':
#     main()