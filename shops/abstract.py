from abc import ABC, abstractmethod

from .product import Product


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
