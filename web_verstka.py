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
