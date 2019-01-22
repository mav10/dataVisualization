import Vue from 'vue'
import Vuex from 'vuex'
import messages from './modules/messages'
import patients from './modules/patient'
import charts from './modules/charts'
import netcdf from './modules/netcdf'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    messages,
    patients,
    charts,
    netcdf
  }
})