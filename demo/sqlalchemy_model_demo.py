from sqlalchemy import create_engine, String, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    age: Mapped[int]

engine = create_engine("sqlite:///demo.db", echo=True)

Base.metadata.create_all(engine)
data = (
    ("Alice", 25),
    ("Bob", 30)
)
with Session(engine) as session:
    for name, age in data:
        user = User(name=name, age=age)
        session.add(user)
    session.commit()

with Session(engine) as session:
    stmt = select(User).where(User.age > 25)
    users = session.scalars(stmt).all() #
    for user in users:
        print(f"Found: {user.name}, Age: {user.age}")
