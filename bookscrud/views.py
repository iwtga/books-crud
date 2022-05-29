from flask import jsonify, make_response, request
from bookscrud import db, app
from bookscrud.models import Books

@app.route('/books/createBook', methods=["POST"])
def create_book():
    name = request.json['name']
    author = request.json['author']
    description = request.json['description']
    book = Books(
        name = name,
        author = author,
        description = description
    )
    book.save()
    return make_response("Book Created!", 201)

@app.route('/books')
def read_book():
    books = []
    for book in Books.objects:
        books.append(book.get_json())
    return make_response(jsonify(books), 200)
