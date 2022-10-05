Базы данных бывают реляционными и не реляционными
Реляционные (SQL базы - Stucture Query Language = Язык структурированых запросов)- в базе данные связаны между собой
Данные не дублируются, легко вносить измененеия, легко использовать
- Строки - называются записями
- Столбцы - называются полями
Самые популярные базы: MySQL и PostgreSQL MSSQL(майкросовтовская), Oracle(в корпорациях и на java языке), SQLite(мобильная)
========================================================================================================================
Не реляционные = NoSQL. Формат хранения данных:
ключ:значение - (используют для кэширования) Redis, AmazonDynamo
JSON - объект, состоящие из ключей и значений. Ключ - это всегда str. Значение: Any. Они как правило документоориентированы
(MongoDB, CouchDB, Elasticsearch)
========================================================================================================================
Типы полей в реляционных базах в MySQL:
Числовые:
- TINYINT - для целых чисел от -128 до 127 (всего 256 значений)
- INT - так же для целочисленных данных от - 2 млрд до 2 с копейкаи млрд
- BigINT - от -2**63 до 2**63-1
- FLOAT - c плавающей точкой от 1.7 * 10**-38 до 3.4 * 10**38
- DOUBLE - с плавающей точкой в два раза большей точности (чем float) от 2.2 * 10**-308 до 1.8 * 10**308
Дата и время:
- datetime - сохраняется дата и время От 1000 до 9999 (YYYY-MM-DD HH:MM:SS - именно такой формат в базе MySQL)
- date - хранится только дата (YYYY-MM-DD) От 1000 до 9999
- TIMESTAMP - Хранятся числа, отражающие количество секунд (YYYY-MM-DD HH:MM:SS), прошедших с 01.01.1970 Срок с 1970 по 19.01.2038
Строковые:
- CHAR(N) - в скобках указываем длину строки. Макс - 255. Строки будут той длины, что указали (не больше не меньше)
- VARCHAR(N) - в скобках указываем длину Макс - 65535 после 5й версии MySQL и 255 до 5й. Длина строк будет от 0 до указанной
- TUNYTEXT - Макс - 255
- TEXT - Макс - 65565
- MEDIUMTEXT - 16 mb данных
- LONGTEXT - 4 Gb данных (интересно: Геном человека в тестовом виде занимает чуть более 3х Gb)
- ENUM - Можно сохранять набор значений (YES и NO)
- Пространственные - хранят все что связано с пространством
- JSON-данные - можно хранить JSON объекты
========================================================================================================================
Специальное значение NULL - может стоять в поле любого типа, если поле не помечено как 'NOT NULL'
========================================================================================================================
Типы связей в реляционных базах
- Один ко многим (one-to-many)- Например база книг. Один автор может быть связан со многими книгами. Или таблица ссылается на саму себя -
Это означает родительское и дочерней отношение (NULL - означает корневой родитель)
- Один к одному - две таблицы (one-to-one): Страны и Столицы, ссылаются по 1 столбцу (по ID), такое поле помечают как UNIQ
- Многие ко многим (many-to-many)- одна запись из первой таблицы может ссылаться на несколько из второй и наоборот
========================================================================================================================
Дамп базы - типа вся инфа по базе, выгруженная в файл, из которго можно всю базу восстановить
========================================================================================================================
результатом выполнения SELECT-запросов всегда является таблица. Такая таблица может состоять как из нескольких полей и
записей, так и всего из одной записи в одном поле, как в последнем примере. Таблица в результате выполнения запроса может
быть и пустой, если условиям в SELECT-запросе не соответствует ни одна запись.
========================================================================================================================
Типы запросов:
1) Запросы на получение данных - Это всегда запросы с оператором SELECT, с помощью этого оператора можно получить данные
как из одной таблицы так и из нескольких. Можно получать данные по выбраным полям, фильтровать значения по разным условиям
 - Пример запроса: select * from tablename; (вместо звездочки могут быть имена полей, конец запроса всегда точка с запятой)
 - Важно, если с базой работаем через язык програмирования, и делаем только один запрос то ';' в конце запрос можно не писать
 - Имя таблицы записывают в обратные одинарные кавычки (это клавиша - тильда (ё) (что бы экранировать его от имени сервера)
 - Если нужно получить несколько полей, то просто перечисляем их имена в одинарных кавычках после оператора SELECT чероез запятую
 - При запросе полей, можно изменять название полей: SELECT `field_1` as F1 from tabelname; (или просто: SELECT field_1 F1 from tabelname)
 - Так же можно производить арифметические вычисления с полями при запросе: SELECT `name`, (`field_1` * `field_2`) `totalcoast` from tabelname;

2) Фильтрация данных, оператор WHERE:
 - Фильтрация по равенству какому то числу: SELECT `id`, `name` from `good` WHERE `count` = 0 (псле оператора WHERE пишется условие)
