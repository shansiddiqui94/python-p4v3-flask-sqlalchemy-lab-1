# server/app.py
#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Earthquake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)


@app.route('/')
def index():
    body = {'message': 'Flask SQLAlchemy Lab 1'}
    return make_response(body, 200)

# Add views here
#Earth View
@app.route('/earthquakes/<int:id>')
def earthView(id):
    body = Earthquake.query.filter(Earthquake.id == id).first() #query filter for my earthquake by id
        
    if body is None:
        return make_response({
           'message': f'Earthquake {id} not found.'
        }, 404)
    
    return make_response({
        'id': body.id,
        'location': body.location,
        'magnitude': body.magnitude,
        'year': body.year
    })

@app.route('/earthquakes/magnitude/<float:magnitude>')
def mag(magnitude):
    # Query the database to get all earthquakes with a magnitude greater than or equal to the specified magnitude
    earthquakes = Earthquake.query.filter(Earthquake.magnitude >= magnitude).all()

    # Construct a list containing the data for each matched earthquake
    quakes_data = [{
        'id': earthquake.id,
        'location': earthquake.location,
        'magnitude': earthquake.magnitude,
        'year': earthquake.year
    } for earthquake in earthquakes]

    # Construct the JSON response manually
    response_body = {
        'count': len(quakes_data),
        'quakes': quakes_data
    }

    # Return the response
    return make_response(response_body)



if __name__ == '__main__':
     app.run(port=5555, debug=True)
