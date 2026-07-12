from abc import ABC, abstractmethod
from typing import List, Any


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


class LoggingInitMixin:
    """Миксин для логирования создания объекта."""
    def __init__(self) -> None:
        # Логируем ПОСЛЕ того, как все атрибуты уже установлены в Product/наследнике
        cls_name = self.__class__.__name__

        # Собираем значимые атрибуты для лога (можно расширить при необходимости)
        parts = []
        if hasattr(self, "name"):
            parts.append(repr(self.name))
        if hasattr(self, "description"):
            parts.append(repr(self.description))
        if hasattr(self, "price"):
            parts.append(str(self.price))
        if hasattr(self, "quantity"):
            parts.append(str(self.quantity))

        params_str = ", ".join(parts)
        print(f"{cls_name}({params_str})")

        super().__init__()


class Product(LoggingInitMixin, BaseProduct):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
    ) -> None:
        # 1. Сначала устанавливаем атрибуты
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

        # 2. Потом вызываем миксин (он залогирует объект с уже заполненными полями)
        super().__init__()

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

    def get_name(self) -> str:
        return self.name

    def get_price(self) -> float:
        return self.price

    def describe(self) -> str:
        return f"{self.name}: {self.description}, цена {self.price}, кол-во {self.quantity}"

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: Any) -> float:
        if type(self) is not type(other):
            raise TypeError(
                "Можно складывать только объекты одного класса продуктов"
            )
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
        # Сначала инициализируем родителя (он установит базовые поля и вызовет миксин)
        super().__init__(name, description, price, quantity)

        # Потом добавляем специфичные поля
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def describe(self) -> str:
        base = super().describe()
        return f"{base}; смартфон: {self.model}, память {self.memory}, цвет {self.color}, эффективность {self.efficiency}"


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
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def describe(self) -> str:
        base = super().describe()
        return f"{base}; газонная трава: страна {self.country}, период прорастания {self.germination_period}, цвет {self.color}"


class Category:
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: List[Product]) -> None:
        self.name = name
        self.description = description

        for p in products:
            if not isinstance(p, Product):
                raise TypeError(
                    "В категорию можно добавлять только объекты Product "
                    "или его наследников"
                )
        self.__products: List[Product] = products

        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product: Product) -> None:
        if not isinstance(product, Product):
            raise TypeError(
                "В категорию можно добавлять только объекты Product "
                "или его наследников"
            )
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        return "\n".join(str(p) for p in self.__products)

    def __str__(self) -> str:
        total_quantity = sum(p.quantity for p in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."