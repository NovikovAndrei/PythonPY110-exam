from typing import Iterator
import json
from random import randint, uniform, choice

from faker import Faker

from conf import MODEL

fake = Faker(locale="ru")


def get_title():
    """Возвращает случайное название книги"""
    with open('books.txt', encoding='utf8') as f:
        random_book = choice(f.readlines()).rstrip()
        return random_book


def get_year() -> int:
    """Возвращает случайный год написания книги"""
    return randint(1985, 2010)


def get_pages() -> int:
    """Возвращает случайное количество страниц в книге"""
    return randint(100, 500)


def get_isbn13() -> str:
    """Возвращает случайный номер isbn13"""
    return fake.isbn13()


def get_rating() -> float:
    """Возвращает случаный рейтинг книги"""
    return round(uniform(0, 5), 1)


def get_price() -> str:
    """Возвращает случайную цену книги"""
    return f'{round(uniform(100, 5000), 2)} руб.'


def get_author() -> list:
    """Возвращает случайный список авторов от 1-го до 3-х"""
    male = f'{fake.first_name_male()} {fake.last_name_male()}'
    female = f'{fake.first_name_female()} {fake.last_name_female()}'
    res = [male, female]
    return [choice(res) for _ in range(randint(1, 3))]


def gen_book(pk: int = 1) -> Iterator:
    """Генератор для книг
    :param pk: начальное значение номера книги"""
    while True:
        yield {
            "model": MODEL,
            "pk": pk,
            "fields": {
                'title': get_title(),
                'year': get_year(),
                'pages': get_pages(),
                'isbn13': get_isbn13(),
                'rating': get_rating(),
                'price': get_price(),
                'author': get_author()
            }
        }
        pk += 1


def main():
    """Генерирует 100 случайных книг и записывает их в файл res.json"""
    books = gen_book()
    res = [next(books) for _ in range(100)]
    with open('res.json', 'w', encoding='utf8') as f:
        f.write(json.dumps(res, indent=4, ensure_ascii=False))


if __name__ == "__main__":
    main()
