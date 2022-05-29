from flask import Flask, make_response, request
import mongoengine as db
from dotenv import load_dotenv
import os

try:
    load_dotenv()
except:
    pass

dbusername = os.environ.get("USERNAME")
database_name = os.environ.get("DATABASE_NAME")
password = os.environ.get("PASSWORD")
DB_URI = f"mongodb+srv://{dbusername}:{password}@python-cluster.vuny8gs.mongodb.net/{database_name}?retryWrites=true&w=majority"
db.connect(host=DB_URI)

app = Flask(__name__)

from bookscrud import views, models