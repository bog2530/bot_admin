from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from ..config import url
from .models import Base, Users

engine = create_engine(url, echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)


async def check_admin(id):
    if Users.query.get(Users.user_id == id) is not None:
        return True
    return False

