import Vue from 'vue'
import Router from 'vue-router'
import Main from '@/components/VueDemo'
import Details from '@/components/Details'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Main
    },
    {
      path: '/repair/:id',
      name: 'details',
      component: Details
    }
  ]
})
