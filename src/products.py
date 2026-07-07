from typing import List, Dict, Any


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
    def new_product(cls, data: Dict[str, Any]) -> "Product":
        return cls(
            name=data["name"],
            description=data.get("description", ""),
            price=data["price"],
            quantity=data["quantity"],
        )


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

    @property
    def products(self) -> str:
        # Это гарантированно укладывается в лимит длины строки и читается лучше
        return "\n".join(
            f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт."
            for p in self.__products
        )