- Фильтрация по тексту: SELECT * from `order_status` WHERE `code` != 'NEW' (текст, как обычно оборачиваем в обычные кавычки)
    Важно! Равенство в SQL в отличии от Python, проверяется одни знаком '='
- Фильтрация по датам: SELECT `id`, `name`, `reg_time` from `user` WHERE `reg_date` >= '2019-01-01'
- Фильтрация по диапазону дат/времени: SELECT * from `user` WHERE `reg_date`>= '2019-08-01' and `reg_date`<= '2019-07-01'
    или                                SELECT * from `user` WHERE `reg_date` BETWEEN '2019-08-01' and '2019-07-01' (оператор
                                    BEETWEN позволяет установить диапазон между)
- Фильтрация по строкам с помощью масок:  SELECT * from `goods` WHERE `name` LIKE 'Чай' (Оператор LIKE позволяет добавлять
                                                                                                        в условия маски)
    Маски:
    '_' - Только один символ (любой)
    '%' - От 0 и более символов. Например: '%Чай%'- будет означать, что слово чай может встречаться в любом месте поля
- Фильтрация с масками и енсколько условий: SELECT * from `goods` WHERE `name` LIKE '%Чай%' or '% Чай %' or '% Чай' or 'Чай %'
    Важно! Пробел в масках так же используется, что бы искать слово чай в начале или конце фразы
- Операторы для работы с категориями Null: Их всего два - is Null и is not Null
    Пример: SELECT * from `user` WHERE `parent_id` is not Null;
    Важно! Обычные операции (например равенсто) не работают с Null, только два этих оператора
- Оператор IN: SELECT * from `goods` WHERE `status` IN (7, 8) - так задаем список (несколько условий для поиска, точ бы
   не писать оператор OR)
- Приоритеты опеторов: Как и в питоне(аналогично) SELECT * from `goods` WHERE `name` LIKE ('%Чай%' or '% Чай %' or '% Чай' or 'Чай %') \
                                                                                     and `parent_id` is not Null
    Таким образом, скобками мы объединяем все условие OR в одно, что бы поиск был по приоритету (у and проиоритет выше)
