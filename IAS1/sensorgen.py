from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import random
  
# creating the flask app
app = Flask(__name__)
# creating an API object
api = Api(app)
    
# another resource to calculate the square of a number
class Sensor1(Resource):  
    def get(self):  
        return jsonify({'data': random.random()})
class Sensor2(Resource):  
    def get(self):  
        return jsonify({'data': random.random()})
class Sensor3(Resource):  
    def get(self):  
        return jsonify({'data': random.random()})
  
  
# adding the defined resources along with their corresponding urls

api.add_resource(Sensor1, '/sensor1')
api.add_resource(Sensor2, '/sensor2')
api.add_resource(Sensor3, '/sensor3')
  
# driver function
if __name__ == '__main__':
    app.run(port = 8080, debug = True)
