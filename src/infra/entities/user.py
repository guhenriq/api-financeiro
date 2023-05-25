from sqlalchemy import Column, Integer, String
from src.infra.config import Base


class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    
    def __repr__(self):
        return f'User(email={self.email}, password={self.password})'