========================================================================================================================
Сортировка и ограничение результатов
 - Сортировка по убыванию/возрастанию: SELECT * from `good` order by `name` ASC (order by - сортировка, ASC - возрастанию
    DESC - убыввание (descending). Что бы сортировать по нескольким полям, просто указываем их через запятую после оператора
    order by: SELECT * from `good` order by `category_id` DESC, `name`  ASC- после каждого поля нужно писать тип сортировки,
    если нуэна сортировка по ворзрастанию, то ASC писать не нужно, т.к. это сортировка по умолчаню
 - Ограничение результатов запроса: SELECT * from `good` order by `price` limit 10, 20
    10 - с какого элемента выдавать результыта, 20 - сколько элементов выдавать по запросу
========================================================================================================================
Объединение таблиц (Join):

Inner Join (внутреннее объединение). При написании такого запроса, слово INNER можно не писать. При таком запросе выводятся
только те записи, данные из которых, есть в обоих таблицах (пересекающиеся данные)
 - SELECT `good_category`.name category_name, `good`.name good_name from `good` join `good_category` on `good_category`.id = `good`.category_id limit 10
    где: после SELECT пишем какие поля вывести, после FROM пишем из какой таблицы выводим поля, а после оператора
    JOIN пишем с какой таблицей надо связать поля, после оператора ON (по какому принципу), указываем как надо связать поля
    К полям обращаемся через точку после названия таблице, то есть как к методу класса
    После названия поля можем сразу переименовать его, просто добавив название сразу через пробел
    А если переименовать таблицы, то запрос получится куда короче, например:
    SELECT
        c.name category_name,
        g.name good_name
    from
        `good` g
    join `good_category` c on
        c.id = g.category_id limit 10
    Важно! Переименование происходит в операторах from и join (то есть в них оставляем настоящие названия таблиц)

Так же существуют LEFT JOIN и RIGHT JOIN. При объединении с помощью LEFT JOIN - из левой таблицы выводятся все записи,
а из правой только те, которые встречаются в левой таблице. Если для какой то записи не будет соотвтетсвия в левой таблице,
то в этом поле мы получим значение NULL. Соотвтетсвенно при объединении RIGHT JOIN все происходит с точностью до наоборот

 - Объединение нескольких таблиц в одну (с переименованием полей/таблиц) для сокращения запроса
    select
        c.name categotyName,
        g.name productName,
        o.creation_date orderDate,
        u.name userName
    from `good` g
    join good_category c on c.id = g.category_id
    join order2good o2g on o2g.good_id = g.id
    join `order` o on o.id = o2g.order_id and (здесь можно добавить нужное условие для объединения просто через AND)
        o.creation_date between '2017-08-01' and '2017-08-31'
    join `user` u on u.id = o.user_id

 - Если потребуется забрать только записи, у которых значение Null, то делается это так:
    select
        g.id,
        g.name,
        o2g.order_id
    from `good` g
    join order2good o2g on o2g.good_id = g.id
    where o2g.order_id is Null
========================================================================================================================
Фильтрация по уникальнолсти и группировка записей. Ключевое  - оператор distinct ('отличный от..', 'уникальный')
Что бы получить все статусы, в которых находятся запросы (выдать уникальные записи), можно сделать такой запрос
    SELECT distinct `status_id`
    from `order`

 - А что бы получить уникальные записи сразу по двум полям (столбцам):
    SELECT distinct
        `src_status_id`,
        `dst_status_id`
    FROM shop.order_status_change;
Важно! Если выбираем несколько уникальных записей из полей одной и той же таблицы, то для каждого поля, нужно снова делать
join той же таблицы (т.к. первый join уже забрал данные из таблицы и она как будто уже пуста), для этого просто даем имя
той же таблице, которе будет отличаться от первого
    SELECT distinct
        os1.name,
        os2.name
    FROM shop.order_status_change ch
    join `order_status` os1 on os1.id = ch.src_status_id  # Вот таблица `order_status` привязывается первый раз и получает имя os1
    join `order_status` os2 on os2.id = ch.dst_status_id  # Вот она же привязывается второй раз и получает другое имя os2

 - Группирповка по одному из полей:
    SELECT
        os1.name,
        os2.name
    FROM shop.order_status_change ch
    join `order_status` os1 on os1.id = ch.src_status_id  # Вот таблица `order_status` привязывается первый раз и получает имя os1
    join `order_status` os2 on os2.id = ch.dst_status_id
    group by ch.src_status_id

 - Группировка по по полю и подсчет сгруппированых данных
 Важно, если спользуется  и группировка и сортировка, сначала пишется GROUP BY, потом ORDER BY
    SELECT
        c.name,
        count(*) 'count' # Здесь говорим оператору count в скобочках, что считать нужно количество записей (строк) в каждой категории
    from good g
    join good_category c on c.id = g.category_id
    group by `category_id`
    order by `count` desc # Группируем по убыванию (имя поля указываем в косых `` кавычках)

 - Группировка по нескольким полям. Для этого после GROUP BY через запятую, указываем нужные поля
    SELECT
        g.name,
    from good g
    group by
        `category_id`,
        `price`
========================================================================================================================

Объединение результатов запросов, опертор UNION
Важно! Если мы объединяем несколько запросов, каждый запрос должен возвращать одинаковое количество полей (строк),
желательно, что бы это были одни и те же поля.
Что бы реализавтаь такаой запрос, сначала прокисываем каждый отдельно, проверяем, что бы он работал корректно, и потом между
ними просто вписываем оператор UNION (Важно! Поле каждого отдельного запроса в конце не ставится ';')
    SELECT o.id, o.creation_date
    FROM `order` o
    join `order_status` s on s.id = o.status_id
    where s.code in ('APPROVED_BY_STOCK', 'PACKED')
    UNION
    SELECT o.id, o.creation_date
    FROM `order` o
    join `user` u on u.id = o.user_id
    where u.reg_date between '2018-02-01' and '2018-02-28'
    UNION
    SELECT o.id, o.creation_date
    FROM `good` g
    join `order2good` o2g on o2g.`good_id` = g.`id`
    join `order` o on o.`id` = o2g.`order_id`
    where g.`name` like '%йогурт%'
========================================================================================================================

Запросы INSERT, UPDATE и DELETE.
Опертор вставки: Сначала пишем INSERT, через пробел, название таблицы `good`, через пробел открываем скобки, и в них, через
запятую вписываем поля, которые нужно вставить. (если их не укащзать, будут вставлены поля по умолчанию таблицы) Если
занчения NULL не было по умолчанию в таблице, то после вставки без указаний этих полей, значения будут в них либо пустые, либо нулевые:
Там где написы числа - будут нули. Там где строки - будут пустые строки, а там где должна быть дата - будет минимально
возможное значение даты
После идет оператор VALUES, после него открываем скобки и начинаем через запятую вносить значения полей, которых указывали в
ISERT
Важно! AUTO_INCREMENT - Это по сути ID (номер записи в таблице) Что бы его не угадывать, нужно проверять, есть ли в этом
после AUTO_INCREMENT. Если да, то поле ID и его значение можно ен указывать. Увидетьь это можно в свойствах таблицы, в пункте
"Дполнительно (extra)"
    insert into `good` (`category_id`, `name`, `count`, `price`)
    values ( 6, 'Белый чай с вишней', 50, 344)

- Множественная вставка записей  - делается через запятую в VALUES, каждая вставка в отдельных скобках
    insert into `good` (`name`, `price`)
    values ('Белый чай с вишней', 344), ('Черный чай с вишней', 300), ('Улун', 450)
========================================================================================================================

Запросы изменения записей в данных. Такие запросы делаются с оператором UPDATE. После него пишем имяч таблицы, потом оператор
SET и указываем имя поля. Если запросов несколько, то просто пишем через запятую, что изменяем
    update `good` set
        price = price + 50
    where `count` > 0 and `count` < 10
========================================================================================================================

Запросы на удаление. Пишем из какой таблицы удалить, а потом, через WHERE указываем ID записи, которую удаляем
    DELETE FROM `good`
    WHERE `ID` = 1373
    WHERE `ID` = 1373
========================================================================================================================

Выражения и функции в SQL запросах.
 - Перемножить значения полей можно так:
    select
        `name`, `price` * `count` as cost # Тут просто пишем как в питоне, какие столюцы перемножить, и присваиваем результату имя 'as cost'
    from `good`

 - Использование условных операторов: Вывести список товаров и указать напротив достаточно/не достатнчо, если количество < 100
    select
        `id`, `name`,
    if(                # Важно!!! Опертор IF так же пишется через запятую, после наименования строк после select
        `count` > 100, # В скобках сначала пишем условие, через запятую, значение если истина, через запятую, значение если ложь
        'enought',     # Важно!!! Значения, которые нужно вывести, указываем в обычных кавычках (НЕ косых!)
        'not_enought'
        ) isEnougth # И поять же, через запятую указываем имя будущего поля (столбца)
    from `good`

 - Использование функций в запросе: Бывают функции для строк (как в питоне), для даты и времени, а бывают агрегатные (типа count)
Агрегатная функция - умеет выполнять арифметические операции сразу над несколькими строками
Посчитать уникальные названия товаров в сгруппированной catrgory_id
    select
        `category_id`,
        count(distinct `name`) unic_name # Тут в с кобках каунта пишем оператор distinct, и горим ему по какому полю смотреть 'name'
    from `good`
    group by `category_id`

 - Использование условного оператора и булевого выражения. Все тот же IF. Умножить цену товара на 0.8 если его количество < 20
Так же, с помощью оператора OR или AND можно добавить условия
    select
        `id`, `name`,
        if (
        `count` < 20,
        `price` * 0.8,
        `price`
        ) `UpdatedPrice`
    from `good`

 - Использование IF с проверколй на Null. По сути то же, что и в верхнем примере, только это чисто bool проверка
    select
        `id`, `name`,
        if (
        `id` is NULL,
        'Yes',
        'No'
        ) `Root_Category`
    from `good`

 - Вложенный IF, можно использовать так же, как и в питоне, в это мпримере, вложенный IF выполняет функцию значения, при
условии False:
    select `id`, `name`, if ( `count` < 20, 'Мало', if (`count` > 500, 'Много', 'Нормально')) `Quantity_value`
    from `good`
Но лучше в таком случае использовать поератор CASE: Важно! Все условия пишутся без запятых
    select
        `id`, `name`,
        case
            when `count` < 20 then 'Мало' # Тут логика когда - тогда (when - then)
            when `count` > 500 then 'Много'
            else 'Нормально'
        end `Quantity_value`              # Оператор END закрывает оператор. В ней же можно задать имя для поля с результатами
    from `good`

========================================================================================================================

Работа со строками.
Определение длинны строк (символов), с последующей обрезкой
 - substring (str, start, length) или substr(str, start, length). Пример: substring ('кофе', 2, 2) = 'ОФ'. Важно!!! В SQL индекс начинается с 1 а не с 0
    str - сама строка, которую хотим обрезать
    start - стартовое значение строки для обрезки
    length - итоговая длина строки после обрезки

 - Конкатенация:
    concat(exp1, exp2, exp3) - где exp это выражение

Для примера: Нужно найти строку, длина которой больше 20 символов, обрезать ее до 20 и дописать в конце многоточие:
 - select
	`id`,
	if (
		char_length(`name`) > 20, # Тут меряем длину строки с помощью char_length, в аргументе указываем "имя" строки
        concat(                   # Дальше конкатенация, в ней пишем выражение(сначала обрезка строки через substr)
        substr(`name`, 1, 20),
        '...'),                   # Вторым выражением пишем что приклеить
        `name`
        ) `name`
    from `good`

Конкатенация при группировке
  - select
        o.id,
        group_concat(trim(g.name) separator ', ') products # Этот опертор соединяет сгруппированые заказы,
    from `order` o                                         # Что бы добавить пробел, то нужен опертор seporator
    join `order2good` o2g on                               # Для того что бы убрать лишние пробелы, нужен оператор trim()
        o2g.order_id = o.id
    join `good` g on
        g.id = o2g.good_id
    group by o.id

Замена подстрок:
 - select
        id,
        replace(                       # Оператор работает стандартно (`имя строки`, "что заменить", "на что заменить")
            replace(`name`, '«', '"'), # Тут вкладываем один replays в другой, что бы удалить и открывающие и закрывающие кавычки
            '»', '"'
        )`name`
    from `good`
========================================================================================================================

Функции работы с датой и временем. Важно!!! timestamp полностью идентичен datetime: yyyy-mm-dd hh:mm:ss
Что бы изменить формат даты есть date_format
 - date_format(field, '%d.%m.%Y') - field: Имя поля, через запятую требуемый формат в кавычках, 'Y' - заглавная!
Символы для вывода даты и времени:
 - %d - День месяца (от 01 до 31)
 - %m - Месяц (от 01 до 12)
 - %Y - Год (4 цифры)
 - %H - Часы (от 00 до 23)
 - %i - Минуты (от 00 до 59)
 - %s - Секунды (от 00 до 59)
 - %w - Номер дня недели (0 - Вс, 6 - Суб)
 - %j - День в году (от 001 до 366)

Посмотреть, в какой месяц заказов больше, а в какой меньше. Данные сортируются по месяцам и отсортированы по убыванию
    select
        date_format(creation_date, '%m') `month`,
        count(*) `count`
    from `order`
    group by `month`
    order by `month`

Доп функции:
dayofweek(date) - выводит день недели, если в нее передать дату
dayofyear(date) - выводит день года, если в нее передать дату
Посмотреть в какой день делают больше заказов (в результате получим дни в цифрах от 1 до 7, 1 - это по прежнему воскресенье):
    select
        dayofweek(creation_date) `day`,
        count(*) `count`
    from `order`
    group by `day`
    order by `day`

Получить текущую дату и время:
 - NOW() - Текущая дата
 - CURDATE() - Текущая дата и время
Пример: Втавить в таблицу данные о регистрации нового пользователя, где дата должна быть текущей
    insert into user
        (`name`, `email`, `password`, `reg_date`)
    values
        ('Дмитрий Петров', 'petrov@offstyle.com', 'fdksjkl321da', now()) # Тут втавляем текущую дату через функцию now()

Посчитать разницу между двумя датами (возвращает разницу в количестве дней):
    datediff(now(), '2014-05-12') # Сначала указываем более позднюю дату, вторым аргументом - более раннюю

Работа с временной меткой timestamp - это кол-во секунд прошедших с 1 января 1970 года до определенного времени
Любую дату и время можно преобразовать в метку времени и оброатно:
 - unix_timestamp(date) - Преобразует дату в метку времени
 - from_unitime(timestamp) - Преобразует метку времени в дату

Для примера: Выбрать из таблицы закз номер 248 и преобразовать его дату в timestamp и потом прибвавить к ней один день
    select unix_timestamp(creation_date) from `order` where `id` = 248 # Тут преоброазовываем дату в timestamp
    SELECT FROM_UNIXTIME(1438979566), from_unixtime(1438979566 + 86400) # Тут прибавляем 1 день в секундах (86400 сек.)
========================================================================================================================

Агрегатные функции. Предназначены для обработки данных сразу из нескольких записей
 - count(*) - считает все, что передано в аргументы
    select count(distinct(`name`)) from `good` # Считает уникальные имена в таблце `good`
 - sum(field) - считает сумму полей, которые в аргументах
    select sum(`price` * `count`) # Считает сумму всех товаров
    from `good`
или
    select sum(if(`count` < 50, 1, 0)) # Посчитать кол-во товаров, остаток которых меньше 50. Если истина - 1 в сумму, если нет - 0
    from `good`
 - min(fiel) / max(field) - # Выводят минимальное и максимальное значения в полях, которые переданы в аргументы
 - avg(fiels) - # (average), выводит среднее занчение по полю, которе передано в аргумент
 =======================================================================================================================

Фильтрация после группировки, оператор HAVING. Этот оператор пишится после GROUP BY и применяется к результатам выполнения
агрегирующих функций  в отличии от оператора where
Для примера: Вывести категории товаров, в которых кол-во товаров менее 50 или более 300
    select `category_id`, count(*) `count`
    from `good`
    group by `category_id`               # Тут групируем по полю `category_id`
    having `count` < 50 or `count` > 300 # Здесь дописываем условия вывода
    order by `count` desc # Сортируем по убыванию
или
Вывести все заказы, стоимость которых больше 1000 рублей:
    select
        o.id, sum(o2g.count * g.price) `TotalPrice`
    from `order` o
    join `order2good` o2g on o2g.order_id = o.id
    join `good` g on g.id = o2g.good_id
    group by o.id
    having `TotalPrice` > 1000
========================================================================================================================

Скорость выполнения запросов, индексы в БД. От чего зависит скорость выполнения запросов в БД:
 - Размер таблицы
 - Скорость поиска записей в таблице
 - Типы поиска бывают: Прямой перебор и "По-умному" - он же бинарный (он же половинное деление: в первой половине таблице или во втрой
если в искомый элемент в первой половине, вторую откидываем и не ищем в ней). Для сравнения: Если нужно найти элемнет в
списке, в которм 1 млн. значений, то в бинарном поиске, в худшем случае будет выполнено всего 20 операций (деление списка пополам)
 - В прямом переборе, в худшем случае, может быть до миллиона операций сравнения!!!
Важно! Для бинарного поиска список должен быть отсортирован
 - Так же, для ускорения запросов, в некоторых (ключевых) полях устанавливается индекс. Если он установлен, появляется возможность
использовать бинарынй поиск. Такой индекс называется Primary (или первичный ключ)

Типы индексов:
 - BTREE - Используется в полях, если в них будет производиться поиск с условиями диапазонов ('<', '>', BETWEEN)
 - HASH - Для поиска по точным совпадениям (для них поиски работают максимально быстро)

Виды индексов (ключей):
 1) Первичный (PRIMARY KEY)
 2) Обычный (KEY)
 3) Уникальный (UNIQUE)

