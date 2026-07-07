
from src.products import Product, Category


def test_product_initialization() -> None:
    p = Product("Чай", "Чёрный чай", 250.5, 10)
    assert p.name == "Чай"
    assert p.description == "Чёрный чай"
    assert p.price == 250.5
    assert p.quantity == 10


def test_category_initialization() -> None:
    p1 = Product("Чай", "Чёрный чай", 250.5, 10)
    p2 = Product("Кофе", "Арабика", 400.0, 5)
    c = Category("Напитки", "Все напитки", [p1, p2])

    assert c.name == "Напитки"
    assert c.description == "Все напитки"

    # Исправленная проверка: разбиваем ожидаемую строку на части,
    # чтобы не было длинной строки в коде и чтобы тест был читаемым.
    expected_part_1 = "Чай, 250.5 руб. Остаток: 10 шт."
    expected_part_2 = "Кофе, 400.0 руб. Остаток: 5 шт."

    output = c.products
    assert expected_part_1 in output
    assert expected_part_2 in output


def test_category_counters_increase() -> None:
    initial_cat_count: int = Category.category_count
    initial_prod_count: int = Category.product_count

    p1 = Product("Чай", "Чёрный чай", 250.5, 10)
    p2 = Product("Кофе", "Арабика", 400.0, 5)

    c1 = Category("Напитки", "Все напитки", [p1, p2])
    assert c1.name == "Напитки"
    assert Category.category_count == initial_cat_count + 1
    assert Category.product_count == initial_prod_count + 2

    c2 = Category("Сладости", "Всё сладкое", [])
    assert c2.name == "Сладости"
    assert Category.category_count == initial_cat_count + 2
    assert Category.product_count == initial_prod_count + 2

    c3 = Category(
        "Фрукты",
        "Свежие фрукты",
        [Product("Яблоко", "Зелёное", 120.0, 20)],
    )
    assert c3.name == "Фрукты"
    assert Category.category_count == initial_cat_count + 3
    assert Category.product_count == initial_prod_count + 3
