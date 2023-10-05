import requests

headers = {
    'authority': 'store.tildacdn.com',
    'accept': '*/*',
    'accept-language': 'uk,en-US;q=0.9,en;q=0.8,ru;q=0.7,uk-UA;q=0.6',
    'dnt': '1',
    'origin': 'https://strgstore.com',
    'referer': 'https://strgstore.com/',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 '
                  'Safari/537.36',
}

params = {
    'storepartuid': '580177428100',
    'recid': '253090920',
    'c': '1695643452804',
    'getparts': 'true',
    'getoptions': 'true',
    'slice': '1',
    'filters[charact:921409][0]': 'Для нього',
    'filters[quantity]': 'y',
    'filters[storepartuid][0]': 'Одяг',
    'filters[brand][0]': "LEVI'S",
    'filters[brand][1]': 'M+RC NOIR',
    'sort[created]': 'desc',
    'size': '12',
}


def parsing():
    response = requests.get(
        'https://store.tildacdn.com/api/getproductslist/?storepartuid=580177428100&recid=253090920&c=1695646813947'
        '&getparts=true&getoptions=true&slice=1&filters%5Bcharact%3A921409%5D%5B0%5D=%D0%94%D0%BB%D1%8F%20%D0%BD%D1'
        '%8C%D0%BE%D0%B3%D0%BE&filters%5Bquantity%5D=y&filters%5Bstorepartuid%5D%5B0%5D=%D0%9E%D0%B4%D1%8F%D0%B3'
        '&filters%5Bbrand%5D%5B0%5D=LEVI%27S&filters%5Bbrand%5D%5B1%5D=M%2BRC%20NOIR&sort%5Bcreated%5D=desc&size=12',
        params=params, headers=headers).json()

    products = response["products"]
    for item in products:
        title = item["title"]
        price = item["price"]
        size = item["descr"]
        gallery = item["gallery"]

        lines = [f"title:{title}\n"
                 f"size: {size}\n"
                 f"price: {price}\n"
                 f"gallery:{gallery}\n"]

        with open(r"first.py.txt", "aa") as file:
            for line in lines:
                file.write(line + '\n')


def main():
    parsing()


if __name__ == '__main__':
    main()
