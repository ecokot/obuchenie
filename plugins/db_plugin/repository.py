from .models import User
from sqlalchemy import select

class UserRepository:
    def __init__(self, session_factory):
        self.session_factory = session_factory

    def create_user(self, username, password_hash):
        with self.session_factory() as session:
            user = User(username=username, password_hash=password_hash)
            session.add(user)
            session.commit()
            return user

    def find_by_username(self, username) -> User | None:
        with self.session_factory() as session:
            stmt = select(User).where(User.username == username)
            result = session.execute(stmt)
            return result.scalar_one_or_none()