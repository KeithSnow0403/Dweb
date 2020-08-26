import Vue from 'vue'
import VueRouter from 'vue-router'
import Router from 'vue-router';

Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'UserList',
    component: () => import('../views/UserList.vue')
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

//Uncaught (in promise) NavigationDuplicated {_name: "NavigationDuplicated"}的解决方法
const originalPush = Router.prototype.push;
Router.prototype.push = function push(location) {
  return originalPush.call(this, location).catch(err => err)
};

export default router
