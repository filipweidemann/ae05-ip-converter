from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
from converter import convert_ip_to_binary, convert_ip_to_string, is_valid_ip_binary, \
    is_valid_ip_string, calculate_checksum, convert_basic_values
from models import IPHeader

app = Flask(__name__)
api = Api(app)
CORS(app)

class ConvertToString(Resource):
    def post(self):
        data = request.get_json()

        header = IPHeader(
            version=data['version'],
            tos=data['tos'],
            identifier=data['identifier'],
            flags=data['flags'],
            offset=data['offset'],
            ttl=data['ttl'],
            protocol=data['protocol'],
            source=data['source'],
            destination=data['destination'],
            binary=True
        )

        header.calculate_checksum()
        header.calculate_ihl()

        converted = header.convert()

        return {
            'version': converted.version,
            'tos': converted.tos,
            'identifier': converted.identifier,
            'flags': converted.flags,
            'offset': converted.offset,
            'ttl': converted.ttl,
            'protocol': converted.protocol,
            'source': converted.source,
            'destination': converted.destination,
            'ihl': converted.ihl,
            'checksum': str(converted.checksum),
            'packet_length': converted.packet_length,
            'binary': converted.binary
        }


class ConvertToBinary(Resource):
    def post(self):
        data = request.get_json()

        header = IPHeader(
            version=data['version'],
            tos=data['tos'],
            identifier=data['identifier'],
            flags=data['flags'],
            offset=data['offset'],
            ttl=data['ttl'],
            protocol=data['protocol'],
            source=data['source'],
            destination=data['destination'],
            binary=False
        )

        header.calculate_ihl()
        header.calculate_checksum()

        converted = header.convert()

        return {
            'version': converted.version,
            'tos': converted.tos,
            'identifier': converted.identifier,
            'flags': converted.flags,
            'offset': converted.offset,
            'ttl': converted.ttl,
            'protocol': converted.protocol,
            'source': converted.source,
            'destination': converted.destination,
            'ihl': converted.ihl,
            'checksum': str(converted.checksum),
            'packet_length': converted.packet_length,
            'binary': converted.binary
        }


api.add_resource(ConvertToString, '/convert-to-string')
api.add_resource(ConvertToBinary, '/convert-to-binary')

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8000)
