### Сайт-блог про мотоциклы

---

### Описание
Сайт на фреймворке Django, посвященный статьям про мотоциклы. Реализованы следующие требования:  
1. Статьи хранятся в базе данных, имеют поле связанное с таблицей, содержащей категорию статьи.
2. Реализованы CRUD операции над статьями.
3. Добавлен механизм регистрации и авторизации пользователей.
4. Разграничены права авторизованных и неавторизованных пользователей.
5. Пользователи могут редактировать и удалять только свои записи.
6. Добавлена аутентификация через сторонные сервисы - VK и Яндекс.
7. Добавлена возможность загрузки изображений в статьи.
8. Сделано базовое оформление сайта с помощью стилей Bootstrap.

*Тестовый аккаунт суперпользователя  
логин: admin  
пароль: admin*  

#### Запуск сервера из домашней дирректории:
>python manage.py runserver

#### Скриншоты:  
![Image alt](https://github.com/IvanSitnikov1/moto_site/blob/main/%D0%A1%D0%BA%D1%80%D0%B8%D0%BD%D1%88%D0%BE%D1%82%D1%8B/1.png)
![Image alt](https://github.com/IvanSitnikov1/moto_site/blob/main/%D0%A1%D0%BA%D1%80%D0%B8%D0%BD%D1%88%D0%BE%D1%82%D1%8B/2.png)
![Image alt](https://github.com/IvanSitnikov1/moto_site/blob/main/%D0%A1%D0%BA%D1%80%D0%B8%D0%BD%D1%88%D0%BE%D1%82%D1%8B/3.png)
![Image alt](https://github.com/IvanSitnikov1/moto_site/blob/main/%D0%A1%D0%BA%D1%80%D0%B8%D0%BD%D1%88%D0%BE%D1%82%D1%8B/4.png)
![Image alt](https://github.com/IvanSitnikov1/moto_site/blob/main/%D0%A1%D0%BA%D1%80%D0%B8%D0%BD%D1%88%D0%BE%D1%82%D1%8B/5.png)

#### Стек: Python | Django | HTML | CSS | Bootstrap | social_django
