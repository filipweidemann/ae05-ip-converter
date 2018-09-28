import textwrap
from exceptions import InvalidIp, InvalidBinary, MissingFields
from flask import abort

class IPHeader:
    def __init__(
            self,
            version,
            tos,
            identifier,
            flags,
            offset,
            ttl,
            protocol,
            source,
            destination,
            binary
    ):
        self.version = version
        self.tos = tos
        self.identifier = identifier
        self.flags = flags
        self.offset = offset
        self.ttl = ttl
        self.protocol = protocol
        self.source = source
        self.destination = destination
        self.binary = binary
        self.checksum = ''
        self.ihl = ''
        self.packet_length = ''

    def validate_ip_fields(self):
        if self.binary:
            if len(self.source) == 32 and len(self.destination) == 32:
                return True
            raise InvalidBinary()

        else:
            source_tokens = self.source.split('.')
            destination_tokens = self.destination.split('.')

            source_token_count = len(source_tokens)
            destination_token_count = len(destination_tokens)

            if source_token_count != 4 or destination_token_count != 4:
                raise InvalidIp()

            for octet in source_tokens + destination_tokens:
                if int(octet) < 0 or int(octet) > 255:
                    raise InvalidIp()

            return True

    def calculate_checksum(self):
        header = self.get_binary_header()

        values = [value for key, value in header.items()]

        partial = bin(sum([int(value, 2) for value in values]))
        checksum_unflipped = partial[2:] + partial

        self.checksum = int(''.join('1' if x == '0' else '0' for x in str(checksum_unflipped)))

    def calculate_ihl(self):
        if self.binary:
            self.ihl = '5'

        else:
            self.ihl = '101'


    def calculate_packet_length(self):
        if self.binary:
            self.packet_length = '5'

        else:
            self.packet_length = '101'


    def convert_ip(self):
        addresses = {}
        try:
            if self.binary and self.validate_ip_fields():
                source_bytes = textwrap.wrap(self.source, 8)
                destination_bytes = textwrap.wrap(self.destination, 8)

                source_values = [str(int(byte, 2)) for byte in source_bytes]
                destination_values = [str(int(byte, 2)) for byte in destination_bytes]

                addresses['source'] = '.'.join(source_values)
                addresses['destination'] = '.'.join(destination_values)
                return addresses

            elif not self.binary and self.validate_ip_fields():
                addresses['source'] = ''.join([bin(int(x) + 256)[3:] for x in self.source.split('.')])
                addresses['destination'] = ''.join([bin(int(x) + 256)[3:] for x in self.destination.split('.')])
                return addresses
        except (InvalidBinary, InvalidIp):
            abort(400)

    def get_binary_header(self):
        header = {}

        if not self.binary:
            header['version'] = bin(int(self.version))[2:]
            header['tos'] = bin(int(self.tos))[2:]
            header['identifier'] = bin(int(self.identifier))[2:]
            header['flags'] = bin(int(self.flags, 2))[2:]
            header['offset'] = bin(int(self.offset))[2:]
            header['ttl'] = bin(int(self.ttl))[2:]
            header['protocol'] = bin(int(self.protocol))[2:]

            ip_addresses = self.convert_ip()
            header['source'] = ip_addresses['source']
            header['destination'] = ip_addresses['destination']

            return header

        if self.binary:
            header['version'] = self.version
            header['tos'] = self.tos
            header['identifier'] = self.identifier
            header['flags'] = self.flags[1:]
            header['offset'] = self.offset
            header['ttl'] = self.ttl
            header['protocol'] = self.protocol
            header['source'] = self.source
            header['destination'] = self.destination

            return header


    def convert(self):
        if self.binary:
            version = int(self.version, 2)
            tos = int(self.tos, 2)
            identifier = int(self.identifier, 2)
            flags = self.flags
            offset = int(self.offset, 2)
            ttl = int(self.ttl, 2)
            protocol = int(self.protocol, 2)

            ip_addresses = self.convert_ip()

            source = ip_addresses['source']
            destination = ip_addresses['destination']

            if not self.checksum:
                self.calculate_checksum()

            if not self.ihl:
                self.calculate_ihl()

            if not self.packet_length:
                self.calculate_packet_length()

            checksum = self.checksum
            ihl = self.ihl
            packet_length = self.packet_length

            header = IPHeader(
                version=version,
                tos=tos,
                identifier=identifier,
                flags=flags,
                offset=offset,
                ttl=ttl,
                protocol=protocol,
                source=source,
                destination=destination,
                binary=not self.binary
            )

            header.checksum = checksum
            header.ihl = ihl
            header.packet_length = packet_length

            return header

        elif not self.binary:
            version = bin(int(self.version))[2:]
            tos = bin(int(self.tos))[2:]
            identifier = bin(int(self.identifier))[2:]
            flags = self.flags
            offset = bin(int(self.offset))[2:]
            ttl = bin(int(self.ttl))[2:]
            protocol = bin(int(self.protocol))[2:]

            ip_addresses = self.convert_ip()

            source = ip_addresses['source']
            destination = ip_addresses['destination']

            if not self.checksum:
                self.calculate_checksum()

            if not self.ihl:
                self.calculate_ihl()

            if not self.packet_length:
                self.calculate_packet_length()

            checksum = self.checksum
            ihl = self.ihl
            packet_length = self.packet_length

            header = IPHeader(
                version=version,
                tos=tos,
                identifier=identifier,
                flags=flags,
                offset=offset,
                ttl=ttl,
                protocol=protocol,
                source=source,
                destination=destination,
                binary=not self.binary
            )

            header.checksum = checksum
            header.ihl = ihl
            header.packet_length = packet_length

            return header

    @classmethod
    def create(cls, data):
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