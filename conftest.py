import pytest
from main import BooksCollector


@pytest.fixture
def collector():
    return BooksCollector()


@pytest.fixture
def collector_with_books(collector):
    collector.add_new_book('Гордость и предубеждение и зомби')
    collector.add_new_book('Оно')
    collector.add_new_book('Шерлок Холмс')
    collector.add_new_book('Вверх')
    collector.add_new_book('Маска')
    collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
    collector.set_book_genre('Оно', 'Ужасы')
    collector.set_book_genre('Шерлок Холмс', 'Детективы')
    collector.set_book_genre('Вверх', 'Мультфильмы')
    collector.set_book_genre('Маска', 'Комедии')
    return collector
