import math
import random


def test_greeting():
    name = "Анна"
    age = 25
    # Сформируйте нужную строку
    output = f"Привет, {name}! Тебе {age} лет."
    # Проверяем результат
    assert output == "Привет, Анна! Тебе 25 лет."


def test_rectangle():
    a = 10
    b = 20
    # сосчитайте периметр
    perimeter = 2 * (a + b)
    assert perimeter == 60
    # сосчитайте площадь
    area = a * b
    assert area == 200


def test_circle():
    r = 23
    # сосчитайте площадь
    area = math.pi * r * r
    assert area == 1661.9025137490005
    # сосчитайте длину окружности
    length = r * (math.pi * 2)
    assert length == 144.51326206513048


def test_random_list():
    # создайте список
    l = []
    for i in range(10):
        random_numb = random.randint(0, 100)
        l.append(random_numb)
        l.sort()
    assert len(l) == 10
    assert l[0] < l[-1]


def test_unique_elements():
    l = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 10]
    # удалите повторяющиеся элементы
    l = list(set(l))
    assert isinstance(l, list)
    assert len(l) == 10
    assert l == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_dicts():
    first = ["a", "b", "c", "d", "e"]
    second = [1, 2, 3, 4, 5]
    # создайте словарь
    d = dict(zip(first, second))
    assert isinstance(d, dict)
    assert len(d) == 5
    print(d)
