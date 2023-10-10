import time
from selenium import webdriver
# from bs4 import BeautifulSoup
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


# from selenium.common.exceptions import TimeoutException
# from webdriver_manager.chrome import ChromeDriverManager

# s = Service(ChromeDriverManager().install())

def get_source_code():
    url = 'https://strgstore.com/all?tfc_charact:921409[253090920]=%D0%94%D0%BB%D1%8F+%D0%BD%D1%8C%D0%BE%D0%B3%D0%BE&tfc_sort[253090920]=created:desc&tfc_quantity[253090920]=y&tfc_storepartuid[253090920]=%D0%9E%D0%B4%D1%8F%D0%B3&tfc_brand[253090920]=LEVI%27S:::M%2BRC+NOIR&tfc_div=:::&pageid=15440869&projectid=3008870'
    options = webdriver.ChromeOptions() # Этот метод позволяет клиенту определять опции и/или требования, связанные с ресурсом, или возможностями сервера, но не производя никаких действий над ресурсом и не инициируя его загрузку.
    options.add_argument("start-maximized") # start-maximized - Эта опция предночначена для того чтобы открывать окно браузера Chrome (Или другие веб-браузеры) на максимальный размер.
    driver = webdriver.Chrome(options=options) # Selenium WebDriver — это инструмент для автоматизации действий веб-браузера. В большинстве случаев используется для тестирования Web-приложений.

    driver.get(url=url)
    time.sleep(7) # time.sleep - это функция, которая задерживает процесс выполнения кода, на заданное количество времени

    items = driver.find_elements(By.CLASS_NAME, "t-store__card__textwrapper") # find.elements - возвращает список веб-элементов, соответствующих критериям поиска. Если элементы не найдены, возвращается пустой список
    for i in items:
        name = i.find_element(By.CLASS_NAME, "js-store-prod-name").text # className – строковое значение, удобно для управления всем набором классов.
        descr = i.find_element(By.CLASS_NAME, "js-store-prod-descr").text
        price = i.find_element(By.CLASS_NAME, "js-product-price").text
        print(name, descr, price)








    # for i in items_3:
    #     name = i.find_element(By.CLASS_NAME, "js-store-prod-name").text
    #     descr = i.find_element(By.CLASS_NAME, "js-store-prod-descr").text
    #     print(name, descr)

    # print(items)
    # for i in items:
    #     item = i.find_element_by_class_name(class_="js-store-prod-name")
    #     print(item)

    # while True:
    #     try:
    #         element = WebDriverWait(driver=driver, timeout=2).until(
    #             expected_conditions.presence_of_element_located((By.ID, "href"))
    #         )
    #
    #         with open("result.txt", "w") as file:
    #             file.write(element.text)
    #
    #         break
    #     except TimeoutException as _ex:
    #         print(_ex)
    #         break
    #
    #     finally:
    #         driver.close()
    #         driver.quit()





def main():
    get_source_code()


if __name__ == '__main__':
    main()
