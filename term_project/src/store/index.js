import Vue from 'vue'
import Vuex from 'vuex'
import messages from './modules/messages'
import cars from './modules/cars'
import repairs from './modules/repairs'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    messages,
    cars,
    repairs
  }
})