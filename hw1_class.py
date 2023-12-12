import json
import keyword


class ColorizeMixin:
    def __init_subclass__(cls):
        super().__init_subclass__()
        cls.repr_color_code = 33

    def __str__(self):
        return f'\033[{self.repr_color_code}m{self.title} | {self.price} ₽'


class Parser:
    def __init__(self, data: dict):
        for key, value in data.items():
            if isinstance(value, dict):
                setattr(self, key, Parser(value))
            else:
                if keyword.iskeyword(key):
                    key = f"{key}_"
                setattr(self, key, value)


class Advert(ColorizeMixin, Parser):
    repr_color_code = 32

    def __init__(self, data: dict):
        super().__init__(data)
        self._price = 0
        if hasattr(self, 'price'):
            self.check_price(self.price)
        if not hasattr(self, 'title'):
            raise ValueError("There is no title in the ad")

    def check_price(self, price):
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Price must be >= 0")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self.check_price(value)
        self._price = value


if __name__ == '__main__':

    lesson_str = """{
        "title": "python",
        "price": 0,
        "location": {
            "address": "город Москва, Лесная, 7",
            "metro_stations": ["Белорусская", "Гагаринская"]
            }
        }"""
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    assert lesson_ad.location.address == 'город Москва, Лесная, 7'
