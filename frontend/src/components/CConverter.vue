<template>
  <v-container fluid>
    <v-slide-y-transition mode="out-in">
      <v-layout column align-center>
        <v-form ref="form" v-model="valid" lazy-validation>

          <v-text-field
            v-model="version"
            :counter="1"
            label="Version"
            required
            disabled
          ></v-text-field>

          <v-text-field
            v-model="tos"
            label="TOS"
            required
            disabled
          ></v-text-field>

          <v-text-field
            v-model="source"
            :counter="15"
            label="Source IP"
            required
          ></v-text-field>

          <v-text-field
            v-model="destination"
            :counter="15"
            label="Destination IP"
            required
          ></v-text-field>
      
          <v-btn
            :disabled="!valid"
            @click="submitForm"
          >
            submit
          </v-btn>
          <v-btn @click="clear">clear</v-btn>
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
      valid: true,
      version: '4',
      tos: '24',
      source: '',
      destination: ''
    }
  },

  methods: {
    submitForm () {
      api.post('convert-to-binary', {

      })
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
