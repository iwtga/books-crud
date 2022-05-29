from flask import jsonify, make_response, request
from bookscrud import db, app
from bookscrud.models import Books

@app.route('/books/createBook', methods=["POST"])
def create_book():
    content = request.json
    name = content['name']
    author = content['author']
    description = content['description']
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

@app.route('/books/<book_id>', methods=["PUT"])
def update_book(book_id):
    content = request.json
    book = Books.objects(book_id=book_id).first()
    if book:
        book.update(name = content["name"], author = content["author"], description = content["description"])
        return make_response("Book Updated Successfully!", 204)
    else:
        return make_response("Invalid Book", 400)

@app.route('/books/<book_id>', methods=["DELETE"])
def delete_book(book_id):
    book = Books.objects(book_id=book_id).first()
    if book:
        book.delete()
        return make_response("Book Deleted Successfully!", 204)
    else:
        return make_response("Book Invalid!", 400)