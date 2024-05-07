##### Команды для подгрузки бд после запуска. Выполнить один раз в app контейнере.
##### Выполнить миграции
```
python manage.py makemigrations --no-input tavern_of_heroes
python manage.py migrate --no-input
```
##### Создание админа:
`python manage.py createsuperuser`
##### Создание нескольких тестовых записей:
`python manage.py loaddata db.json`
##### Либо напрямую в докер:
```
docker-compose run app python manage.py makemigrations --no-input tavern_of_heroes
docker-compose run app python manage.py migrate --no-input
docker-compose run app python manage.py createsuperuser
docker-compose run app python manage.py loaddata db.json
```