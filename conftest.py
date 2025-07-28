import pytest
from main import BooksCollector

@pytest.fixture
def collection():
    return BooksCollector()

def pytest_make_parametrize_id(val):
    return repr(val)

@pytest.fixture
def collection_five_books(collection):
    books = ['Властелин колец', 'Король лев', 'Чужой', 'Сон в летнюю ночь', 'Молчание ягнят']
    genres = ['Фантастика', 'Мультфильмы', 'Ужасы', 'Комедии', 'Детективы']
    for book, genre in zip(books, genres):
        collection.add_new_book(book)
        collection.set_book_genre(book, genre)
    return collection
