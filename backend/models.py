import textwrap
from exceptions import InvalidIp, InvalidBinary

class IPv4Header:
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

            if source_token_count != 4 and destination_token_count != 4:
                raise InvalidIp()

            for octet in source_tokens + destination_tokens:
                if int(octet) < 0 or int(octet) > 255:
                    raise InvalidIp()

            return True

    def convert_ip(self):
        addresses = {}

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

            return {
                'version': version,
                'tos': tos,
                'identifier': identifier,
                'flags': flags,
                'offset': offset,
                'ttl': ttl,
                'protocol': protocol,
                'source': source,
                'destination': destination
            }

        elif not self.binary:
            version = bin(int(self.version))
            tos = bin(int(self.tos))
            identifier = bin(int(self.identifier))
            flags = self.flags
            offset = bin(int(self.offset))
            ttl = bin(int(self.ttl))
            protocol = bin(int(self.protocol))

            ip_addresses = self.convert_ip()

            source = ip_addresses['source']
            destination = ip_addresses['destination']

            return {
                'version': version[2:],
                'tos': tos[2:],
                'identifier': identifier[2:],
                'flags': flags,
                'offset': offset[2:],
                'ttl': ttl[2:],
                'protocol': protocol[2:],
                'source': source[2:],
                'destination': destination[2:]
            }


if __name__ == '__main__':
    header = IPv4Header(
        version='100',
        tos='1100101',
        identifier='0',
        flags='010',
        offset='0',
        ttl='10000000',
        protocol='0',
        source='00000001000000010000000100000001',
        destination='00000001000000010000000100000010',
        binary=True
    )

    converted = header.convert()
    print(converted)
