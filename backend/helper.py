def header_to_dict(header):
    if not header.checksum or not header.ihl:
        raise Exception()

    return {
        'version': header.version,
        'tos': header.tos,
        'identifier': header.identifier,
        'flags': header.flags,
        'offset': header.offset,
        'ttl': header.ttl,
        'protocol': header.protocol,
        'source': header.source,
        'destination': header.destination,
        'ihl': header.ihl,
        'checksum': str(header.checksum),
        'packet_length': header.packet_length,
        'binary': header.binary
    }