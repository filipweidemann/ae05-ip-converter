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
          :counter="1"
          class="form__input"
          label="Version"
          required
          disabled
        ></v-text-field>

        <v-text-field
          v-model="header.tos"
          :rules="tosRules"
          class="form__input"
          label="TOS"
          required
        ></v-text-field>
      </div>

      <div class="header-form__column">
        <v-text-field
          v-model="header.identifier"
          :rules="identifierRules"
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
          :rules="offsetRules"
          class="form__input"
          label="Fragment Offset"
          required
        ></v-text-field>
      </div>

      <v-text-field
        v-model="header.ttl"
        :rules="ttlRules"
        class="form__input"
        label="TTL"
        required
      ></v-text-field>

      <v-text-field
        v-model="header.protocol"
        :rules="protocolRules"
        class="form__input"
        label="Protokol"
        required
      ></v-text-field>

      <div class="header-form__column">
        <v-text-field
          v-model="header.source"
          :rules="ipRules"
          :counter="15"
          class="form__input"
          label="Source IP"
          required
        ></v-text-field>

        <v-text-field
          v-model="header.destination"
          :rules="ipRules"
          :counter="15"
          class="form__input"
          label="Destination IP"
          required
        ></v-text-field>
      </div>

      <v-text-field
        v-model="header.checksum"
        class="form__input"
        label="Checksum"
        disabled
      ></v-text-field>

      <div class="header-form__column">
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
      </div>

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
import rules from '@/stringRules'

export default {
  name: 'CFormString',

  data () {
    return {
      valid: false,

      tosRules: rules.tosRules,
      identifierRules: rules.identifierRules,
      offsetRules: rules.offsetRules,
      ttlRules: rules.ttlRules,
      protocolRules: rules.protocolRules,
      ipRules: rules.ipRules,

      header: {
        version: '4',
        tos: '',
        identifier: '',
        flags: '010',
        offset: '',
        ttl: '',
        protocol: '',
        source: '',
        destination: '',
        checksum: '',
        ihl: '',
        packetLength: ''
      },
      alert: false
    }
  },

  methods: {
    submitForm () {
      this.alert = false

      if (!this.$refs.form.validate()) {
        return
      }

      this.$api.post('convert-to-binary', this.header)
        .then(response => {
          console.log(response.data)
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
