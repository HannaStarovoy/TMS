from sqlalchemy import Column, Integer, String,  ForeignKey, select
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker, relationship, DeclarativeBase

dsn = "sqlite:///dz15.db"

engine = create_engine(dsn, echo=True)
session = sessionmaker(bind=engine, autoflush=False)

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(64), unique=True, nullable=False)
    password = Column(String(64), nullable=False)
    email = Column(String(200), unique=True, nullable=False)

    orders = relationship("Orders", back_populates="users")

    def __str__(self):
        return f"User: {self.username}"

class Seller(Base):
    __tablename__ = "sellers"
    id = Column(Integer, primary_key=True, autoincrement=True)
    company = Column(String(64), unique=True, nullable=False)
    phone = Column(String(64), unique=True, nullable=False)

    products = relationship("Products", back_populates="sellers")
class Products(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64), unique=True, nullable=False)
    cost = Column(Integer, unique=False, nullable=False)
    count = Column(Integer, unique=False, nullable=False, default=0)
    seller_id = Column(Integer, ForeignKey("sellers.id"))

    orders = relationship("Orders", back_populates="products")
    seller = relationship("Seller", back_populates="products")


class Orders(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, autoincrement=True)
    count = Column(Integer, nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"))
    user_id = Column(Integer, ForeignKey("users.id"))

    product = relationship("Products", back_populates="orders")
    user = relationship("User", back_populates="orders")


def create_tables():
    Base.metadata.create_all(engine)

def drop_tables():
    Base.metadata.drop_all(engine)

def add_users(connection):
    user = User(username="hanna", password="<PASSWORD>", email="hanna@mail.com")
    connection.add(user)
    connection.add(User(username="hanna", password="<PASSWORD>", email="hanna@mail.com"))
    connection.add(User(username="kate", password="<PASSWORD>", email="kate@mail.com"))
    connection.add(User(username="tom", password="<PASSWORD>", email="tom@mail.com"))

    connection.commit()

def add_sellers(connection):
    connection.add(Seller(company="A", phone='335826'))
    connection.add(Seller(company="B", phone='223987'))
    connection.add(Seller(company="C", phone='478593'))

    connection.commit()

def add_products(connection):
    connection.add(Products(name="phone", cost=100, count=10, seller_id=1))
    connection.add(Products(name="computer", cost=200, count=20, seller_id=2))
    connection.add(Products(name="tv", cost=300, count=30, seller_id=3))

    connection.commit()

def create_order(connection, user: User, product: Products):
    order = Orders(user_id=user.id, product_id=product.id)
    connection.add(order)
    connection.commit()


def show_user_orders(connection, username: str):
    query = (
        select(User.username, Products.name)
        .join(User.orders)
        .join(Orders.product)
        .where(User.username == username)
    )

    res = connection.execute(query)

    for line in res:
        print("-" * 20, line)

drop_tables()
create_tables()

with session() as conn:
    add_users(conn)
    add_sellers(conn)
    add_products(conn)

    query = select(User)

    users = conn.execute(query).scalars()


    for user in users:
        print(user.username, user.email)

    query = select(User).where(User.username == "hanna")

    user = conn.execute(query).scalars().one()

    query = select(Products).where(Products.name == "phone")
    product = conn.execute(query).scalars().one()

    create_order(conn, user, product)

    print("=" * 20)
    print("START show_user_orders_opt")


    show_user_orders(conn, "hanna")