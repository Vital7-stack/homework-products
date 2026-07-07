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

    # ИСПРАВЛЕНО: products теперь возвращает строку, а не список.
    # Проверяем, что в строке есть оба товара в нужном формате.
    output = c.products
    assert "Чай, 250.5 руб. Остаток: 10 шт." in output
    assert "Кофе, 400.0 руб. Остаток: 5 шт." in output


def test_category_counters_increase():
    initial_cat_count = Category.category_count
    initial_prod_count = Category.product_count

    p1 = Product("Чай", "Чёрный чай", 250.5, 10)
    p2 = Product("Кофе", "Арабика", 400.0, 5)

    c1 = Category("Напитки", "Все напитки", [p1, p2])
    assert c1.name == "Напитки"                 # <-- теперь c1 используется
    assert Category.category_count == initial_cat_count + 1
    assert Category.product_count == initial_prod_count + 2

    c2 = Category("Сладости", "Всё сладкое", [])
    assert c2.name == "Сладости"                 # <-- теперь c2 используется
    assert Category.category_count == initial_cat_count + 2
    assert Category.product_count == initial_prod_count + 2

    c3 = Category("Фрукты", "Свежие фрукты", [Product("Яблоко", "Зелёное", 120.0, 20)])
    assert c3.name == "Фрукты"                  # <-- теперь c3 используется
    assert Category.category_count == initial_cat_count + 3
    assert Category.product_count == initial_prod_count + 3