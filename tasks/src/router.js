import Vue from 'vue'
import Router from 'vue-router'
import VueDemo from '@/components/VueDemo'
import Messages from '@/components/Messages'
import Patients from '@/components/PatientsList'
import Charts from '@/components/Charts'
import Netcdf from '@/components/Netcdf'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: VueDemo
    },
    {
      path: '/messages',
      name: 'messages',
      component: Messages
    },
    {
      path: '/patients',
      name: 'patients',
      component: Patients
    },
    {
      path: '/charts',
      name: 'charts',
      component: Charts
    },
    {
      path: '/netcdf',
      name: 'netcdf',
      component: Netcdf
    }
  ]
})
