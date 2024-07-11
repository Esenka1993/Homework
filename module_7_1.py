from pprint import pprint
class Product:

    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}.'

class Shop:

    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        products_str = file.read()
        file.close()
        return products_str


    def add(self, *products):
        existing_products = self.get_products().split('\n')
        for i in products:
            if i.name not in [p.split(' - ')[0] for p in existing_products]:
                with open(self.__file_name, 'a') as file:
                    file.write(f"{i}\n")
                    existing_products.append(i)
            if i.name in [p.split(' - ')[0] for p in existing_products]:
                print(f'Продукт {i.name} есть в магазине')

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
print(p2)
s1.add(p1, p2, p3)
print(s1.get_products())
