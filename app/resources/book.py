from flask_restful import Resource, reqparse
from ..models.book import BookModel


class Book(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("title", type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument("price", type=float, required=True, help="This field cannot be left blank!")

    def get(self, book_id):
        print(book_id)
        book = BookModel.find_by_id(book_id)
        if book:
            return book.json()
        return {'message': 'Item not found'}, 404

    def put(self, book_id):
        pass

    def delete(self, book_id):
        pass


class CreateBook(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("title", type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument("price", type=float, required=True, help="This field cannot be left blank!")

    def post(self):
        data = self.parser.parse_args()
        book = BookModel(**data)
        print(book)
        try:
            book.save_to_db()
            return {'book': book.json()}
        except:
            return {'message': 'An error occurred inserting the item.'}, 500


class BookList(Resource):
    def get(self):
        return {'books': [item.json() for item in BookModel.query.all()]}
