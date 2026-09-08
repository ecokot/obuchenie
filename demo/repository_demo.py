from sqlalchemy.orm import Session
from sqlalchemy import select, delete, create_engine
from sqlalchemy_model_demo import User, Base

class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def create_user(self, name, age) -> User:
        user = User(name=name, age=age)
        self.session.add(user)
        self.session.commit()
        return user

    def get_by_id(self, id: int) -> User | None:
        return self.session.execute(select(User).where(User.id == id)).scalar_one_or_none()

    def get_by_name(self, name: str) -> User | None:
        return self.session.execute(select(User).where(User.name == name)).scalar_one_or_none()

    def delete(self, id: int) -> bool:
        res = self.session.execute(delete(User).where(User.id == id)).rowcount
        self.session.commit()
        return res > 0




engine = create_engine("sqlite:///demo.db", echo=False)
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

with Session(engine) as session:
    user_repo = UserRepository(session)

    print(user_repo.create_user('Alice', 25).id)
    print(user_repo.delete(1))
    print(user_repo.get_by_id(1))