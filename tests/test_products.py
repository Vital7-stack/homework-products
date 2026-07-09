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


# --- Новые тесты для магических методов ---

def test_product_str() -> None:
    p = Product("Чай", "Чёрный чай", 250.5, 10)
    expected = "Чай, 250.5 руб. Остаток: 10 шт."
    assert str(p) == expected


def test_category_str() -> None:
    p1 = Product("Чай", "Чёрный чай", 250.5, 10)
    p2 = Product("Кофе", "Арабика", 400.0, 5)
    c = Category("Напитки", "Все напитки", [p1, p2])
    # Общее количество: 10 + 5 = 15
    expected = "Напитки, количество продуктов: 15 шт."
    assert str(c) == expected


def test_product_add() -> None:
    # a: 100 × 10 = 1000
    a = Product("Товар А", "Описание А", 100.0, 10)
    # b: 200 × 2 = 400
    b = Product("Товар Б", "Описание Б", 200.0, 2)
    # Итого: 1400
    total = a + b
    assert total == 1400.0