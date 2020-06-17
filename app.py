from flask import Flask, request
from flask_restful import reqparse, Resource, Api
from infer import infer, CLASS_NAMES
from search import findRestaurant
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)

parser = reqparse.RequestParser()
parser.add_argument('image')
parser.add_argument('category')

class Predict(Resource):
    def post(self):
        args = parser.parse_args()

        category = infer(args['image'])
        #404
        if category == -1:
            return {"restaurants": [], "message": "your image doesn't match any of the categories"}

        restaurants = findRestaurant(category)

        return {"restaurants": restaurants, "message": "success"}
        #except:
            #return {"message": "something wrong happened, perhaps wrong base64 format"}

class Search(Resource):
    def post(self):
        args = parser.parse_args()

        category = args['category']
    
        if category not in CLASS_NAMES:
            return {"restaurants": [], "message": "Our database doesn't contain info about category " + category}

        restaurants = list(findRestaurant(category))

        return {"restaurants": restaurants, "message": "success"}


api.add_resource(Predict, '/predict')
api.add_resource(Search, '/search')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
