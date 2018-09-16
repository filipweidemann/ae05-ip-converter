<template>
  <v-app>
    <v-toolbar
      app
    >
      <v-toolbar-title v-text="title"></v-toolbar-title>
    </v-toolbar>
    <v-content>
      <CConverter/>
    </v-content>
    <v-footer app>
      <span>&copy; 2018</span>
    </v-footer>
  </v-app>
</template>

<script>
import CConverter from './components/CConverter'

export default {
  name: 'App',
  components: {
    CConverter
  },
  data () {
    return {
      clipped: false,
      drawer: true,
      miniVariant: false,
      right: true,
      rightDrawer: false,
      title: 'AE05 - IP Converter'
    }
  }
}
</script>
