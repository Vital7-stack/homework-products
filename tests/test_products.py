from src.products import Product, Category


def test_product_initialization():
    p = Product("Чай", "Чёрный чай", 250.5, 10)
    assert p.name == "Чай"
    assert p.description == "Чёрный чай"
    assert p.price == 250.5
    assert p.quantity == 10


def test_category_initialization():
    p1 = Product("Чай", "Чёрный чай", 250.5, 10)
    p2 = Product("Кофе", "Арабика", 400.0, 5)
    c = Category("Напитки", "Все напитки", [p1, p2])
    assert c.name == "Напитки"
    assert c.description == "Все напитки"
    assert len(c.products) == 2
    assert c.products[0] is p1
    assert c.products[1] is p2


def test_category_counters_increase():
    Category.category_count = 0
    Category.product_count = 0

    p1 = Product("Чай", "Чёрный чай", 250.5, 10)
    p2 = Product("Кофе", "Арабика", 400.0, 5)

    c1 = Category("Напитки", "Все напитки", [p1, p2])
    assert Category.category_count == 1
    assert Category.product_count == 2
    assert c1.name == "Напитки"

    c2 = Category("Сладости", "Всё сладкое", [])
    assert Category.category_count == 2
    assert Category.product_count == 2
    assert c2.name == "Сладости"

    c3 = Category("Фрукты", "Свежие фрукты", [Product("Яблоко", "Зелёное", 120.0, 20)])
    assert Category.category_count == 3
    assert Category.product_count == 3
    assert c3.name == "Фрукты"
