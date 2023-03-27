from bs4 import BeautifulSoup  # Импорт библиотеки BeautifulSoup
import requests                # Импорт библиотеки requests


# Функция, проводящяя парсинг сайта
def parse():
    # URL, который будем парсить
    url = 'https://omsk.biglion.ru/services/entertainment/'
    # Отправка GET-запроса на URL и запись ответа в переменную
    response = requests.get(url)
    # Вывод код ответа HTTP
    print(response.status_code)

    # Записываем ответ в объект BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")
    # Поиск всех контейнеров div, содержащих предложения со скидкой
    discounts = soup.find_all("div", class_="card-item item bservices__deals_item")
    # Первая половина для составления ссылки на товар/услугу
    link_base = "https://omsk.biglion.ru/"

    # Проходимся по каждому предложению из полученных
    for item in discounts:
        # В конце списка есть элемент, который содержит только картинку. Он игнорируется
        if item.get("data-id") == "4984627":
            break

        # Поиск названия товара/услуги и запись в переменную
        title = item.find("a", class_="card-item__title").text
        # Поиск размера скидки товара/услуги и запись в переменную
        discount = item.find("span", class_="card-item__discount").text
        # Поиск цены со скидкой товара/услуги и запись в переменную
        new_price = item.find("span", class_="dc__price_new").text.strip().replace("\n", "").replace(" ", "")
        # Поиск ссылки на покупку товара/услуги и запись в переменную
        link = item.find("a", class_="card-item__title").get("href")

        # Форматированный вывод найденных данных
        print("Товар/Услуга: " + title)
        print("Цена: " + new_price + " (скидка " + discount + ")")
        print("Ссылка: " + link_base + link)
        print("--------------------------------------------------------")
