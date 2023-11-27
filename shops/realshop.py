from .abstract import AbstractShop
from .product import Product, Furniture, Book, Computer

class RealShop(AbstractShop):
    def __init__(self, productlist: list[Product]):
        self.productlist = productlist

    def is_valid(self, obj: Product) -> None:
        if not isinstance(obj, Product):
            raise NonProductError(f'переданый тип не является Product')

    def add_product(self, obj: Product):
        self.is_valid(obj)
        self.productlist.append(obj)

    def sell_product(self, obj: Product):
        self.is_valid(obj)
        self.productlist.remove(obj)

    def all_products(self) -> list[Product]:
        return self.productlist

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

class BookShop(AbstractShop):
    def __init__(self, productlist: list[Book]):
        self.productlist = productlist

    def add_product(self, obj: Book):
        if isinstance(obj, Book):
            self.productlist.append(obj)
        else:
            raise NonProductError('передаваемый продукт не является мебелью!')

    def sell_product(self, obj: Book):
        if isinstance(obj, Book):
            if sellproduct in self.productlist:
                self.productlist.remove(obj)
            else:
                print('отсутсвует')
        else:
            raise NonProductError('передаваемый продукт не является мебелью!')

    def all_products(self) -> list[Book]:
        return self.productlist

class ComputerShop(AbstractShop):
    def __init__(self, productlist: list[Computer]):
        self.productlist = productlist

    def add_product(self, obj: Computer):
        if isinstance(obj, Computer):
            self.productlist.append(obj)
        else:
            raise NonProductError('передаваемый продукт не является мебелью!')

    def sell_product(self, obj: Computer):
        if isinstance(obj, Computer):
            if sellproduct in self.productlist:
                self.productlist.remove(obj)
            else:
                print('отсутсвует')
        else:
            raise NonProductError('передаваемый продукт не является мебелью!')

    def all_products(self) -> list[Computer]:
        return self.productlist
