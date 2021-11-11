from flask import Flask
from flask import request
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow.fields import Integer
from marshmallow import Schema

#init app
app = Flask(__name__)
#init marshmallow
ma = Marshmallow(app)

#For Database "BooksInfo_DB"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///BooksInfo_DB.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#calss for creating Database table
class Catalog_Server_DB(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(500))
    quantity = db.Column(db.Integer)
    price = db.Column(db.Float)
    topic = db.Column(db.String(500))
     

    def __init__(self,id,title,quantity,price,topic):
        self.id=id
        self.title=title
        self.quantity=quantity
        self.price=price
        self.topic=topic

#init marshmallow
ma = Marshmallow(app)
class Catalog_server_schema(Schema):
    class Meta:
        fields = ('id', 'title' , 'quantity' , 'price' , 'topic')

#init schema
book = Catalog_server_schema()
books = Catalog_server_schema(many=True)

#==================== info operations =====================================

#get all books information from the database
@app.route("/Bazar/info/all", methods=['GET'])
def get_info():
    books_db = Catalog_Server_DB.query.all()
    result = books.dump(books_db)
    return jsonify(result)


@app.route("/Bazar/info/<id>", methods=['GET'])
def get_info_forID(id):
    book_info = Catalog_Server_DB.query.with_entities(Catalog_Server_DB.title,Catalog_Server_DB.topic,Catalog_Server_DB.quantity,Catalog_Server_DB.price).filter_by(id = id).first()
    return book.jsonify(book_info)


