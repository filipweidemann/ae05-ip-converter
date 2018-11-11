export default {
  ipRules: [
    v => !!v || 'IP is required',
    v => (v && v.length == 32) || 'IP adresses contain 32 bits.'
  ],
  tosRules: [
    v => !!v || 'TOS is required',
    v => (v.length > 0 && v.length <= 8) || 'TOS can only contain up to 8 bits'
  ],
  identifierRules: [
    v => !!v || 'Identifier is required',
    v => (v.length > 0 && v.length <= 16) || 'Identifier ca only contain up to 16 bits'
  ],
  ttlRules: [
    v => !!v || 'TTL field is required',
    v => (v.length > 0 && v.length <= 8) || 'TTL can only contain up to 8 bits'
  ],
  protocolRules: [
    v => !!v || 'Protocol is required',
    v => (v.length > 0 && v.length <= 8) || 'Protocol can only contain up to 8 bits'
  ],
  offsetRules: [
    v => !!v || 'Offset is required',
    v => (v.length > 0 && v.length <= 13) || 'Offset can only contain up to 13 bits'
  ],
}