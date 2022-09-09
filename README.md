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
## Создание и применение миграций
### После запуска контейнеров в Docker Desktop открыть терминал контейнера `stripe_web`:
<img src= "https://imgur.com/e2QeRtn.png" width = "1000" height = "100">

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
## Выполненные бонусные задачи:
### - Запуск используя Docker
### - Использование environment variables
### - Просмотр Django Моделей в Django Admin панели

