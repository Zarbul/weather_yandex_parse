from bs4 import BeautifulSoup
import requests

inp = str(input('Введите годод...\n'))
URL = 'https://yandex.ru/pogoda/' + inp


def get_html(url):
    session = requests.Session()
    request = session.get(url)
    return request.text


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')

    weather = soup.find('div', class_='fact')
    city = weather.find('h1').text
    temperature = weather.find('div', class_='fact__temp-wrap').find('span', class_='temp__value').text
    temp_unit = weather.find('div', class_='fact__temp-wrap').find('span', class_='temp__unit').text
    time = weather.find('div', class_='fact__time-yesterday-wrap').find('time').text
    feeling = weather.find('div', class_='link__feelings').find('div', class_='link__condition').text

    print(city + ':\n' + time + temperature + temp_unit + ' ' + feeling)


def main():
    get_data(get_html(URL))


if __name__ == '__main__':
    main()
