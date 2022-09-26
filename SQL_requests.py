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
- Фильтрация по датам: SELECT `id`, `name`, `reg_time` from `user` WHERE `reg_date` >= '2019-01-01'
- Фильтрация по диапазону дат/времени: SELECT * from `user` WHERE `reg_date`>= '2019-08-01' and `reg_date`<= '2019-07-01'