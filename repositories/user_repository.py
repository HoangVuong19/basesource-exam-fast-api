from models.user_model import User
from repositories.base_repository import BaseRepository
from sqlalchemy.orm import Session


class UserRepository(BaseRepository[User]):
    model = User

    def __init__(self, db_session: Session):
        super().__init__(db_session)

    def is_user_exists(self, email: str):
        user = self.get_by("email", email, unique=True)
        if user and user.del_flag:
            user = None
        return user
