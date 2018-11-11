export default {
  ipRules: [
    v => !!v || 'IP is required',
    v => (v && v.length <= 15 && v.length >= 7) || 'IP adresses have a maximum of 15 characters.'
  ],
  tosRules: [
    v => !!v || 'TOS is required',
    v => (v <= 256 && v >= 0) || 'TOS field needs to be between 0 and 256'
  ],
  identifierRules: [
    v => !!v || 'Identifier is required',
    v => (v <= 65536 && v >= 0) || 'Identifier field needs to be between 0 and 65536'
  ],
  ttlRules: [
    v => !!v || 'TTL field is required',
    v => (v <= 256 && v >= 0) || 'TTL needs to be between 0 and 256'
  ],
  protocolRules: [
    v => !!v || 'Protocol is required',
    v => (v <= 256 && v >= 0) || 'Protocol needs to be between 0 and 256'
  ],
  offsetRules: [
    v => !!v || 'Offset is required',
    v => (v <= 8192 && v >= 0) || 'Offset needs to be between 0 and 8192'
  ],
}