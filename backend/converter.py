import textwrap
from exceptions import InvalidIp, InvalidBinary


def convert_ip_to_binary(address):
    if not is_valid_ip_string(address):
        raise InvalidIp()

    return ''.join([bin(int(x) + 256)[3:] for x in address.split('.')])


def convert_ip_to_string(binary):
    if not is_valid_ip_binary(binary):
        raise InvalidBinary()

    bytes = textwrap.wrap(binary, 8)
    values = [str(int(byte, 2)) for byte in bytes]

    return '.'.join(values)

def convert_basic_values(header, binary=False):
    converted = {}

    for key, value in header.items():
        if key == 'source' or key == 'destination':
            if not binary:
                converted[key] = convert_ip_to_binary(header[key])
            else:
                converted[key] = convert_ip_to_string(header[key])
        else:
            if not binary:
                converted[key] = bin(int(value))[2:]
            else:
                converted[key] = int(value, 2)

    return converted


def is_valid_ip_string(address):
    tokens = address.split('.')
    if len(tokens) != 4:
        return False

    for token in tokens:
        if int(token) > 255:
            return False

    return True


def is_valid_ip_binary(binary):
    if len(binary) != 32:
        return False

    return True


def calculate_checksum(header, binary=False):
    bin_values = []

    if not binary:
        for key, value in header.items():
            if key == 'checksum':
                pass
            else:
                bin_values.append(bin(int(value)))
    else:
        for key, value in header.items():
            if key == 'checksum':
                pass
            else:
                bin_values.append(value)

    partial = bin(sum([int(value, 2) for value in bin_values]))
    checksum_unflipped = partial[2:] + partial
    return int(''.join('1' if x == '0' else '0' for x in str(checksum_unflipped)))


