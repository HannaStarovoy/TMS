from dataclasses import dataclass

@dataclass
class Product:
    id : int
    name: str
    price: float

@dataclass
class Pizza(Product):
    ingridients: list
    spicy: bool
    diameter: int

@dataclass
class Coffee(Product):
    size: int
    typecoffee: str

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

@dataclass
class Book(Product):
    id: int
    name: str
    price: float

@dataclass
class Books(Book):
    title: str
    price: float
@dataclass
class Magazine(Book):
    title: str
    price: float

@dataclass
class Computer(Product):
    id: int
    name: str
    price: float

@dataclass
class Motherboard(Computer):
    title: str
    price: float

@dataclass
class VideoCard(Computer):
    title: str
    price: float

