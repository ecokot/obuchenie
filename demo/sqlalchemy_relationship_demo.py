from sqlalchemy import create_engine, String, ForeignKey, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, Session, joinedload

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__  = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    age: Mapped[int]
    posts: Mapped[list["Post"]] = relationship(back_populates="user")

class Post(Base):
    __tablename__ = "posts"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="posts")
engine = create_engine("sqlite:///demo.db", echo=True)

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

data_user = [
    ("Alice", 30),
    ("Bob", 25)
    ]
with Session(engine) as session:
    for name, age in data_user:
        user = User(name=name, age=age)
        session.add(user)
    session.commit()
data_post = [
    ("Post 1", 1),
    ("Post 2", 2),
    ("Post 3", 1),
    ("Post 4", 2),
    ("Post 5", 1)
]
with Session(engine) as session:
    for title, user_id in data_post:
        post = Post(title=title, user_id=user_id)
        session.add(post)
    session.commit()

with Session(engine) as session:
    stmt = select(User).where(User.id == 1)
    user = session.execute(stmt).scalar_one()
    for post in user.posts:
        print(user.name, post.title)

with Session(engine) as session:
    stmt = select(Post).where(Post.id == 1)
    post = session.execute(stmt).scalar_one()
    print(post.user.name)

with Session(engine) as session:
    stmt = select(User).options(joinedload(User.posts))
    users = session.execute(stmt).unique().scalars().all()
    for user in users:
        for post in user.posts:
            print(user.name, post.title)