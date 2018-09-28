from flask import Flask, request, abort
from flask_restful import Resource, Api
from flask_cors import CORS
from exceptions import MissingFields
from models import IPHeader
from helper import header_to_dict

app = Flask(__name__)
api = Api(app)
CORS(app)

class ConvertToString(Resource):
    def post(self):
        data = request.get_json()
        data['binary'] = True

        try:
            header = IPHeader.create(data)
        except MissingFields:
            abort(400)

        try:
            header.calculate_checksum()
            header.calculate_ihl()
            header.calculate_packet_length()

            converted = header.convert()
            header_final = header_to_dict(converted)
        except ValueError:
            abort(400)

        return header_final


class ConvertToBinary(Resource):
    def post(self):
        data = request.get_json()
        data['binary'] = False

        try:
            header = IPHeader.create(data)
        except MissingFields:
            abort(400)

        try:
            header.calculate_ihl()
            header.calculate_checksum()
            header.calculate_packet_length()

            converted = header.convert()
            header_final = header_to_dict(converted)
        except ValueError:
            abort(400)

        return header_final


api.add_resource(ConvertToString, '/convert-to-string')
api.add_resource(ConvertToBinary, '/convert-to-binary')

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8000)
