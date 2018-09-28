<template>
  <div>
    <v-alert
        v-model="alert"
        dismissible
        type="error"
        color="error"
      >
        Die eingegebenen Parameter sind nicht gültig.
    </v-alert>
    <v-form ref="form" class="header-form" v-model="valid" lazy-validation>
      <div class="header-form__column">
        <v-text-field
          v-model="header.version"
          :counter="3"
          class="form__input"
          label="Version"
          required
          disabled
        ></v-text-field>

        <v-text-field
          v-model="header.tos"
          :counter="8"
          class="form__input"
          label="TOS"
          required
        ></v-text-field>
      </div>

      <div class="header-form__column">
        <v-text-field
          v-model="header.identifier"
          :counter="16"
          class="form__input"
          label="Kennung"
          required
        ></v-text-field>

        <v-text-field
          v-model="header.flags"
          class="form__input"
          label="Flags"
          required
          disabled
        ></v-text-field>

        <v-text-field
          v-model="header.offset"
          :counter="13"
          class="form__input"
          label="Fragment Offset"
          required
        ></v-text-field>
      </div>

      <v-text-field
        v-model="header.ttl"
        :counter="8"
        class="form__input"
        label="TTL"
        required
      ></v-text-field>

      <v-text-field
        v-model="header.protocol"
        :counter="8"
        class="form__input"
        label="Protokol"
        required
      ></v-text-field>

      <v-text-field
        v-model="header.source"
        :rules="ipRules"
        :counter="32"
        class="form__input"
        label="Source IP"
        required
      ></v-text-field>

      <v-text-field
        v-model="header.destination"
        :rules="ipRules"
        :counter="32"
        class="form__input"
        label="Destination IP"
        required
      ></v-text-field>

      <v-text-field
        v-model="header.checksum"
        class="form__input"
        label="Checksum"
        disabled
      ></v-text-field>

      <v-text-field
        v-model="header.ihl"
        class="form__input"
        label="IHL"
        disabled
      ></v-text-field>

      <v-text-field
        v-model="header.packetLength"
        class="form__input"
        label="Packet Length"
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
      alert: false,
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
        checksum: '',
        ihl: '',
        packetLength: ''
      } 
    }
  },

  methods: {
    submitForm () {
      this.alert = false

      if (!this.$refs.form.validate()) {
        return
      }

      this.$api.post('convert-to-string', this.header)
        .then(response => {
          console.log(response)
          this.$emit('converted', response.data)
        })
        .catch(() => {
          this.alert = true
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
      this.header.ihl = data.ihl
      this.header.packetLength = data.packet_length
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

.header-form__column {
  display: flex;
  flex-direction: row;
  width: 500px;
}

.form__input {
  padding: 10px;
}
</style>
