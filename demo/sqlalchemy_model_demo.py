from sqlalchemy import create_engine, String
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

with Session(engine) as session:
    user = User(name="Alice", age=25)
    session.add(user)
    session.commit()

with Session(engine) as session:
    user = session.query(User).filter_by(name="Alice").first()
    print(f"Found: {user.name}, Age: {user.age}")
