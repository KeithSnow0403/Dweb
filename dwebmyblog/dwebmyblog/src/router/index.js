import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Django',
    component: () => import('../views/Django.vue')
  }, 
  {
    path: '/',
    name: 'VueCli',
    component: () => import('../views/Vuecli.vue')
  }, 
  {
    path: '/',
    name: 'Django',
    component: () => import('../views/Django.vue')
  }, 
  {
    path: '/',
    name: 'Django',
    component: () => import('../views/Django.vue')
  }, 
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
]

const router = new VueRouter({
  routes
})

export default router