Установка первичного индекса при создании таблицы:
    CREATE TABLE `good_type` (
    `id` int not Null auto_incriment,  # Указываем тип данных для поля, НЕ устанавливаем Null по умолчанию, автоувеличение номера записи на 1
    `name` varchar(255),               # Указываем максимальную длину строки
    PRIMARY KEY(`id`)                  # Устанавливаем первичный ключ для поля `id`
    );

Изменение первичного индекса в уже созданой таблице (если он установлен не был):
    ALTER TABLE `good`
        ADD PRIMARY KEY (`id`);        # Добавляем первичный ключ в поле `id`

Установка обычного (не первичного) индекса в уже созданную таблицу:
    ALTER TABLE `good`
        ADD KEY (`category_id`);

Установка уникального (после его установки, в этом поле можно сохранять только уникальные значения):
    ALTER TABLE `good_type`
        ADD UNIQUE (`code`);

Так как уникальный и первичный ключи допускают только уникальные значения, между ними все же ест разница:
----------------------------------------------------------
                            PIMARY KEY      UNIQUE KEY
----------------------------------------------------------
 1) Используются для            ДА      |        НЕТ
 идентификации записей                  |
 2) Может быть одно                     |
    значение NULL               Нет     |         ДА
 3) Может быть несколько
    в одной таблице             Нет     |         Да

