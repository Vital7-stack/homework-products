from typing import List, Dict


class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        # Задание 4: атрибут цены приватный
        self.__price = price
        self.quantity = quantity

    # Задание 4: Геттер для цены
    @property
    def price(self) -> float:
        return self.__price

    # Задание 4: Сеттер для цены с проверкой
    @price.setter
    def price(self, new_price: float) -> None:
        if new_price > 0:
            self.__price = new_price
        else:
            print("Цена не должна быть нулевая или отрицательная")

    # Задание 3: Класс-метод new_product
    @classmethod
    def new_product(cls, data: Dict) -> "Product":
        return cls(
            name=data["name"],
            description=data.get("description", ""),
            price=data["price"],
            quantity=data["quantity"]
        )


class Category:
    # Атрибуты класса (счётчики)
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: List[Product]) -> None:
        self.name = name
        self.description = description
        # Задание 1: список товаров приватный
        self.__products = products

        # Увеличиваем счётчики
        Category.category_count += 1
        Category.product_count += len(products)

    # Задание 1: метод для добавления продукта
    def add_product(self, product: Product) -> None:
        self.__products.append(product)
        Category.product_count += 1

    # Задание 2: Геттер для вывода списка товаров в виде строки
    @property
    def products(self) -> str:
        result = ""
        for p in self.__products:
            # Строго по шаблону: "Название продукта, X руб. Остаток: X шт.\n"
            result += f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт.\n"
        return result

