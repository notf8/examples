- Установить виртуальное окружение: python -m venv venv
- Запустить окружение: venv\scripts\activate
- Установить библиотеку реквестс: pip install requests
- Проверить что установлено в окружении: pip freeze
- Установить Flask: pip install flask
- Перейти в папку с приложением и выполнить ряд команд:
    1) setx FLASK_APP "app.py"
    2) setx FLASK_DEBUG 1
    3) python -m flask run --port=5555
После можно переходить по ссылке: http://127.0.0.1:5555/test
========================================================================================================================

Разбираемся, как это работает:
 - app=Flask(__name__) # подключаем к приложению flask
 - @app.route('/test') # это эндпоинт(находится в файле app.py), в аргументе функции как раз находится адрес страницы
 - def test_function(): # Как раз возвражает страницу по указанному эндпоинту
    now = datetime.datetime.now().utcnow()
    return f'Это тестовая страничка, ответ сгенерирован в {now}'
========================================================================================================================

 - Коды ответов - https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
========================================================================================================================

__________________________________________Полезные функции______________________________________________________________

Точное время через час:
# import datetime
#
# def time_future():
#     now = datetime.datetime.now()
#     future = datetime.timedelta(hours=+1)
#     current_time_after_hour = now + future
#     return f'«Точное время через час будет {current_time_after_hour.__format__("%H:%M:%S")}»'

Поиск и сбор целых слов в текством файле (без знаков припинания и пробелов, нужно вбить путь к файлу):
# import re
# import os
#
# def get_word():
#     data = []
#     base_dir = os.path.dirname(os.path.abspath(__file__))
#     book_file = os.path.join(base_dir, 'war_and_peace.txt')
#     word = re.compile(r'\w*[^.,()!:;"\d\s\-]')
#     with open(book_file, 'r', encoding='utf-8') as file:
#         for i in file:
#             result = re.findall(word, i.strip())
#             data.extend(result)
#     return data

Возврат элементов списка через запятую в виде строки (без скобок [])
# def cars():
#     car_list = ['Chevrolet', 'Renault', 'Ford', 'Lada']
#     return f'Список машин: {", ".join(map(str,[x for x in car_list]))}'