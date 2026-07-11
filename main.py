from src.products import Product, Category

print("--- 1. Проверка класс-метода new_product() ---")
# Создаём товары через словарь (требование задания)
p1 = Product.new_product({
    "name": "Samsung Galaxy S23 Ultra",
    "description": "256GB, Серый цвет, 200MP камера",
    "price": 180000.0,
    "quantity": 5
})
p2 = Product.new_product({
    "name": "Iphone 15",
    "description": "512GB, Gray space",
    "price": 210000.0,
    "quantity": 8
})

print(f"Товар 1: {p1.name}, цена: {p1.price}")
print(f"Товар 2: {p2.name}, цена: {p2.price}")

print("\n--- 2. Проверка создания категории и метода add_product() ---")
category1 = Category("Смартфоны", "Смартфоны для удобной жизни", [])
# Добавляем товары по одному через специальный метод (требование задания)
category1.add_product(p1)
category1.add_product(p2)

# Проверка вывода через геттер (должен вернуть строку по шаблону)
print("Список товаров в категории:")
print(category1.products)  # Это строка, а не список!

print("\n--- 3. Проверка сеттера цены (валидное и невалидное значение) ---")
print(f"Старая цена {p1.name}: {p1.price}")
p1.price = 170000.0  # Корректное изменение
print(f"Новая цена: {p1.price}")

print("Попытка установить отрицательную цену:")
p1.price = -500.0    # Должно вывести сообщение об ошибке
print(f"Цена после попытки: {p1.price}")  # Должна остаться 170000.0

print("\n--- 4. Проверка счётчиков категорий и товаров ---")
# Создадим ещё одну категорию для проверки глобальных счётчиков
p3 = Product.new_product({"name": "Xiaomi Redmi Note 11", "description": "1024GB, Синий", "price": 31000.0, "quantity": 14})
category2 = Category("Бюджетные телефоны", "Доступные смартфоны", [p3])

print(f"Всего категорий: {Category.category_count}")
print(f"Всего товаров: {Category.product_count}")

print("\n--- 5. Проверка формата вывода геттера products ---")
output = category2.products
print("Формат вывода второй категории:")
print(output)