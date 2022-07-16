<h1 align=center> Горецкий Максим </h1>
<h2 align=center>Тестовое задание Python </h2>

---

<h3 align=center> Описание проекта </h3>

Список магазинов в вашем городе.

<h3 align=center> Функционал </h3>

Запросы:
GET/city/—получение списка городов
GET/city/city_id/street/ — получение всех улиц города
POST/shop/create — создание магазина
GET/shop/list?street=&city=&open=0/1—получение списка магазинов c возможностью фильтрации(необезательна):
street = наименование улицы
city = наимнование города
open 1 или 0, где 1 открыт, 0 закрыт

<h3 align=center> Установка </h3>

pip install -r requirements.txt

<h4>Обратить внимание что для установки psycopg2-binary(*unix/macOS) нужно установить PostgreSql
Для работы в операционной системе Windows заменить psycopg2-binary на psycopg2 в файле requirements.txt </h4>
https://www.postgresql.org/download/

Более подробную информацию можно найти в официальной документации https://www.psycopg.org/docs/install.html
