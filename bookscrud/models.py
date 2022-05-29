from bookscrud import db

class Books(db.Document):
    book_id = db.SequenceField(primary_key=True)
    name = db.StringField()
    author = db.StringField()
    description = db.StringField()

    def get_json(self):
        return {
            "book_id": self.book_id,
            "name": self.name,
            "author": self.author,
            "description": self.description
        }
    