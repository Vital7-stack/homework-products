from typing import List


class Product:
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
    ) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        if new_price > 0:
            self.__price = new_price
        else:
            print("Цена не должна быть нулевая или отрицательная")

    @classmethod
    def new_product(cls, data: dict) -> "Product":
        return cls(
            name=data["name"],
            description=data.get("description", ""),
            price=data["price"],
            quantity=data["quantity"],
        )

    # Задание 1: строковое представление Product
    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    # Задание 2: сложение двух продуктов (возвращает общую стоимость на складе)
    def __add__(self, other: "Product") -> float:
        if not isinstance(other, Product):
            return NotImplemented
        return (self.price * self.quantity) + (other.price * other.quantity)


class Category:
    category_count: int = 0
    product_count: int = 0

    def __init__(
        self,
        name: str,
        description: str,
        products: List[Product],
    ) -> None:
        self.name = name
        self.description = description
        self.__products: List[Product] = products

        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product: Product) -> None:
        self.__products.append(product)
        Category.product_count += 1

    # Оптимизированный геттер: теперь использует __str__ у Product
    @property
    def products(self) -> str:
        return "\n".join(str(p) for p in self.__products)

    # Задание 1: строковое представление Category
    def __str__(self) -> str:
        total_quantity = sum(p.quantity for p in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."
