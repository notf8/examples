HTML  - язык гипертекстовой разметки (hyper text markup languish)
CSS - технология стилей в браузерах
Java Script - нужен для обеспечения взаимодействия сайта с пользователем

- $0 - Специальная переменная в консоли, позволяет получить доступ к элемнету сайта

VS Code (горячие клавиши)
Ctrl + F - Вызвать поиск
Ctrl + / - Зкомментировать код
Ctrl + G - Перейти к строке № ...
Alt + ↑ / ↓ - Поменять строки местами
Shift+Alt + ↓ / ↑ - Дублировать строку (перед этим поставить курсор на троку, которую нужно дублировать)
Shift + Alt + F - Отформатировать листинг (сделать формат соответсвующий моему код-стайлу)
Ctrl + Alt + ↑ / ↓ - Мультикурсорность (или Зажмите Alt и кликайте левой кнопкой мышки там, куда нужно добавить курсор
    Выделите несколько строк, зажав среднюю кнопку мыши. В каждой из выделенных строк появится по курсору)
Ctrl + D - Множественное редактирование (перед этим мышкой выделить элементы, которые нужно редактировать)
Автосокращения  - ввести пару символов и дождаться предложения от VS Code
Ctrl + ` - Вызов терминала
Alt + Z - Перенос строк (если не помещается строка в окне, включение/отключение)
Ctrl + Shift + P - Окно ввода команд
'Live server' - полезный плагин для просмотра изменений кода он-лайн(прямо на сайте)
========================================================================================================================

Элементы разметки:
 - lorem - команда для быстрого наполнения текстом
 - <p></p> - Параграф, добавляет пустые строки после строки с текстом
    <p align="right"> </p> - Атрибут, выравнивание по правому краю (это устаревший атрибут, редактор об этом скажет)
 - <!doctype HTML> - Обязательный тег, говорит о том, что используется версия файла HTML 5 (не имеет закрывабщегося тега)
 - <html></html> - Основной тег, весь контент сайта раполагается внутри него! (кроме тэга <!doctype HTML>)
 - <head></head> - "Голова", внутри находятся мета-информация, description, title
 - <body></body> - Именно тут располагается весь контент, который видит пользователь

Заголовки:
<h1>Заголовок страницы</h1> - На каждой странице должен быть только один!
<h2>Заголовок страницы</h2> - Хорошо подходит для названия раздела и т.д. (причем визуально, все заголовки могут быть похожи, но для посиковых ситсем они соершенно разные)
<h3>Заголовок страницы</h3>
<h4>Заголовок страницы</h4>
<h5>Заголовок страницы</h5>
<h6>Заголовок страницы</h6>

Начертание текста (есть не только визуальная ценность тега):
<b>Просто полужирное начертание текста</b> (просто выделяет текст жирным, не имеет веса для поисковых систем)
<br> - Переход на новую строку
<strong>Выделение полужирным важного содержимого</strong> (этот тег важнее для поиска, им выделяют что-то особое)
<br> - Переход на новую строку
<i>Просто курсивный текст</i> (исключительно декоративный характер)
<br> - Переход на новую строку
<em>Особый акцент на текст, меняющий смысл предложения</em> (имеет такой же вес, как и тег strong, например в голосовых читалках, меняется интонация голоса)

Цитаты:
<q>Какая-то цитата</q> (Самая простая цитата, если не нужно указывать автора)
<p>
  <q>Шутка Петросяна</q> (Важно! Тег сам предоставляет кавычки, и если они есть в тексте изначально, могут получится двойные кавычки)
  <cite>Петросян</cite> (в этом теге указываем автора ,если он известен)
</p>

<!-- Можно использовать просто цитату, если неизвестен автор или ссылка на нее -->
<!-- Однако, если автор известен - используйте тег <cite> для его обозначения -->
<!-- Существует также тег blockqoute для более сложных, многострочных цитат, который мы изучим позже -->

Блочные и строчные тэги:
<h1>Блочный тег</h1> - Занимет все доступное ему пространство
<a href="#">Строчный тег</a> Занимает не всю доступную ширину, может соседствовать с тегом 'b', отлино идут друг за другом, посмле них нет новой строки
<b>Строчный тег 2</b>

Ссылки (для автовставки тега, прото печатаем арглийкую 'a' и далее табом выбираем предложенный варинат )
 - <a href="">Яндекс</a> - Между открытым и закрытым тегом находится текст(визуальная часть) ссылки

Закомментировать текст в VScode:
 <!--Как выглядит наш сайт кодстайла--> В отличии от питона, здесь такой тег <!----> (между двумя дефисами вставляем то, что хотим закоментить)
========================================================================================================================

Изображения в HTML:
<img src="https://avatars.mds.yandex.net/get-zen_doc/1587994/pub_5d9727deaad43600addf4098_5d972c8b3f548700aead6cfc/scale_1200" alt="Вид на Санкт-Петербург">
<!-- img - непарный тег, которому не нужно писать закрывающий -->
<!-- сам по себе тег img не работает - нужно обязательно указывать атрибут src, с передачей пути до картинки -->
<!-- атрибут width="600" height="100" - указывает ширину и высоту картинки-->  Как правило атрибуты ширины и высоты прописываются  в CSS
<!-- атрибут alt - обязательный. В нем нужно указывать то, что изображено на картинке --> Если вдруг не загрузится картинка, можно будет увидеть ее иконку и название
<!-- можно использовать атрибуты width и height для задания размеров изображению (однако, рекомендуется CSS) -->


Группировка контента:
<figure>
  <img src="https://avatars.mds.yandex.net/get-zen_doc/1587994/pub_5d9727deaad43600addf4098_5d972c8b3f548700aead6cfc/scale_1200" alt="Вид на Санкт-Петербург">
  <figcaption>Вид на Санкт-Петербург</figcaption>
</figure>
<!-- figure - группирующий тег -->
<!-- figcaption - описание контента, необязательный тег --> Это как правило текстовая инфа, которая находится под картинкой
========================================================================================================================

Ссылки и кнопки:
<a href="#">Текст ссылки</a> Используется для перехода к другому разделу/странице/сайту/части документа
<!-- href - атрибут, в который записывается адрес, куда мы перейдем по клику -->
    <!-- при написании адреса в href нужно использовать абсолютные пути: https://yandex.ru/, а не yandex.ru -->
<a href="#" target="_blank">Открыть в новой вкладке</a>
    <!-- при использовании ссылок на внешние ресурсы обычно используют открытие в новой вкладке браузера. Это делает атрибут target -->
<a href="document.docx" download>Скачать документ</a> - Download - булевый атребут, достаточно просто написать его имя
    <!-- если передать в href путь до документа, а также добавить атрибут download, ссылка сможет скачать документ -->

<a href="#paragraph">Текст ссылки</a> - Якорная ссылка. "#" Это id со значением параграфа (ведет на определенное местов тексте)
<p id="paragraph" style="margin-top: 300px;">some text</p>
<!--
ссылка может использоваться в рамках одной страницы, чтобы переходить по так называемым "якорям" - разделам сайта.
Для этого нужно задать у раздела атрибут id, а у ссылки передать значение этого атрибута с решеткой
-->

Кнопки:
<button></button> - Используются, когда по клику на кнопку, нужно выполнить какое-либо действие
========================================================================================================================

Текги для списков:
<ul>  - Не нумерованый список
  <li>some text</li>
  <li>some text</li>
  <li>some text</li>
</ul>

<ol> - Нумерованый список
  <li>some text</li>
  <li>some text</li>
  <li>some text</li>
</ol>

<!-- В HTML, как и в любом редакторе текста, два вида списков - маркированный и нумерованный -->
<!-- Используйте ul для маркированный и ol для нумерованных списков -->
<!--
Внутри тега ol и ul могут быть только теги li напрямую.
Вкладывать любые теги в li можно, но в ol и ul - только li
 -->
<!-- списки могут быть использованы не только для текста, но и для целых массивов данных, которые похожи между собой -->
<ol start="3"> - вы можете менять начало нумерации списка с помощью атрибута start
  <li>some text</li>
  <li>some text</li>
  <li>some text</li>
</ol>
========================================================================================================================

Тэги таблиц:
<table border="1" cellspacing="0" cellpadding="5">  - table говорит, что это таблица, cellspacing - расстояние между ячеками, cellpadding расстояние от содержмого ячейки до ее границы
  <caption>Заголовок таблицы</caption> # Заголовок никогда не принадлежит ни <th>, ни <td>, ни <tf>
  <tr>   # Это TableRow - т.е. строка таблицы
    <td>Ячейка</td>  # Ячейки таблицы. Ячейки таблицы не могут быть написаны без строк, поэтому td всегда должны быть внутри tr
    <td>Ячейка</td>
    <td>Ячейка</td>
    <td>Ячейка</td>
  </tr>
  <tr>
    <td>Ячейка</td>
    <td>Ячейка</td>
    <td>Ячейка</td>
    <td>Ячейка</td>
  </tr>
</table>
тег caption - это заголовок для таблицы. Как видите, он не оборачивается границей, чтобы выглядеть именно как отдельный заголовок.
При построении таблиц очень важно соблюдать количество ячеек внутри строк. Если на первой строке было 4 ячейки, значит и на второй должно быть четыре.
Исключение есть, оно будет на другом примере.

Важно!!! ЧТо бы вставить сразу несколько tr, td для этоко можно прям в VScode написать (tr>td*3)*5 и дождавшись подсветки, просто нажать TAB
Важно!!! Потом выделив только один закрываюшися тэг мышкой, зажимаем CTRL + D и выделяем все остальные, что бы развернуть все разом

<table border="1" cellspacing="0" cellpadding="3">
  <caption>Размер заработной платы учителя</caption>
  <thead>  # Это верхний блок таблицы, используется для заголовков
    <tr>  # Новая строка
      <th rowspan="2">Регион</th> # rowspan объединяет строки, при использовании, строка находящаясся по объединяемой сдвинется на один столбец вправо (т.к. таблицы выравниваются всегда по левому краю)
      <th colspan="3">Средняя зарплата</th>
    </tr>
    <tr>
      <th>По экономике региона</th> # Сец ячейка, для использования внутри заголовка, жирный шрифт по умолчанию
      <th>Учителей, сентябрь</th>
      <th>Учителей, июль</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Волгоградская область</td>
      <td>19,0</td>
      <td>16,8</td>
      <td>17,2</td>
    </tr>
    <tr>
      <td>Краснодарский край</td>
      <td>16,5</td>
      <td>18,3</td>
      <td>21,4</td>
    </tr>
  </tbody>
</table>

Применение colspan (используется, если нужно объеденить несколько ячеек в одну)
<table border="1" cellspacing="0" cellpadding="3">
  <caption>Таблица продаж</caption>
  <thead>
    <tr>
      <th>День</th>
      <th>Наименование</th>
      <th>Фирма</th>
      <th>Количество</th>
      <th>Цена</th>
      <th>Общая сумма</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>Пылесос</td>
      <td>Bosch</td>
      <td>3</td>
      <td>1 200</td>
      <td>3 600</td>
    </tr>
    <tr>
      <td>2</td>
      <td>Телевизор</td>
      <td>LG</td>
      <td>5</td>
      <td>1 400</td>
      <td>7 000</td>
    </tr>
    <tr>
      <td>3</td>
      <td>Ноутбук</td>
      <td>Samsung</td>
      <td>12</td>
      <td>5 400</td>
      <td>64 800</td>
    </tr>
  </tbody>
  <tfoot>
    <tr>
      <td>Итого:</td>
      <td colspan="5">75 400</td>  # После равенства в двойных кавычках, указываем, сколько ячеек нужно объеденить в одну
    </tr>
  </tfoot> # Используется как итоговая строка в конце таблицы
</table>
<!-- caption стоит "особняком", и не входит ни в одну из частей таблицы -->
<!-- thead - заголовочная часть таблицы. Как правило, содержит в себе теги th (но обязательно в строке) -->
<!-- tbody - основное содержимое таблицы -->
<!-- tfoot - подвал таблицы. Как правило, это блоки типа "итого" или пр. -->
<!-- для исправления ошибки ячеек добавьте атрибут colspan="5" для ячейки "итого" -->
========================================================================================================================

Служебные тэги:
<!DOCTYPE html>
<html lang="ru"> # Тут код языка страницы, что бы браузер мог предложить перевод
<head>
  <meta charset="UTF-8"> # Мета передает в себе настройки страницы (charset=например кодировка)
  <meta name="viewport" content="width=device-width, initial-scale=1"> # Тут описывается поведение страницы внутри сайта
    # viewport - видимая область контента, width=device-width - ширина равна ширине экрана девайса, initial-scale = мастштаб (1 = 100%)
  <title>Заголовок</title>  # Тут понятно, имя страницы (оно же сохраняется в закладках, оно же подсвечивается при шеринге, тип H1
</head>
<body>
  Контент страницы
  <p lang="en">some words in english</p>
</body>
</html>
========================================================================================================================

Прочие теги:
<br>  # принудительный переход на новую строку (лучше не использовать в адаптивной версте. ТОлько если уверены. Например применять стоит в таблице)
<pre>   текст</pre> # Сохраняет исходное форматирование (например если нужно оставить три пробела в начале)
<p>H<sub>2</sub>O</p> # Опускает символы ниже линии текста (baseline), например формула H2O
<p>m<sup>3</sup></p> # Наоборот подымает символы выше лини текста, например что бы написать кубические метры (м3)
<u>подчеркнутый текст</u> # Нижнее подчеркивание (underline)
<code>let a = 5;</code> # Для того, что бы можно было написать пример кода.
<s>зачеркнутый текст</s> # Собственно, зачеркнутый текст
The <abbr title="World Health Organization">WHO</abbr> was founded in 1948 # Для короткого сокращения (аббревиатура)
<p>Мой любимый цвет <del>Синий</del> <ins>Красного</ins>!</p> # Эти теги как будто перечеркивают слова, которые мы передумали писать и добавили исправления
<p>
To learn AJAX, you must be familiar with the XML<wbr>Http<wbr>Request Object. # Показывает предпочтительные точки для переноса слова
</p>
========================================================================================================================

Валидность HTML кода:
Самый авторитетный ресурс для валидации: https://validator.w3.org/
 - &lt; и &gt; - Что бы указать угловые скобки в тексте (иначе сайт будет интерпретироваеть его как тэг). Левая и правая скобки
========================================================================================================================

Плагины для работы:
 - https://code.visualstudio.com/docs/editor/emmet
 - Привет эммет (https://habr.com/ru/post/175747/)
 - https://marketplace.visualstudio.com/items?itemName=mkaufman.HTMLHint (HTML hint) Лучше сразу установить именно его
 - https://marketplace.visualstudio.com/items?itemName=EditorConfig.EditorConfig (Editorconfid Для VScode)
 - Эммет:
    - Если напечатать ! и нажатьTAB, эммет развернет шаблон html страницы целиком!
    - tr>td*3 - будет напечатана одна строка с требя ячейками в таблце (и так люьое выражение, которое нам требуется)
    - #class.class - Напечатать тэг DIV. # Это селектор CSS ID, далее ID потом "." и название класса
    - span#class.class - Тогда напечатается тэг span
 - Editorconfig^:
    - Перед началом работы сохраняем файл '.editorconfig' - вначале названия точка
    - [*] - Означает, что настройки общие, для любого проекта
========================================================================================================================

Кодстайл:
https://codeguide.maxgraph.ru/ - с оглавлением
https://yoksel.github.io/easy-markup/ - простые правила разметки
CTRL + SHIFT + P - Отформатировать весь документ (в поиске написть: format document)
========================================================================================================================

Как находить файлы в проекте:
 - './' - '.' - означает текущую папку. './'  - перейти из текущей папки куда либо
 - '/' - Слэш вначале означает корневую деррикторию
 -Важно! При запуске проекта на веб-сервере, корневой директорией для него является сама папка проекта, при запуске на компе,
    корневой директорией является диск "С"
    Если же по каки-либо причинам файл .html лежит не в корневой директории, то нужно использовать относительные пути
    Т.е. без "/" вначале пути (просто пишем имя папки)
    Если же нет задачи открывать .html по клику мышки, то всегда пишут абсолютный путь для вебсервера с указанием корневой дирректории - ставят "/" в начале пути
 - '../' - Означает на одну деррикторию выше
========================================================================================================================

CSS - Каскадные таблицы стилей (Cascade Style Sheet)

Атрибут style:

Самый простой способ - писать стиль в каждой строке, но это проблнмно, так как код будет громадный, проще подключить CSS
И тогда стили будут применяться ко всем указанным элементам
 - <h1 style="color: red;">Заголовок страницы</h1> # синтаксис стиля такой же как у словарей {ключ: значение; ключ: значение}

 - Подключение стилей:
Для подключения стилей используется тег <link rel="stylesheet" href="style.css"> # Где href= это адрес папки с таблицей стилей
Важно! Можно подключать в одном документе разные таблицы стилей (что не есть хорошо, но можно), просто добавив теги с именами
подключаемых таблиц. Они будут загружаться в той последовательности, в которой мы укажем. Самый важный приоритет будет у
последнего подключенного файла стилей

 - Сброс стилей:
Для сброса стилей используется тег <link rel="stylesheet" href="reset.css" или <link rel="stylesheet" href="normalize.css"
Важно!!! Тег сброса стилей никогда не указывать последжним, иначе у него будет самый высокий приоритет
Что бы скрыть какой либо элемнет в стилях, просто указываем параметр display: none
 - Иногда стили пишу сразу в блоке head (так делают, если используется минимум стилей, и они однородны)
    <head>
        <style>
            @import 'css/style.css'; # Можно импортировать стиль пряма в теге <style>. Импорт всегда указывается в начале файл! Но это не самое лучшее решение
            body {
                background: red;
                }
        </style>
    </head>
Итого:
 - Для точечного стиля  - Можно использовать атребут style внутри тега (<h1 style="color: red;">Заголовок страницы</h1>)
 - Если стилей будет не много и не нужно делать лишний запрос к серверу - Используем тег <style> в секции Head
 - Если же нужно использовать много разных стилей - прописываем их в отдельнос файле и подключаем (<link rel="stylesheet" href="style.css">) так же в секции Head
========================================================================================================================

Селекторы CSS (а так же их синтаксис):
 - Почитать про базовые селекторы: https://webref.ru/course/css-tutorial/selector
 - Почитать про вес селекттора: http://css.yoksel.ru/specifity/
 -

1) Название тега (h1, body и т.д.). Что бы указать стили сразу для нескольких тегов ,просто перечислем их через запятую
    h1, h2 {
      font-size: 30px;
      font-style: italic;
    }
2) указать * - это как и в питоне означает: абсолютно все, что есть в файле
    * {
      color: red;
    }
3) Использовать классы - для этого нужному элементу присваиваем класс: <h1 class="heading">Some text</h1>
И далее образщаемся к классу в файле css как объекту класса, те через точку (.heading)
Это лучший способ стилизации
    .heading {
      color: red;
    }
4) Обращение по ID. ID и класс никак не пересекаются, потому могут присутсвовать оба в атрибутах
Для обращения к атребуту ID используется #
    #heading {
      color: blue;
    }

Вес селекторов:
 - Сначала сверяются уровни вложенности. Чем больше(глубже) вложенность, тем больше вес
 - Если уровень одинаковый, ID ('#') иемеет больший вес чем Класс ('.')
 - Если все прочие равны, то вес больше у последнего (по очереди) элемента
 - Атрибут style внутри тега (<h1 style="color: red;">Заголовок страницы</h1>) - Имеет больший вес, чем селектор по тегу(h1)
========================================================================================================================

Вложенность селекторов (если используем, то элементы в ложенности пишутся через пробеле, НЕ запятую):
 - Каскадная вложенность. Ее лучше не использовать, без крайней необходимости. Очень хрупкая система (изменив немного файл HTMS, каскад может сломаться целиком)
    .parent div {                 - Этот селектор для все DIVов,внутри тега, который имеет класс 'parent'
      width: 100px;
      height: 100px;
      margin: 10px;
      background-color: red;

Решения для упращения:
 - Стараться использовать классы (не связываться с весами и каскадами)
 - Если нельзя менять код CSS - Для это просто используем атрибут style="" внутри тега
 - Если нельзя менять структуру файл HTML - в файлсе CSS, напротив нужного параметра просто добавляем: !important
    .heading {
      color: red !important;
 - Если есть !important в файле CSS но его менять нельзя - Просто добавить !important в аргумент тэга <h1 style="color: red !important;">Заголовок страницы</h1>
========================================================================================================================

Единицы измерения CSS:
 - Базовые: https://webref.ru/course/css-basics/size
 - Дополнительные: https://www.w3.org/Style/Examples/007/units.ru.html
 - Справочник стилей: https://webref.ru/css
 - Справочник стилей (2): https://html5book.ru/css-css3/
 - Пиксели, как правило основная единица измерения. Но с ними адаптивность не работает

Абсолютные величины:
Для примера:
    .parent {
      max-width: 1000px; # С помощью этого параметра ограничиваем размер контента сайта (указываем максимальный возможный размер)
      margin: 0 auto;  # Если указывать в %, то на большом экране получим слишком большой контейнер
      display: flex;
    }

    .child {
      min-height: 200px; # Аналогичное решение, с мин размером, что бы точно соответствовать дизайну
      width: 33.33%;
      background-color: red;
      border: 2px solid #000;  Бордеры вообще всегда указывают в пикселях
    }

 - Относительные единицы измерения:
    Если используем проценты, то это как правило процент от родительского элемента
    EM и REM. EM - зависят от размера шрифта родительского элемнета. REM - зависят от размера базового шрифта сайта
        Для примера:
            .block {
              font-size: 50px;
            }
            .block p {
              font-size: 1em;
              margin-bottom: 1em; # Отступ между параграфами в таком случае соответствует размеру шрифта параграфа
            }
        Или
            html {
              font-size: 10px;
            }

            .block p {
              font-size: 5rem; # Подходит для того, что бы увеличивать размер шрифта в каком-то одном месте сайта
            }
========================================================================================================================

Свойства Display: С помощью Display мы управляем поведением элемнтов на странице. Их видимостью и т.д.
 - Справочник 1 - https://webref.ru/css/display
 - Справочник 2 - https://www.w3schools.com/cssref/pr_class_display.php
 - Справочник 3 - https://html5book.ru/svoystvo-display/
 - Блочный ии строчный элемент:
    Блочный  - растягивается на всю дсотупную ширину экрана
    Строчный - стремится занять как можно меньше доступного пространства (отступы между элементами не настраиваются)
    Для примера:
        div, span {
          background-color: aqua;
        }

        div {
          display: inline; # С помощью display делаем div строчным
        }

        span {
          display: block;  # С помощью display делаем span блочным
        }
        Так же бывает атрибут display: none;  # Так мы делаем элемент невидимым и убираем его из потока запросов к стилям

    Объединение inline и block:
        .block {
          margin-bottom: 30px;
        }

        .inline {
          margin-bottom: 30px;
        }

        .inline-block {
          display: inline-block; # В отличии от чистого Block, имеет настраиваемые margin (т.е. обладает настраиваемыми элементами inline)
          margin-bottom: 30px;
        }

Практика:
    * {                         # это значит что бордер боксы одинаковы для всего сайта
      box-sizing: border-box;
    }

    .block {
      background-color: aqua;  # Синтаксис задний фон
      display: block;          # Переопределенное свойство означает, что за эти элементом (справа) уже ничего не станет и будет перенос строки
      width: 300px;
    }
========================================================================================================================

Размеры, отступы, границы
 - /*...*/ - синтаксис комментариев в CSS
 - margin - внешний отступ элементов (не работает в инлайн)? для отделения разных элементов (блоков) друг от друга
    Важно!!! margin left и right работают в инлайн элементах!!
 Маргины top и bottom в блочных элементах не складываютс!!! Будет применен наибольший маргин из двух блоков!
    - короткая форма записи 1 - margin: 10px 20px 30px 40px; (1я цифра=верх, 2я=право, 3я=низ, 4я=лево (по часовой стрелке))
    - короткая форма записи 2 - margin: 0 30px; (1я цифра=вертикальные отступы, 2я цифра=горизонтальные отступы)
    - короткая форма записи 3 - margin: 10px; (отступы со всех сторон)
    - короткая форма записи 4 - margin: 20x 0px 30px; (1я цифра=верхний отступ, 2я цифра=левый и правый отсупы, 3я цифра=нижний отступ)
    Точечные отсутпы:
    - верхний отсуп - margin top: 10px
    - Правый отступ - margin right: 10px
    - Нижний отсутп - margin bottom: 10px
    - Левый оступ - margin left: 10px
 - padding - внутренний отступ (работает в инлайн), для отделения контента внутри одного элемента
    - Синтаксис такой же как и margin
 - border - напрямую влияет на отступы (суммируется с margin). У них есть три аргумента
    - border-width: 2px; - ширина бордера (px)
    - border-style: solid; - стиль бордера ('solid'-цельный, 'dashed'-пунктирный, 'doted'-точечный)
    - border-color: red; - цвет бордера('red')
    - коротакая форма записи - border: 10px solid #ff0 (все арогументы указываются через пробел)
    - Так же бывает точечная настройка (border-top, border-right, border-bottom, border-left)
- Высота и ширина блока (div) - Нужны для визуального выделения блока.
    - border-width и border-height не работают со строчными элементами!
    - Важно!!! лучше не исполльзовать абсолютную величину (px), иначе может быть слишком много текста, и тогда блоки залезут друг на друга
    В таком случае лучше использовать min-width: 350px; и max-width: 1000px (минимальные и максимальные значения)
    Как правило, для блоков с текстом max-higth не используется, т.к. его может быть чудовищно много
 - outline - почти то же самое, но в отличии от бордера, вообще никак не задействован в размерах
========================================================================================================================

Блочная модель.
 - Блочная модель1 - https://webref.ru/layout/learn-html-css/box-model
 - Блочная модель2 - https://developer.mozilla.org/ru/docs/Web/CSS/CSS_Box_Model/Introduction_to_the_CSS_box_model
 - Блочная модель3 - https://html5book.ru/css-blochnaya-model/
    .example {
      background-color: navy;
      width: 400px;
      padding: 20px;
      border: 6px solid gray;
      border-radius: 20px             # Делает границы элемента закругленными (только визуально, на сайте)
      box-sizing: border-box; # (по умолчанию значение 'content-box', При таком формате внутренние отступы, увеличивают
      #размер элемента. Общепринято использовать 'border-box' - внутренние отступы съедают размеры элемента изнутри,
      # т.е. не зависят от paddingа. Однако все старые сайты используют 'content-box' и если по умолчаню в браузере,box-sizing
      # изменить на 'border-box', то сайты поломаются, потому разарабы сами переназначают значения в версте новых сайтов)
      # border-box проще использовать, что бы не ломать голову и не просчитывать размеры каждого блока, используя любые
      # paddingи, что бы они использовали внутренний размер блока

Практика:
    * {
      box-sizing: border-box;
    }

    .parent {
      width: 1000px;
      margin: 0 auto;
    }

    .element {
      border: 1px solid #000;
      display: inline-block;
      width: 325px;
    }
Важно! Что бы расположить стык-в-стык элементы со свойством display: inline-block; (что бы браузер не вставлял невидимый невидимый символ)
между ними, нужно: нужно сделать font-size: 0; у родительского элемента, и вернуть убраный font-size (например 14px) дочерним элементам

 - Что бы выбрать все селекторы, кроме последнего дочернего есть запись: .element: not(:last-child)
 - Что бы выбрать каждый третий селектор, есть запись: .element: nth-child(3n) - буква 'n' говорит что это иттеративный элемент
 - Что бы отцентрировать запись в колонке есть запись: .element: vertical-align: midle (или right или left или bottom или top)
========================================================================================================================

Организация отступов в верстке:
 - Почитать - https://skillbox.ru/media/code/pravila_organizatsii_otstupov_kak_sdelat_vyerstku_gibkoy_i_ne_dopustit_oshibok/
 - Что бы избежать неожиданных последствий при смене контента, принято писать отсутпы в тилях так (при условии, что вся медиа в классе content)
    Правильное решение, делать отступы только справа и снизу
    .content {
    padding: 2rem 1rem; #Отступы по вертикали и по горизонтали
    }
    h2 {
    margin: 0 0 1em # Отступы для загловков, 1em-размерность равная размеру шрифта
    }
    ul {
    display: inline-block; # Если списков несколько, лучше расположить на одном уровне (в линию)
    padding-left: 1em; # Убираем лишний отсутп между списками, оступом служит размер маркера списка. Хорошая практика-удалять отступы только между соседними элементами в одном потоке (блоке)
    margin: 0 2em 1em # Для списка делаем то же самое. Сверху паразитный отступ не нужен, так как если поставить картинку сверху, выйдет УГ, 2em-что бы списки не слипались
    }
    ul:last-child { # Таким силектором выбираем последний элемент
    margin-right: 0; # Убираем правый отступ (что бы во время адаптивного отображения, список слишком рано не переходил на новую строку)
    margin-bottom: 0; # Убираем нижний отступ (что бы во время адаптивного отображения, список слишком рано не переходил на новую строку)
    }
 - По правилам организации отступов - margin-top: Зпрещен!!!
 - Отступы, как правила, задаются от предидущего элемента к следующему
 - Отступы между секциями, должны регулироваться исключительно стилями самих секций
 - Логика должна читаться: Если элементы inline-block то убираем правый отступ у последнего элемента. Если елемент
    display-block: то убираем нижний отсутп у последнегшо элемента
 - Пример грамотного сброса:
    html {
        box-sizing: border-box;
    }
    *,
    *::before,
    *::after {
        box-sizing: inherit;
    }
    a {
        color: inherit;
        text-decoration: none;
    }
    img {
        max-width: 100%;
    }
    body {
        font-family: 'font', sans-serif;
    }
