import datetime
from sqlalchemy import Column, String, Boolean, DateTime, Integer
from crawler_app.data.modelbase import SqlAlchemyBase


class History(SqlAlchemyBase):
    __tablename__ = 'History'

    auto_id = Column(Integer, primary_key=True)
    user_id = Column(String, index=True, nullable=False)
    url = Column(String, nullable=False)
    search_type = Column(String, nullable=False)
    keyword = Column(String)
    created = Column(DateTime, default=datetime.datetime.now)