Что бы добавить индекс в в поле с текстовыми значениями, стоит установить длину текста по которой будет установлен индекс
Иначе, если ставить индекс по всей длине, смысл его потеряется и поиск будеть долгим:
    ALTER TABLE `good`
        ADD KEY (`name`(30))
========================================================================================================================

Связи, внешние ключи и ограничения. Нарушение целостности данных - это когда записи в одной таблице ссылаются на не
существующие записи в другой таблице. Важно!!! В каждой таблице, поле `id` как правило является первичным ключем

 - Установка связи "Один ко многим":
    ALTER table `good`
        ADD foreign key (`category_id`)          # Здесь добавляем внешний ключ к конкретному полю
            references `good_category` (`id`);   # В этой строке указываем, на что этот ключ ссылается `имя таблицы` (`поле, на которое этот ключ ссылается`)

 - Установка связи "Один к одному"
    ALTER table `countries` ADD unique (`capital_id`); # Сначала устанавливаем уникальный ключ на поле, в котором содержутся ссылки на другую таблицу
    ALTER table `countries`                            # что бы защититься от создание других ссылок на ту же таблицу
    ADD foreign key (`capital_id`)                     # Здесь добавляем внешний ключ к конкретному полю
            references `capitals` (`id`);              # В этой строке указываем, на что этот ключ ссылается `имя таблицы` (`поле, на которое этот ключ ссылается`)

 - Установка связи "Многие ко многим":
    create table `book2order` (                        #
        `id` int not null auto_increment,
        `book_id` int not null,
        `order_id` int not null,
        primary key (`id`),             # Тут устанавливаем первичный ключ на поле `id`
        foreign key (`book_id`)         # Тут ссылка на внешние ключи таблиц, на которые она ссылается
            references `books` (`id`),  # В этих полях уникальные ключи для двух таблиц, на которые установили ссылку
        foreign key (`order_id`)        # Тут ссылка на внешние ключи таблиц, на которые она ссылается
            references `orders` (`id`),
        unique (`book_id`, `order_id`)  # В этих полях уникальные ключи для двух таблиц, на которые установили ссылку
        );

 - Именование ключей (индексов):
    alter table `book2order`
        add constraint `book2order_fk_1`       # Этой командой присваиваем имя ключу
            foreign key (`order_id`)           # Тут ссылка на внешние ключи таблиц, на которые она ссылается
            references `order` (`id`),         # В этих полях уникальные ключи для двух таблиц, на которые установили ссылку
        add constraint `book2order_fk_2`
            foreign key (`book_id`)
            references `book` (`id`);

    Дальше можно будет удалять ключ, обратившись к нему по имени:
        alter table `book2order`
            drop index `book2order_fk_2`

 - Обеспечение целостности данных (с помощью ключей / индексов):
    ALTER table `good`
        ADD foreign key (`category_id`)
        references `good_category` (`id`)
        on delete set null                # При удалении записей из таблицы `good_category`, в поле `category_id` будет установлено значение NULL
        on update no action;              # При изменении поля `id` в `good_category`, произойдет ошибка, если в `good` есть хотя бы одна
                                          # запись, которая ссылается на этот `id` в таблице `good_category`

 - Действия при нарушении целостности данных:
 - RESTRICT / NO ACTION - Это вариант по умолчанию при создании индекса (ограничивает действие, если оно нарушает целостность данных)
 - CASCADE - Каскадное удаление/изменение всех связанных записей
 - SET NULL - Устанавливает значение NULL поле, которе будет ссылаться на несуществующую запись после выполнения изменений
