from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel, Field, field_validator, ValidationError


class AuthorBase(BaseModel):

    first_name: str = Field(..., min_length=2, max_length=32, description='Имя автора')
    last_name: str = Field(..., min_length=2, max_length=32, description='Фамилия автора')
    birthday: datetime = Field(..., description='Дата рождения автора')

    @field_validator('birthday')
    def validate_creation_datetime(self, value: datetime):
        if value and value.timestamp() > datetime.now().timestamp():
            raise ValidationError('Некорректная дата')

        return value


class AuthorCreate(AuthorBase):
    pass


class Author(AuthorBase):
    id: int

    class Config:
        orm_mode = True


class BookBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=32, description='Название книги')
    description: str = Field(..., min_length=2, max_length=256, description='Описание книги')
    author_id: int
    quantity: int = Field(..., gt=0, description='Количество доступных экземпляров книги')


class BookCreate(BookBase):
    pass


class Book(BookBase):
    id: int

    class Config:
        orm_mode = True


class BorrowBase(BaseModel):
    book_id: int
    reader_name: str = Field(..., min_length=2, max_length=32, description='Имя читателя')
    borrow_date: datetime = Field(..., description='Дата выдачи книги')
    return_date: datetime = Field(..., description='Дата возврата книги')

    @field_validator('borrow_date', 'return_date')
    def validate_creation_datetime(self, value: datetime, values: datetime):
        if (value and value.timestamp() > datetime.now().timestamp()) or value.timestamp() > values.timestamp():
            raise ValidationError('Некорректная дата')

        return value


class BorrowCreate(BorrowBase):
    pass


class Borrow(BorrowBase):
    id: int

    class Config:
        orm_mode = True
