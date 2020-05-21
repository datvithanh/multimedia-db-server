from flask import Flask
from flask_restful import reqparse, Resource, Api
from infer import infer

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('image')

class Predict(Resource):
    def post(self):
        args = parser.parse_args()

        try: 
            output = infer(args['image'])
            return {"name": output}
        except:
            return {"message": "something wrong happened, perhaps wrong base64 format"}

api.add_resource(Predict, '/predict')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
