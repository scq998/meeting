import { createRouter, createWebHistory } from 'vue-router'
import MeetingRoom from '@/components/MeetingRoom.vue'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'MeetingRoom',
      component: MeetingRoom
    }
  ]
})

export default router