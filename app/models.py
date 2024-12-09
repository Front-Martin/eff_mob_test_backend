from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from .database import Base


class Authors(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True, autoincrement="auto", index=True)
    first_name = Column(String)
    last_name = Column(String)
    birthday = Column(DateTime)


class Books(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, autoincrement="auto", index=True)
    name = Column(String)
    description = Column(String)
    author_id = Column(Integer, ForeignKey('authors.id'))
    quantity = Column(Integer)


class Borrows(Base):
    __tablename__ = 'borrows'

    id = Column(Integer, primary_key=True, autoincrement="auto", index=True)
    book_id = Column(Integer, ForeignKey('books.id'))
    reader_name = Column(String)
    borrow_date = Column(DateTime)
    return_date = Column(DateTime)
