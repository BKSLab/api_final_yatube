# API для взаимодействия с блог-платформой Yatube

## Описание проекта api_final_yatube

Проект api_final_yatube является учебным проектом  
для взаимодействия с сервисом публикаций yatube.  

## Разворачивание проекта api_final_yatube

После клонирования репозитория с GitHub:

- создать виртуальное окружение (версия Python 3.9.10);
- установить зависимости из файла requirements.txt
- запустить локальный сервер.

## Доступ к API

API доступен по Адресу:  

    http://127.0.0.1:8000/api/v1/

## Адреса и методы запросов к API

### Аутентификация. JWT токен

У неаутентифицированных пользователей доступ к API ограничен.  
Неаутентифицированные пользователи могут отправлять только GET запросы, за исключением GET запросов
для получения списка подписок. Список подписок может получить
только аутентифицированный пользователь.  

Получение токена аутентификации Метод POST:  

    http://127.0.0.1:8000/api/v1/jwt/create

Обновление токена аутентификации. Метод POST:  

    http://127.0.0.1:8000/api/v1/jwt/refresh/

Проверка токена аутентификации. Метод POST:  

    http://127.0.0.1:8000/api/v1/jwt/verify/

### Получение, создание, изменение и удаление публикаций

Получение списка публикаций. Метод GET:  

    http://127.0.0.1:8000/api/v1/posts/

Допустимые параметры запроса:

- limit - количество публикаций на страницу;
- offset - Номер страницы после которой начинать выдачу.

**Примечание:** при указании параметров limit и offset
публикации возвраащаются с пагинацией.  

Создание новой публикации (не доступно анонимным пользователям). Метод POST:  

    http://127.0.0.1:8000/api/v1/posts/

Получение отдельной публикации. Метод GET:  

    http://127.0.0.1:8000/api/v1/posts/{id}/

Полное изменение (метод PUT) или частичное изменение (Метод PATCH) публикации:  

    http://127.0.0.1:8000/api/v1/posts/{id}/

Удаление публикации. Метод DELETE:  

    http://127.0.0.1:8000/api/v1/posts/{id}/

### Получение, создание, изменение и удаление комментариев

Получение списка комментариев к заданной публикации. Метод GET:  

    http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/

Добавленние нового комментария к публикации. Метод POST:  

    http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/

Получение отдельного комментария к публикации. Метод GET:  

    http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/

Полное изменение (метод PUT) или частичное изменение (Метод PATCH) комментария:

    http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/

Удаление комментария. Метод DELETE:  

    http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/

### Получение списка сообществ и информацции о конкретном сообществе

Получение списка сообществ. Метод GET:  

    http://127.0.0.1:8000/api/v1/groups/

Получение информации об отдельном сообществе. Метод GET:  

    http://127.0.0.1:8000/api/v1/groups/{id}/

### Получение списка подписок и создание новой подписки

Получение всех подписок пользователя, сделавшего запрос. Метод GET:  

    http://127.0.0.1:8000/api/v1/follow/

Создание новой подписки пользователя, от имени которого
сделан запрос на указанного в теле запроса пользователя:  

    http://127.0.0.1:8000/api/v1/follow/


## Об авторе проекта
Барабанщиков Кирилл, я python backend разработчик.

## Мои контакты
Telegram: https://t.me/Kirill_Barabanshchikov
почта: bks2408@mail.ru