========================================================================================================================

Вложенные запросы (подзапросы в условиях):
 - Посчитать общую сумму групп товаров, чья стоимость до 10000 руб и посчитать сумму группу товаров, чья общая стоимость
выше 10000 руб. Порядок выполнения такого запроса: изнутри - наружу То есть сначала вложенный запрос, который в скобках
после оператора FROM(xxxx) и только потом второй запрос, который стоит после оператора SELECT сверху
    select                                            # Это ВТОРОЙ запрос, получившейся таблице 't' внизу
        sum(if (totalPrice > 10000, totalPrice, 0))
            highpriceTotal,
        sum(if (totalPrice <= 10000, totalPrice, 0))
            lowpriceTotal
    from (select `id`, (`count` * `price`) totalPrice  # Это ПЕРВЫЙ запрос, а верхний уже считает сумму разных групп
        from `good`
        group by `id`) t                           # 't' - это псевдоним таблицы, которая получится в результате запроса

 - Подзапрос, который содержится в УСЛОВИЯХ внешнего запроса: Вываести общие стоимости товаров, кол-во наименований которых
более 50 шту. Важно!! Такие запросы ресурсоемки и снижают быстродействие. Лучше их избегать, и вычислять по отдельности,
с помошью языка програмирования: Сначала получить нужные группы id, и уже потом подставить их в запрос с count
    select `id`, (`count` * `price`) totalPrice
    from `good`
    where `category_id` in (
        select `category_id` from `good`
        group by `category_id` having count(*) > 50
        )
    group by `id`
