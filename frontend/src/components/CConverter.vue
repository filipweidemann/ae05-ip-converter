<template>
  <v-container fluid>
    <v-slide-y-transition mode="out-in">
      <v-layout column align-center>
    
          <v-switch
            label="Binäre Eingabe"
            v-model="binaryInput"
          ></v-switch>

          <div v-if="!binaryInput">
            <c-form-string @converted="displayResponse"/>
          </div>
          
          <div v-else-if="binaryInput">
            <c-form-binary @converted="displayResponse"/>
          </div>

          {{ response }}

      </v-layout>
    </v-slide-y-transition>
  </v-container>
</template>

<script>
import api from '@/api'
import CFormString from '@/components/CFormString'
import CFormBinary from '@/components/CFormBinary'

export default {
  name: 'CConverter',

  components: {
    CFormString,
    CFormBinary
  },

  data () {
    return {
      binaryInput: false,
      response: null
    }
  },

  methods: {
    displayResponse (response) {
      let stringified = `${response.version} - ${response.ihl} - ${response.tos} - ${response.packet_length} - ${response.flags} - ${response.offset} - ${response.ttl}`
      this.response = stringified
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
