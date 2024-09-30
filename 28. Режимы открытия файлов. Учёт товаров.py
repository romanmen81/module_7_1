class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"

class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        try:
            with open(self.__file_name, 'r') as file:
                return file.read().strip()  # Возвращаем строку без лишних пробелов в начале и конце
        except FileNotFoundError:
            return ""  # Файл не найден, возвращаем пустую строку

    def add(self, *products):
        existing_products = self.get_products().splitlines()

        for product in products:
            product_str = str(product)
            if product_str not in existing_products:
                with open(self.__file_name, 'a') as file:
                    file.write(f"{product}\n")  # Записываем продукт в файл
            else:
                print(f"Продукт {product} уже есть в магазине")

# Пример работы программы
if __name__ == "__main__":
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')

    print(p2)  # __str__

    # Первый запуск добавления товаров
    s1.add(p1, p2, p3)

    print(s1.get_products())