========================================================================================================================

Структурные запросы:
 - SHOW DATABASES - Посмотреть список доступных БД на сервере
 - USE `databaseName` - перейти к использованию указанной БД
 - CREATE DATABASE `dbName` - создать БД
 - DROP DATABASE `dbName` - удалить базу данных

Запросы на управление таблицами:
 - SHOW TABLES - Показать список имен таблиц в выбранной ДБ
 - DESCRIBE `tableName` - Посмотреть описание таблицы
 - CREATE TABLE `good_type` (  - Создать таблицу
	`id` int not null auto_increment,
	`sort_index` int,
    `name` varchar (255),
    primary key (`id`)
	)
 - Удаление/добавка/полей в таблице
    alter table `good_type`
        drop column `name`,      # Удалить строку `name`
        add `code` text not null # Добавить строку `code`
            after `id`           # Указать, куда именно добавить (после какой строки)

 - Очистка таблицы (плюс сброс автоинкремента):
    TRUNCATE `tableName` - очистить таблицу

 - Удаление таблицы:
    DROP `tablename` - полностью удаляет таблицу
========================================================================================================================

Представления - это виртуальные виртуальные таблицы, которые используются для формирования динамических наборов данных

 - Создать представление (Для частого обращения к списку товаров, которых менее 10 и ценой более 200 рублей)
    create view `ending_goods` as                 # Сначала создаем представление
    select * from `good`
    where `count` < 10 and `price` > 200;
    select * from `ending_goods`                  # Потом отдельным запросом к нему обращаемся

 - Изменить уже существующее представление:
    create or replace view `ending_goods` as      # Тут просто добавляется условие "OR REPLACE" и далее тот же синтаксис
    select * from `good`
    where `count` > 10 and `price` < 200;
    select * from `ending_goods`

 - Удалить представление:
    DROP view `ending_goods; - полностью удаляет представление
========================================================================================================================

Проектирование структуры базы данных. Что бы делать это эффективно, нужно для начала ответить на вопросы и прописать, какие
в будущей БД будут:
 - таблицы (названия принято писать маленькими латинскими буквами)
 - Поля (числа, строки, даты и т.д.)
 - Связи
