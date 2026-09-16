# qa_python

Тесты, реализованные для покрытия класса BooksCollector:
collector вынесен в фикстуру.
1) test_add_new_book_added - проверка добавления допустимых имён для книг; используется параметризация.
2) test_add_new_book_invalid_name_not_added - проверка, что невалидные имена не добавляются; используется параметризация.
3) test_add_new_book_twice_not_duplicated - проверка, что книгу с одним названием можно добавить только один раз.
4) test_set_book_genre_valid - проверка, что можно установить жанр книге; используется параметризация.
5) test_get_book_genre_of_existing_book_success - проверка, что можно получить жанр по книге; collector_with_books - фикстура.
6) test_get_books_with_specific_genre_success - проверка, что метод get_books_with_specific_genre по ключу жанра возвращает ожидаемые названия книг.
Используется параметризация и фикстура collector_with_books.
7) test_get_books_for_children_equals_flag - проверка, подходит ли жанр для детей; используется параметризация.
8) test_add_book_in_favorites_success - проверка, что книга добавляется в избранное.
9) test_delete_book_from_favorites_success - проверка, что книга удаляется из избранного.
10) test_get_list_of_favorites_books_shows_multiple - проверка получения списка избранных книг; используется фикстура collector_with_books.

С учётом параметризации реализовано 26 тестов.