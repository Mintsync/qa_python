import pytest


class TestBooksCollector:

    @pytest.mark.parametrize('name', [
        'Гордость и предубеждение и зомби',
        'Что делать, если ваш кот хочет вас убить',
        'А' * 40,
        'А',
    ])
    def test_add_new_book_added(self, collector, name):
        collector.add_new_book(name)
        assert name in collector.get_books_genre()

    @pytest.mark.parametrize('name', ['', 'А' * 41])
    def test_add_new_book_invalid_name_not_added(self, collector, name):
        collector.add_new_book(name)
        assert name not in collector.get_books_genre()

    def test_add_new_book_twice_not_duplicated(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize('name, genre', [
        ('Гордость и предубеждение и зомби', 'Фантастика'),
        ('Оно', 'Ужасы'),
        ('Шерлок Холмс', 'Детективы'),
        ('Вверх', 'Мультфильмы'),
        ('Маска', 'Комедии'),
    ])
    def test_set_book_genre_valid(self, collector, name, genre):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    def test_get_book_genre_of_existing_book_success(self, collector_with_books):
        assert collector_with_books.get_book_genre('Оно') == 'Ужасы'

    @pytest.mark.parametrize('genre, expected', [
        ('Фантастика', ['Гордость и предубеждение и зомби']),
        ('Ужасы', ['Оно']),
        ('Детективы', ['Шерлок Холмс']),
        ('Мультфильмы', ['Вверх']),
        ('Комедии', ['Маска']),
    ])
    def test_get_books_with_specific_genre_success(self, collector_with_books, genre, expected):
        assert collector_with_books.get_books_with_specific_genre(genre) == expected

    @pytest.mark.parametrize('name, genre, is_for_children', [
        ('Вверх', 'Мультфильмы', True),
        ('Маска', 'Комедии', True),
        ('Гордость и предубеждение и зомби', 'Фантастика', True),
        ('Оно', 'Ужасы', False),
        ('Шерлок Холмс', 'Детективы', False)
    ])
    def test_get_books_for_children_equals_flag(self, collector, name, genre, is_for_children):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        result = collector.get_books_for_children()
        assert (name in result) == is_for_children

    def test_add_book_in_favorites_success(self, collector):
        collector.add_new_book('Оно')
        collector.add_book_in_favorites('Оно')
        assert collector.get_list_of_favorites_books() == ['Оно']

    def test_delete_book_from_favorites_success(self, collector):
        collector.add_new_book('Оно')
        collector.add_book_in_favorites('Оно')
        collector.delete_book_from_favorites('Оно')
        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books_shows_multiple(self, collector_with_books):
        for name in ['Оно', 'Вверх', 'Маска']:
            collector_with_books.add_book_in_favorites(name)
        assert collector_with_books.get_list_of_favorites_books() == ['Оно', 'Вверх', 'Маска']
