<template>
  <div>
    <v-form ref="form" class="header-form" v-model="valid" lazy-validation>
      <v-text-field
        v-model="header.version"
        :counter="1"
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
        :counter="15"
        label="Source IP"
        required
      ></v-text-field>

      <v-text-field
        v-model="header.destination"
        :rules="ipRules"
        :counter="15"
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
        submit
      </v-btn>
    </v-form>
  </div>
</template>

<script>
import api from '@/api'

export default {
  name: 'CFormString',

  data () {
    return {
      valid: false,
      ipRules: [
        v => !!v || 'IP is required',
        v => (v && v.length <= 15 && v.length >= 7) || 'IP adresses have a maximum of 15 characters.'
      ],
      header: {
        version: '4',
        tos: '24',
        identifier: '0',
        flags: '010',
        offset: '0',
        ttl: '128',
        protocol: '0',
        source: '',
        destination: '',
        checksum: ''
      } 
    }
  },

  methods: {
    submitForm () {
      this.$api.post('convert-to-binary', this.header)
        .then(response => {
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
