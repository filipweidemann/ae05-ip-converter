<template>
  <v-container fluid>
    <v-slide-y-transition mode="out-in">
      <v-layout column align-center>
        <v-form ref="form" v-model="valid" lazy-validation>

          <v-switch
            :label="`Binäre Eingabe: ${binaryInput.toString()}`"
            v-model="binaryInput"
          ></v-switch>

          <div v-if="!binaryInput">
            <v-text-field
              v-model="headerString.version"
              :counter="1"
              label="Version"
              required
              disabled
            ></v-text-field>

            <v-text-field
              v-model="headerString.tos"
              label="TOS"
              required
              disabled
            ></v-text-field>

            <v-text-field
              v-model="headerString.identifier"
              label="Kennung"
              required
              disabled
            ></v-text-field>

            <v-text-field
              v-model="headerString.flags"
              label="Flags"
              required
              disabled
            ></v-text-field>

            <v-text-field
              v-model="headerString.offset"
              label="Fragment Offset"
              required
              disabled
            ></v-text-field>

            <v-text-field
              v-model="headerString.ttl"
              label="TTL"
              required
              disabled
            ></v-text-field>

            <v-text-field
              v-model="headerString.protocol"
              label="Protokol"
              required
              disabled
            ></v-text-field>

            <v-text-field
              v-model="headerString.source"
              :rules="ipRules"
              :counter="15"
              label="Source IP"
              required
            ></v-text-field>

            <v-text-field
              v-model="headerString.destination"
              :rules="ipRules"
              :counter="15"
              label="Destination IP"
              required
            ></v-text-field>
          </div>
          
          <div v-if="binaryInput">
            <v-text-field
              v-model="headerBinary.version"
              :counter="3"
              label="Version"
              required
              disabled
            ></v-text-field>

            <v-text-field
              v-model="headerBinary.tos"
              label="TOS"
              required
              disabled
            ></v-text-field>

            <v-text-field
              v-model="headerBinary.identifier"
              label="Kennung"
              required
              disabled
            ></v-text-field>

            <v-text-field
              v-model="headerBinary.flags"
              label="Flags"
              required
              disabled
            ></v-text-field>

            <v-text-field
              v-model="headerBinary.offset"
              label="Fragment Offset"
              required
              disabled
            ></v-text-field>

            <v-text-field
              v-model="headerBinary.ttl"
              label="TTL"
              required
              disabled
            ></v-text-field>

            <v-text-field
              v-model="headerBinary.protocol"
              label="Protokol"
              required
              disabled
            ></v-text-field>

            <v-text-field
              v-model="headerBinary.source"
              :rules="ipRulesBinary"
              :counter="32"
              label="Source IP"
              required
            ></v-text-field>

            <v-text-field
              v-model="headerBinary.destination"
              :rules="ipRulesBinary"
              :counter="32"
              label="Destination IP"
              required
            ></v-text-field>
          </div>
        
          <v-btn
            :disabled="!valid"
            @click="submitForm"
          >
            submit
          </v-btn>
        </v-form>
      </v-layout>
    </v-slide-y-transition>
  </v-container>
</template>

<script>
import api from '@/api'

export default {
  name: 'CConverter',

  data () {
    return {
      ipRules: [
        v => !!v || 'IP is required',
        v => (v && v.length <= 15 && v.length >= 7) || 'IP adresses have a maximum of 15 characters.'
      ],
      ipRulesBinary: [
        v => !!v || 'IP is required',
        v => (v && v.length == 32) || 'IP adresses contain 32 bits.'
      ],
      valid: true,
      binaryInput: false,
      headerString: {
        version: '4',
        tos: '24',
        identifier: '0',
        flags: '010',
        offset: '0',
        ttl: '128',
        protocol: '0',
        source: '',
        destination: ''
      },
      headerBinary: {
        version: '100',
        tos: '11000',
        identifier: '0',
        flags: '010',
        offset: '0',
        ttl: '10000000',
        protocol: '0',
        source: '',
        destination: ''
      }
    }
  },

  methods: {
    submitForm () {
      let endpoint = this.binaryInput ? 'convert-to-string' : 'convert-to-binary'
      let payload = this.binaryInput ? this.headerBinary : this.headerString

      console.log(endpoint)

      api.post(endpoint, payload)
      .then(response => {
        console.log(response.data)
      })
      .catch(err => {
        console.log(err)
      })
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
</style>
