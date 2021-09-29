from sqlalchemy import Column, BigInteger, String, sql

from database.database import TimedBaseModel


class User(TimedBaseModel):
    __tablename__ = 'users'

    id = Column(BigInteger, primary_key=True)
    username = Column(String(100))

    query: sql.Select
