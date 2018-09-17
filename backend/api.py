from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
from converter import convert_ip_to_binary, convert_ip_to_string, is_valid_ip_binary, \
    is_valid_ip_string, calculate_checksum, convert_basic_values, calculate_ihl

app = Flask(__name__)
api = Api(app)
CORS(app)

class ConvertToString(Resource):
    def post(self):
        form = request.get_json()
        converted = {}

        checksum = calculate_checksum(form, binary=True)
        converted = convert_basic_values(form, binary=True)

        converted['checksum'] = checksum

        return converted


class ConvertToBinary(Resource):
    def post(self):
        form = request.get_json()
        converted = {}

        checksum = calculate_checksum(form, binary=False)
        converted = convert_basic_values(form, binary=False)

        converted['checksum'] = checksum

        return converted


api.add_resource(ConvertToString, '/convert-to-string')
api.add_resource(ConvertToBinary, '/convert-to-binary')

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8000)
