from sqlalchemy.orm import Session
from sqlalchemy import select, delete
from sqlalchemy_model_demo import User

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
        return self.session.execute(delete(User).where(User.id == id)).rowcount > 0