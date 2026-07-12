import io
import sys
import pytest
from src.products import BaseProduct, Product, Smartphone, LawnGrass, Category


# --- Базовые тесты (без дублей) ---

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


def test_product_add_same_type() -> None:
    # a: 100 × 10 = 1000
    a = Product("Товар А", "Описание А", 100.0, 10)
    # b: 200 × 2 = 400
    b = Product("Товар Б", "Описание Б", 200.0, 2)
    # Итого: 1400
    total = a + b
    assert total == 1400.0


# --- Тесты для новых классов и проверок типов ---

def test_smartphone_inheritance() -> None:
    s = Smartphone(
        name="iPhone",
        description="Смартфон Apple",
        price=100000.0,
        quantity=5,
        efficiency=95.0,
        model="15 Pro",
        memory=256,
        color="серый",
    )
    assert isinstance(s, Product)
    assert s.model == "15 Pro"
    assert s.memory == 256
    assert s.color == "серый"


def test_lawn_grass_inheritance() -> None:
    g = LawnGrass(
        name="Газонная трава",
        description="Смесь для газона",
        price=2000.0,
        quantity=10,
        country="Россия",
        germination_period=14,
        color="зелёный",
    )
    assert isinstance(g, Product)
    assert g.country == "Россия"
    assert g.germination_period == 14
    assert g.color == "зелёный"


def test_add_different_types_raises_type_error() -> None:
    s = Smartphone(
        name="Phone",
        description="",
        price=50000.0,
        quantity=2,
        efficiency=80.0,
        model="X",
        memory=128,
        color="чёрный",
    )
    g = LawnGrass(
        name="Трава",
        description="",
        price=3000.0,
        quantity=5,
        country="Китай",
        germination_period=7,
        color="зелёный",
    )
    with pytest.raises(TypeError):
        _ = s + g


def test_add_product_wrong_type_raises_type_error() -> None:
    c = Category("Электроника", "Смартфоны и аксессуары", [])
    with pytest.raises(TypeError):
        c.add_product("не продукт")  # type: ignore

    with pytest.raises(TypeError):
        c.add_product(123)  # type: ignore


# --- НОВЫЕ ТЕСТЫ: Abstract Base Class и LoggingMixin ---

def test_cannot_instantiate_base_product() -> None:
    """Нельзя создать экземпляр абстрактного класса напрямую."""
    with pytest.raises(TypeError):
        BaseProduct()


def test_logging_mixin_output_for_product(capsys) -> None:
    """Миксин должен выводить строку создания объекта Product в консоль."""
    p = Product("Чай", "Чёрный чай", 250.5, 10)
    captured = capsys.readouterr()

    # Проверяем, что строка вывода содержит имя класса и аргументы
    assert "Product('Чай', 'Чёрный чай', 250.5, 10)" in captured.out


def test_logging_mixin_output_for_smartphone(capsys) -> None:
    """Миксин должен корректно работать и для наследников (Smartphone)."""
    s = Smartphone(
        name="iPhone",
        description="Смартфон Apple",
        price=100000.0,
        quantity=5,
        efficiency=95.0,
        model="15 Pro",
        memory=256,
        color="серый",
    )
    captured = capsys.readouterr()

    # Достаточно проверить, что имя класса и имя продукта есть в выводе
    assert "Smartphone" in captured.out
    assert "'iPhone'" in captured.out


def test_logging_mixin_output_for_lawn_grass(capsys) -> None:
    """Миксин должен корректно работать и для LawnGrass."""
    g = LawnGrass(
        name="Газонная трава",
        description="Смесь для газона",
        price=2000.0,
        quantity=10,
        country="Россия",
        germination_period=14,
        color="зелёный",
    )
    captured = capsys.readouterr()

    assert "LawnGrass" in captured.out
    assert "'Газонная трава'" in captured.out


def test_base_methods_implemented_in_product() -> None:
    """Product должен реализовывать все абстрактные методы BaseProduct."""
    p = Product("Тест", "Описание теста", 123.45, 1)

    assert p.get_name() == "Тест"
    assert p.get_price() == 123.45
    assert "Тест: Описание теста" in p.describe()


def test_describe_overridden_in_smartphone() -> None:
    """Smartphone должен переопределять describe и включать свои специфичные поля."""
    s = Smartphone("S1", "Смартфон", 15000, 3, 90, "A1", 128, "blue")
    desc = s.describe()

    assert "смартфон" in desc.lower()
    assert "A1" in desc
    assert "128" in desc


def test_describe_overridden_in_lawn_grass() -> None:
    """LawnGrass должен переопределять describe и включать свои специфичные поля."""
    g = LawnGrass("G1", "Трава", 400, 5, "DE", 5, "green")
    desc = g.describe()

    assert "газонная трава" in desc.lower()
    assert "DE" in desc
