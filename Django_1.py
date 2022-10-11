Фрэймворк - это набор готовых библиотек и готовых модулей, типа панель администратора, набор регистрации пользователей и т.д.
Django - это готовый фреймворк, с огромным набором библиотек

 - HTTP запрос бывает 2-х видов: Get и Post. В себе они содержат голову (Head) и тело (Body)
 - Для получения инфы с сервера используется Get запрос
 - Для обновления инфы на сервере используется Post запрос
 - Host - Указывет, к какому веб приложению нужно обратится на сервере
 - User-agent - говорит с какого браузера и устройства обращается клиент
 - Accept - говорит о том, какой язык может понять клиент
========================================================================================================================

Простейшее серверное приложение:
## (Запустить сервер из командной строки, находясь в директории с файлом: python simple_http_server.py)
from http.server import HTTPServer, BaseHTTPRequestHandler

APP_HOST = 'Localhost'  # Указываем на каком хосту будет запускаться наш веб-сервер (в это случае, это хост нашей машины = 127.001)
APP_PORT = 8000  # Указываем на каком порту сервер будет работать

class SimpleGetHandler(BaseHTTPRequestHandler):  # Класс - элементарный обработчик get запросов
    def _set_handlers(self):
        self.send_response(200)  # Указываем, какие заголовки должны быть в нашем запросе
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()

    def _html(self, message):
        content = (f"<html>"
                   f"<body>"
                   f"<h1>{message}</h1>"  # Здесь передаем наш месадж в html код
                   f"</body>"
                   f"/html")
        return content.encode("utf8")  # Кодируем контент в utf8

    def do_GET(self):
        self._set_handlers()
        message = "Привет, мир!"  # Создаем нужный нам месадж
        self.wfile.write(self._html(message))  # Отправляем наш ответ(ответ сервера) клиенту

def run_server(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):  # Инициализируем запуск сервера
    server_address = (APP_HOST, APP_PORT)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()  # Указываем, что сервер необходимо хранить вечно (пока не упадет в ошибку или мы его не выключим)

if __name__ == "__main__":
    run_server(handler_class=SimpleGetHandler)