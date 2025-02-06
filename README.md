### Тестирование API

### Цель:

Потренироваться тестировать API сервисы на основе их документации

### Описание:

#### Часть 1

Нужно написать тесты для API следующих сервисов:

- https://dog.ceo/dog-api/
- https://www.openbrewerydb.org/
- https://jsonplaceholder.typicode.com/

Для каждого из указанных выше сервисов должны быть выполнены следующие условия:

- Написать минимум 5 тестов для REST API сервиса
- Как минимум 2 из 5 тестов должны использовать параметризацию
- Документация к API есть на сайте 
- Тесты должны успешно проходить

Тестирование каждого API оформить в отдельном тестовом модуле

#### Часть 2

Реализуйте в отдельном модуле (файле) тестовую функцию, которая будет принимать 2 параметра:  

`url` - значение по умолчанию https://ya.ru  
`status_code` - значение по умолчанию `200`

Параметры должны быть реализованы через `pytest.addoption`. Можно положить фикcтуру и тестовую функцию в один файл.
Основная задача чтобы ваш тест проверял статус ответа по переданному URL. 
Например, по несуществующему адресу https://ya.ru/sfhfh должен быть валидным ответ `404`

Пример запуска pytest: 

```shell
test_module.py --url=https://mail.ru --status_code=200
```

#### Часть 3 (опционально)

В качестве дополнительного "задания со звёздочкой" вам предлагается потренироваться
в тестировании реального продуктового API компании [Gectaro](https://gectaro.com/).

Описание API можно посмотреть по ссылке https://swagger.gectaro.com/

Для разработки тестов предлагается использовать эндпоинт[Снабжение: Заявки](https://swagger.gectaro.com/#/%D0%A1%D0%BD%D0%B0%D0%B1%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5%3A%20%D0%97%D0%B0%D1%8F%D0%B2%D0%BA%D0%B8)

Руководство к тестированию можно посмотреть [тут](https://gectaro.notion.site/API-Gectaro-x-OTUS-68fc9f6513f14f41b1bb5bf10589bbe8?pvs=4)

Для указанного эндпоинта нужно:

- Для каждого метода эндпоинта **Снабжение: Заявки** нужно написать 2 позитивных и 2 негативных теста.
- Если находите баг, то его нужно задокументировать (например, в Google Docs).

Список найденных багов нужно прислать в виде ссылки на Google-документ в ЛК.

### Как начать работать с API Gectaro:

1. Указать ваш email в специальной форме, ссылка на которую будет предоставлена преподавателем.
2. На ваш email будет отправлена ссылка для подтверждения регистрации.
3. Для вас будет создан отдельный аккаунт в API Gectaro.
4. Также для вас будет создан проект, в рамках которого можно будет работать с разделом **Снабжение: Заявки**.
5. Для осуществления запросов к API нужно использовать API-key, который можно взять из настроек профиля 
(см. [скриншот](Gectaro_API_Key.png)).

### Критерии оценки:

Статус "Принято" ставится, если:

1. Под тесты каждого сервиса заведён отдельный файл
2. Для каждого сервиса написано минимум 5 тестов, 2 из которых используют параметризацию
3. Реализована тестовая функция, которая принимает 2 параметра
4. Задание выполнено и сдаётся в формате pull-request
5. Для всех файлов соблюдается минимальный код-стайл 

Критерии оценки для дополнительного задания:

1. Написаны тесты для каждого метода эндпоинта Снабжение: Заявки 
2. Найденные баги оформлены в Google-документе
