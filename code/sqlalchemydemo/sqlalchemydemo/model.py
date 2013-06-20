from sqlalchemy import (
    Column,
    Integer,
    Text,
)
from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
)
from sqlalchemy.ext.declarative import declarative_base
from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(
    sessionmaker(extension=ZopeTransactionExtension())
)
Base = declarative_base()


class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True)
    title = Column(Text, unique=True)
    body = Column(Text)

    def __init__(self, title, body):
        self.title = title
        self.body = body
