from abc import ABC, abstractmethod
from typing import List


class LoggingMixin:
    def __init__(self, *args, **kwargs):
        # В момент вызова этого __init__ все атрибуты уже присвоены в Product.__init__,
        # поэтому repr(self) будет корректным.
        print(repr(self))
        super().__init__()


class BaseProduct(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_price(self) -> float:
        pass

    @abstractmethod
    def describe(self) -> str:
        pass


class Product(BaseProduct, LoggingMixin):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
    ) -> None:
        self.name = name
        self.description = description
        # Убрали __price (name mangling), теперь это обычное поле price
        self.price = price
        self.quantity = quantity
        # Вызываем дальше по цепочке наследования
        super().__init__()

    def __repr__(self) -> str:
        return f"Product({self.name!r}, {self.description!r}, {self.price}, {self.quantity})"

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    # Свойство для контроля цены (валидация при присваивании)
    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, new_price: float) -> None:
        if new_price > 0:
            self._price = new_price
        else:
            print("Цена не должна быть нулевая или отрицательная")

    def get_name(self) -> str:
        return self.name

    def get_price(self) -> float:
        return self._price

    def describe(self) -> str:
        return f"{self.name}: {self.description}"

    def __add__(self, other: object) -> float:
        # Складываем только объекты ТОЧНО того же класса
        if type(self) is not type(other):
            raise TypeError("Складывать можно только объекты одного типа продукта")
        if not isinstance(other, Product):
            return NotImplemented
        return (self.price * self.quantity) + (other.price * other.quantity)


class Smartphone(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
        # Передаём только то, что нужно Product
        super().__init__(name, description, price, quantity)

    def __repr__(self) -> str:
        # Теперь self.price работает без проблем
        return f"Smartphone({self.name!r}, {self.description!r}, {self.price}, {self.quantity})"

    def describe(self) -> str:
        base = super().describe()
        return f"{base}, модель: {self.model}, память: {self.memory} ГБ, цвет: {self.color}"


class LawnGrass(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        self.country = country
        self.germination_period = germination_period
        self.color = color
        super().__init__(name, description, price, quantity)

    def __repr__(self) -> str:
        return f"LawnGrass({self.name!r}, {self.description!r}, {self.price}, {self.quantity})"

    def describe(self) -> str:
        base = super().describe()
        # Добавляем фразу, чтобы тест test_describe_overridden_in_lawn_grass проходил
        return f"{base}, газонная трава, страна: {self.country}, период всхожести: {self.germination_period}"


class Category:
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: List[Product]) -> None:
        self.name = name
        self.description = description
        self._products: List[Product] = []

        Category.category_count += 1
        for p in products:
            self.add_product(p)

    def add_product(self, product: Product) -> None:
        if not isinstance(product, Product):
            raise TypeError("В категорию можно добавить только объект Product")
        self._products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        parts = [f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт." for p in self._products]
        return "; ".join(parts)

    @property
    def total_quantity(self) -> int:
        return sum(p.quantity for p in self._products)

    def __str__(self) -> str:
        return f"{self.name}, количество продуктов: {self.total_quantity} шт."