from sqlalchemy import Column, BigInteger, String, ARRAY, sql

from database.database import TimedBaseModel


class Percent(TimedBaseModel):
    __tablename__ = 'percent'

    id = Column(BigInteger, primary_key=True)
    percents = Column(ARRAY(String(100)))

    query: sql.Select
