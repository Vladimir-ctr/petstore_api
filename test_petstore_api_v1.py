import requests
import pytest


@pytest.fixture()
def create_pet():  # функция предусловия
    body_pet_post = {  # Создаем переменную для удобного размещения json в коде теста
            "id": 1231234,
            "category": {
                "id": 123,
                "name": "huklya"
            },
            "name": "kuklya",
            "photoUrls": [
                "string"
            ],
            "tags": [
                {
                    "id": 12,
                    "name": "string"
                }
            ],
            "status": "available"
        }

    response = requests.post('https://petstore.swagger.io/v2/pet', json=body_pet_post).json()
    yield response["id"]  # все что под yield выполнится после завершения теста
    requests.delete(f'https://petstore.swagger.io/v2/pet/{response["id"]}')


def test_petstore_post():
    body_pet_post = {  # Создаем переменную для удобного размещения json в коде теста
            "id": 100199,
            "category": {
                "id": 0,
                "name": "huklya"
            },
            "name": "kuklya",
            "photoUrls": [
                "string"
            ],
            "tags": [
                {
                    "id": 0,
                    "name": "string"
                }
            ],
            "status": "available"
        }

    response = requests.post('https://petstore.swagger.io/v2/pet', json=body_pet_post)  # описание кода который выше
    assert response.status_code == 200  # переменная = выполнить запрос методом post(нужный url),
    data = response.json()  # подставить данные (тело запроса) в формате json. Получить ответ в формате json
    # получить ответ в формате json (c помощью точки мы, как бы, обращаемся к методу
    # (точнее к его данным), который выполнили, и просим его вывести нам данные которые содержи ответ)

    # с помощью точки обращаемся к данным о статус коде ответа при этом из самого запроса убираем

    # возврат данных в формате json
    # проверка, что в теле ответа есть параметр "name" == "name в теле ответа"
    assert data["name"] == body_pet_post["name"]  # с помощью массива(Списка) мы обращаемся к параметру в теле ответа
    requests.delete(f'https://petstore.swagger.io/v2/pet/{"id"}')


def test_petstore_get(create_pet):  # мы импортировали из pytest и сделали фикстуру из предусловия смотри выше
    # pet_id = create_pet()                  # мы создали выше предусловие - функцию create_pet которая каждый раз будет создавать новый объект тем самым делая тесты независимыми
    response = requests.get(f'https://petstore.swagger.io/v2/pet/{create_pet}').json()
    assert response["id"] == create_pet


def test_petstore_put(create_pet):
    body_pet_put = {
        "id": create_pet,
        "category": {
            "id": 0,
            "name": "New name"
        },
        "name": "New Style",
        "photoUrls": [
             "string"
        ],
         "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }
    response = requests.put('https://petstore.swagger.io/v2/pet', json=body_pet_put)
    assert response.status_code == 200
    data = response.json()  # вытаскиваем из ответа его тело в формате json и записываем все это под переменной data это позволит выполнить еще ряд проверок

    assert data["id"] == create_pet
    assert data["name"] == "New Style"
    assert data["category"]["name"] == "New name"  # чтобы проверять json параметра надо написать сначала параметр в скобках, а потом его содержимое которе хотим проверить


    #
    #
def test_petstore_delete(create_pet):
    response = requests.delete(f'https://petstore.swagger.io/v2/pet/{create_pet}')
    assert response.status_code == 200
