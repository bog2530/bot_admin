from sqlalchemy import BigInteger, Column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Users(Base):
    __tablename__ = 'User'

    user_id = Column(BigInteger, unique=True, nullable=False, primary_key=True)
