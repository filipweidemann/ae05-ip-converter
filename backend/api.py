from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
from models import IPHeader
from factories import create_ip_header
from helper import header_to_dict

app = Flask(__name__)
api = Api(app)
CORS(app)

class ConvertToString(Resource):
    def post(self):
        data = request.get_json()
        data['binary'] = True

        header = create_ip_header(data)

        header.calculate_checksum()
        header.calculate_ihl()

        converted = header.convert()

        header_final = header_to_dict(converted)

        return header_final


class ConvertToBinary(Resource):
    def post(self):
        data = request.get_json()
        data['binary'] = False

        header = create_ip_header(data)

        header.calculate_ihl()
        header.calculate_checksum()

        converted = header.convert()

        header_final = header_to_dict(converted)

        return header_final


api.add_resource(ConvertToString, '/convert-to-string')
api.add_resource(ConvertToBinary, '/convert-to-binary')

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8000)
