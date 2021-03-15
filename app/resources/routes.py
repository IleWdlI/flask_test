from .book import Book, CreateBook, BookList


def initialize_routes(api):
    api.add_resource(Book, '/book/<int:book_id>')
    api.add_resource(CreateBook, '/book')
    api.add_resource(BookList, '/books')
