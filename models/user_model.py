import uuid

from sqlalchemy import Boolean, Column, String

from models.base_model import BaseModel


class User(BaseModel):
    __tablename__ = "users"

    id = Column(String(36), primary_key=True, default=uuid.uuid4)
    name = Column(String, unique=True, index=True, nullable=False)
    username = Column(String, nullable=False)
    mfa_enabled = Column(Boolean, nullable=True)
    del_flag = Column(Boolean, nullable=True)
