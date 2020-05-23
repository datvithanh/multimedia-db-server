from flask import Flask
from flask_restful import reqparse, Resource, Api
from infer import infer
from search import findRestaurant
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)

parser = reqparse.RequestParser()
parser.add_argument('image')

class Predict(Resource):
    def post(self):
        args = parser.parse_args()

        try: 
            category = infer(args['image'])
            restaurants = findRestaurant(category)

            return {"restaurants": restaurants}
        except:
            return {"message": "something wrong happened, perhaps wrong base64 format"}

api.add_resource(Predict, '/predict')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
