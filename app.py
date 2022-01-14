from flask import Flask, jsonify
import collections
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/test'
db = SQLAlchemy(app)

class hotelsModel(db.Model):
    __tablename__ = 'hotels_content'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), nullable=False)
    price = db.Column(db.Integer(), nullable=False)
    review = db.Column(db.String(), nullable=False)
    location = db.Column(db.String())
    amenities = db.Column(db.String(), nullable=False)
    image_link = db.Column(db.String(), nullable=False)

    # id        = db.Column(db.Integer, primary_key=True)
    # bookTitle = db.Column(db.String())
    # bookText  = db.Column(db.String(), nullable=False)
    # likes     = db.Column(db.Integer(), nullable=False, default=0)

    def __init__(self, id, title, price, review, location, amenities, image_link):
        self.id = id
        self.title = title
        self.price = price
        self.review = review
        self.location = location
        self.amenities = amenities
        self.image_link = image_link

    # def __init__(self, bookTitle, bookText, likes):
    #     self.bookTitle = bookTitle
    #     self.bookText = bookText
    #     self.likes = likes


@app.route('/test', methods=['GET'])
def test():
    return {
        'test': 'test1'
    }


@app.route('/hotels', methods=['GET'])
def getHotels():
    allHotels = hotelsModel.query.all()
    output = []
    for record in allHotels:
        d = {'id': record.id, 'title': record.title, 'price': record.price, 'review': record.review,
             'location': record.location, 'amenities': record.amenities, 'image_link': record.image_link}
        output.append(d)

    return jsonify(output)


if __name__ == '__main__':
    app.run(debug=True)
