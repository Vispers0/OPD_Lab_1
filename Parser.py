from bs4 import BeautifulSoup  # Импорт библиотеки BeautifulSoup
import requests                # Импорт библиотеки requests
from fake_useragent import UserAgent # Импорт библиотекти Fake useragent


# Функция, проводящяя парсинг сайта
def parse():
    # URL, который будем парсить
    url = 'https://pepper.ru/'
    #Создаём объект класса UserAgent для построения хедера
    ua = UserAgent(browsers=['edge'])
    #Строим хедер с рандомным UserAgent
    headers = {"User-Agent": ua.random}
    # Отправка GET-запроса на URL и запись ответа в переменную
    response = requests.get(url=url, headers=headers)
    # Вывод код ответа HTTP
    print(response.status_code)

    # Записываем ответ в объект BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")
    # Поиск всех контейнеров div, содержащих предложения со скидкой
    discounts = soup.find_all("article", class_="thread cept-thread-item thread--type-list imgFrame-container--scale thread--deal")

    # Проходимся по каждому предложению из полученных
    for item in discounts:
        # Поиск названия товара/услуги и запись в переменную
        title = item.find("a", class_="cept-tt thread-link linkPlain thread-title--list js-thread-title").get("title")
        degrees = item.find("span", class_="cept-vote-temp vote-temp vote-temp--hot")

        if degrees is not None:
            degrees = item.find("span", class_="cept-vote-temp vote-temp vote-temp--hot").text.strip()
        else:
            degrees = item.find("span", class_="cept-vote-temp vote-temp vote-temp--burn").text.strip()

        link = item.find("a", class_="cept-tt thread-link linkPlain thread-title--list js-thread-title").get("href")

        # Форматированный вывод найденных данных
        print("Товар/Услуга: " + title)
        print("Градусы: " + degrees)
        print("Ссылка: " + link)
        print("--------------------------------------------------------")
