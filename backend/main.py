def calculate_checksum(header):
    bin_values = []

    for key, value in header.items():
        if key == 'checksum':
            pass
        else:
            bin_values.append(bin(int(value)))

    partial = bin(sum([int(value, 2) for value in bin_values]))
    checksum_unflipped = partial[2:] + partial
    return int(''.join('1' if x == '0' else '0' for x in str(checksum_unflipped)), 2)