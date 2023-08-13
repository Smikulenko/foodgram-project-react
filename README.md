![workflow](https://github.com/Smikulenko/foodgram-project-react/actions/workflows/main.yml/badge.svg)
# Foodgram project
На этом сервисе пользователи смогут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.

# **Используемые технологии**
Python 3.9, Django 3.2.13,  Django Rest Framework (DRF) 3.12.4, Simple-JWT 4.7.2, Djoser 2.1.0


# **Как запустить проект:**
Клонировать репозиторий и перейти в него в командной строке:

Cоздать и активировать виртуальное окружение:
```
python3 -m venv env
```
```
source env/bin/activate
```
Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
Выполнить миграции:
```
python3 manage.py migrate
```
Запустить проект:
```
python3 manage.py runserver
```

# **Примеры запросов API**

Регистрация пользователя:
```
   POST /api//users/
```
Получение данных текущего пользователя:
```
   GET /api/users/me/
```
Добавление подписки:
```
   POST /api/users/id/subscribe/
```
Скачать список покупок
```
   GET /api/recipes/download_shopping_cart/
```

IP - 84.252.131.215

login admin

password 2332opL


**Автор**
*Микуленко Софья*
