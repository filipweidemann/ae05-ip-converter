import '@babel/polyfill'
import Vue from 'vue'
import './plugins/vuetify'
import App from './App.vue'
import api from '@/api'

Vue.config.productionTip = false

Vue.prototype.$api = api

new Vue({
  render: h => h(App)
}).$mount('#app')
