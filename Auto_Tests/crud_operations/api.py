from crud_operations.crud import CRUD


# Класс для работы с API сервисом
class GMAPI:
    def __init__(self):  # Базовые параметры для работы с запросами
        self.api_key = "?key=qaclick123"
        self.base_url = "https://rahulshettyacademy.com"
        self.post_resources = "/maps/api/place/add/json"
        self.get_resources = "/maps/api/place/get/json"
        self.body = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            },
            "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "https://google.com",
            "language": "French-IN"
        }

    # Вывод ответа Post-запроса
    def create_new_place(self):
        url = self.base_url + self.post_resources + self.api_key
        print(url)
        return CRUD.post(url, self.body)

    # Вывод ответа Get-запроса
    def get_place_by_place_id(self, place_id):
        url = self.base_url + self.get_resources + self.api_key + '&place_id=' + place_id
        print(url)
        return CRUD.get(url)
