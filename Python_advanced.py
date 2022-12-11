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