# Django-stripe project

## Запуск проекта с помощью Docker
### Делаем копию проекта
```
git clone https://github.com/brintadis/django-stripe.git
```
### Создаем и активируем виртуальное окружение
```
python -m venv env
```
```
env\Scripts\activate
```
```
pip install -r requirments.txt
```
### Получение Stripe api ключей
Регистрируем аккаунт [Stripe](https://dashboard.stripe.com/settings/account/) и указываем `Account name`.
Stripe ключи можно получить [здесь](https://dashboard.stripe.com/test/apikeys).
### Создаем файл конфигурации `.env` с необходимыми переменными
```
# DB
POSTGRES_USER=stripe
POSTGRES_PASSWORD=stripe
POSTGRES_DB=stripe
POSTGRES_HOST=db

# Django settings
DJANGO_SECRET_KEY=mydjangosecretkey
DJANGO_SETTINGS_MODULE=stripe_project.settings

# Stripe
STRIPE_PUBLISHABLE_KEY=Your Stripe Publishable Key
STRIPE_SECRET_KEY=Your Stripe Secret Key
```
### Сборка контрейнеров
```
docker-compose build
```
### Запуск контейнеров
```
docker-compose up
```
## Создание и применение миграций, добавление записи item в базу данных
### После запуска контейнеров в Docker Desktop открыть терминал контейнера `stripe_web`:
<img src= "https://imgur.com/e2QeRtn.png" width = "1000" height = "120">

### Создание миграций
```
python stripe_project/manage.py makemigrations
```
### Применение миграций
```
python stripe_project/manage.py migrate
```
### Создание админ аккаунта
```
python stripe_project/manage.py createsuperuser
```
### Создание записи в бд делаем через админ панель
```http://localhost:8000/admin```
#### Вводим данные, которые указывали в предыдущем пункте.
***
## Документация
```GET http://localhost:8000/item/<id>``` - HTML страница с информацией о выбранном `item` с кнопкой купить.

```GET http://localhost:8000/buy/<id>``` - получение Stripe Session Id для оплаты выбранного `item`.
***
## Выполненные бонусные задачи:
- Запуск используя Docker
- Использование environment variables
- Просмотр Django Моделей в Django Admin панели

