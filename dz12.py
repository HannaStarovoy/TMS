from dataclasses import dataclass
from abc import ABC, abstractmethod
# 1
@dataclass
class Product:
    id : int
    name: str
    price: float

person = Product(122434, 'bag', 1050)

print(person.id)
print(person.name)
print(person.price)

# 2
@dataclass
class Pizza(Product):
    ingridients: list
    spicy: bool
    diameter: int

@dataclass
class Coffee(Product):
    size: int
    typecoffee: str

# 3
class AbstractShop(ABC):
    @abstractmethod
    def add_product(self, obj: Product):
        pass

    @abstractmethod
    def sell_product(self, obj: Product):
        pass

    @abstractmethod
    def all_products(self) -> list[Product]:
        pass
# 4
class NonProductError(ValueError):
    pass

class RealShop(AbstractShop):
    def __init__(self, productlist: list[Product]):
        self.productlist = productlist

    def is_valid(self, obj: Product) -> None:
        if not isinstance(obj, Product):
            raise NonProductError(f'переданый тип не является Product')

    def add_product(self, obj: Product) :
        self.is_valid(obj)
        self.productlist.append(obj)

    def sell_product(self, obj: Product):
        self.is_valid(obj)
        self.productlist.remove(obj)

    def all_products(self) -> list[Product]:
        return self.productlist


pizza = Pizza(54561, 'маргарита', 6.99, ['сыр','паста'], False, 17)
coffee = Coffee(1, 'coffe', 2.99, 400, 'americano')
coffee1 = Coffee(2, 'coffe1', 3.99, 450, 'capucino')
shop = RealShop([coffee, pizza])
print(shop.all_products())
shop.add_product(coffee1)
print(shop.all_products())
shop.sell_product(coffee1)
print(shop.all_products())

# 6. 7
@dataclass
class Furniture(Product):
    id: int
    name: str
    price: float

@dataclass
class Table(Furniture):
    diametr: float
    typetable: str

@dataclass
class Chair(Furniture):
    typechair: str

@dataclass
class Closet(Furniture):
    color: str

class FurnitureShop(AbstractShop):
    def __init__(self, productlist: list[Furniture]):
        self.productlist = productlist

    def add_product(self, obj: Furniture):
        if isinstance(obj, Furniture):
            self.productlist.append(obj)
        else:
            raise NonProductError('передаваемый продукт не является мебелью!')

    def sell_product(self, obj: Furniture):
        if isinstance(obj, Furniture):
            if sellproduct in self.productlist:
                self.productlist.remove(obj)
            else:
                print('отсутсвует')
        else:
            raise NonProductError('передаваемый продукт не является мебелью!')

    def all_products(self) -> list[Furniture]:
        return self.productlist
