from models import IPHeader
from exceptions import MissingFields

def create_ip_header(data):
    required_fields = [
        'version',
        'tos',
        'identifier',
        'flags',
        'offset',
        'ttl',
        'protocol',
        'source',
        'destination',
        'binary'
    ]

    for key in required_fields:
        if not key in list(data.keys()):
            raise MissingFields()

    return IPHeader(
            version=data['version'],
            tos=data['tos'],
            identifier=data['identifier'],
            flags=data['flags'],
            offset=data['offset'],
            ttl=data['ttl'],
            protocol=data['protocol'],
            source=data['source'],
            destination=data['destination'],
            binary=data['binary']
        )