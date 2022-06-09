import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      component: () => import('../views/HomeView.vue')
    },
    {
      path: '/impressum',
      component: () => import('../views/ImpressumView.vue')
    },
    {
      path: '/kontakt',
      component: () => import('../views/KontaktView.vue')
    },
    {
      path: '/login',
      component: () => import('../views/LoginView.vue')
    },
    {
      path: '/kreuzen',
      component: () => import('../views/KreuzenView.vue'),
      children: [
        {
          path: '',
          component: () => import('../views/kreuzen/HomeView.vue')
        },
        {
          path: 'admin',
          component: ''
        }
      ]
    }
  ]
})

export default router
