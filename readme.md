# LinkShorter
### Для чего?
Данный сервис используется для сокращения ссылок.
### Стек
Проект написан на Django, в качестве БД использовалась PostgreSQL, для кеширования использовался Redis, для развертывания использовался Docker.
### Как запустить проект
Для запуска нужно использовать Docker, также создать файл .env в корне проекта:
1) Написать .env по примеру файла .env_example (можно переименовать .env_example в .env, тогда можно пропустить следующий шаг)
2) В docker-compose.yml в блоке db в environment изменить значения переменных POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB на значения из файла .env
3) В терминале ввести команду ```docker-compose up -d --build```
4) Перейти по адресу http://localhost:8000
После этого можно пользоваться сервисом.
### Как использовать
Чтобы создать администратора нужно написать следующую команду в терминале - ```docker exec -it link_shorter python manage.py createsuperuser```. После этого перейти по адресу http://localhost:8000/login и авторизоваться.
Если нужно создать обычного пользователя, то можно перейти по адресу http://localhost:8000/signup и зарегистрироваться.
