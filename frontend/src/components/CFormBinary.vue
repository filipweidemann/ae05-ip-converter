<template>
  <div>
    <v-form ref="form" class="header-form" v-model="valid" lazy-validation>
      <v-text-field
        v-model="header.version"
        :counter="3"
        label="Version"
        required
        disabled
      ></v-text-field>

      <v-text-field
        v-model="header.tos"
        label="TOS"
        required
        disabled
      ></v-text-field>

      <v-text-field
        v-model="header.identifier"
        label="Kennung"
        required
        disabled
      ></v-text-field>

      <v-text-field
        v-model="header.flags"
        label="Flags"
        required
        disabled
      ></v-text-field>

      <v-text-field
        v-model="header.offset"
        label="Fragment Offset"
        required
        disabled
      ></v-text-field>

      <v-text-field
        v-model="header.ttl"
        label="TTL"
        required
        disabled
      ></v-text-field>

      <v-text-field
        v-model="header.protocol"
        label="Protokol"
        required
        disabled
      ></v-text-field>

      <v-text-field
        v-model="header.source"
        :rules="ipRules"
        :counter="32"
        label="Source IP"
        required
      ></v-text-field>

      <v-text-field
        v-model="header.destination"
        :rules="ipRules"
        :counter="32"
        label="Destination IP"
        required
      ></v-text-field>

      <v-text-field
        v-model="header.checksum"
        label="Checksum"
        disabled
      ></v-text-field>

      <v-btn
        :disabled="!valid"
        @click="submitForm"
      >
        Submit
      </v-btn>
    </v-form>
  </div>
</template>

<script>
import api from '@/api'

export default {
  name: 'CFormBinary',

  data () {
    return {
      valid: false,
      ipRules: [
        v => !!v || 'IP is required',
        v => (v && v.length == 32) || 'IP adresses contain 32 bits.'
      ],
      header: {
        version: '100',
        tos: '11000',
        identifier: '0',
        flags: '010',
        offset: '0',
        ttl: '10000000',
        protocol: '0',
        source: '',
        destination: '',
        checksum: ''
      } 
    }
  },

  methods: {
    submitForm () {
      this.$api.post('convert-to-string', this.header)
        .then(response => {
          console.log(response)
          this.$emit('converted', response.data)
        })
        .catch(err => {
          console.log(err)
        })
    },

    initializeData (data) {
      this.header.version = data.version
      this.header.tos = data.tos
      this.header.identifier = data.identifier
      this.header.flags = data.flags
      this.header.offset = data.offset
      this.header.ttl = data.ttl
      this.header.protocol = data.protocol
      this.header.source = data.source
      this.header.destination = data.destination
      this.header.checksum = data.checksum
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}

.header-form {
  width: 500px;
}
</style>
