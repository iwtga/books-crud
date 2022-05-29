import mongoengine as db
from dotenv import load_dotenv
import os

try:
    load_dotenv()
except:
    pass

database_name = "bookstore"
password = os.environ.get("PASSWORD")
DB_URI = f"mongodb+srv://alan:{password}@python-cluster.vuny8gs.mongodb.net/{database_name}?retryWrites=true&w=majority"
db.connect(host=DB_URI)

class Books(db.Document):
    book_id = db.IntField()
    name = db.StringField()
    author = db.StringField()

    def get_json(self):
        return {
            "book_id": self.book_id,
            "name": self.name,
            "author": self.author
        }

# b1 = Books(
#     book_id = 1,
#     name="Oliver Twist",
#     author="Charles Dickens"
# )

# b1.save()
book = Books.objects(book_id=1).first()
book.update(name="Harry Potter")
print(book.get_json())