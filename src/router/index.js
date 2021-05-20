import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/views/Home'
import Data from '@/views/Data'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '',
      name: 'Home',
      component: Home
    },
    {
      path: '/data',
      name: 'Data',
      component: Data
    }
  ]
})
