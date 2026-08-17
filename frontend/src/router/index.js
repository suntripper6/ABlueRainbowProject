import { createRouter, createWebHistory } from 'vue-router'
import Home from '../components/Home.vue'
import AssistedLivingList from '../components/AssistedLivingList.vue'
import HomeHealthList from '../components/HomeHealthList.vue'
import SkilledNursingList from '../components/SkilledNursingList.vue'
import HospiceList from '../components/HospiceList.vue'
import FacilityDetail from '../components/FacilityDetail.vue'
import Feedback from '../components/Feedback.vue'
import AdminLogin from '../components/AdminLogin.vue'
import AdminFacilityCreate from '../components/AdminFacilityCreate.vue'
import AdminUsers from '../components/AdminUsers.vue'
import AdminAuditLogs from '../components/AdminAuditLogs.vue'
import { isAuthenticated } from '../auth'
import { getAssistedLivingDetail, getHomeHealthDetail, getSkilledNursingDetail, getHospiceDetail } from '../api'

const routes = [
  { path: '/', component: Home },
  { path: '/assistedliving', component: AssistedLivingList },
  { 
    path: '/assistedliving/:id', 
    component: FacilityDetail, 
    props: route => ({ kicker: 'Assisted Living', fetchData: getAssistedLivingDetail, id: route.params.id, resourcePath: 'assistedliving' }) 
  },
  { path: '/homehealth', component: HomeHealthList },
  { 
    path: '/homehealth/:id', 
    component: FacilityDetail, 
    props: route => ({ kicker: 'Home Health', fetchData: getHomeHealthDetail, id: route.params.id, resourcePath: 'homehealth' }) 
  },
  { path: '/skillednursing', component: SkilledNursingList },
  { 
    path: '/skillednursing/:id', 
    component: FacilityDetail, 
    props: route => ({ kicker: 'Skilled Nursing', fetchData: getSkilledNursingDetail, id: route.params.id, resourcePath: 'skillednursing' }) 
  },
  { path: '/hospice', component: HospiceList },
  { 
    path: '/hospice/:id', 
    component: FacilityDetail, 
    props: route => ({ kicker: 'Hospice Care', fetchData: getHospiceDetail, id: route.params.id, resourcePath: 'hospice' }) 
  },
  { path: '/feedback', component: Feedback },
  { path: '/login', component: AdminLogin },
  { path: '/admin/facilities/new', component: AdminFacilityCreate, meta: { requiresAuth: true } },
  { path: '/admin/users', component: AdminUsers, meta: { requiresAuth: true } },
  { path: '/admin/audit-logs', component: AdminAuditLogs, meta: { requiresAuth: true } },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

router.beforeEach((to) => {
  if (to.meta.requiresAuth && !isAuthenticated.value) {
    return {
      path: '/login',
      query: { redirect: to.fullPath },
    }
  }

  if (to.path === '/login' && isAuthenticated.value) {
    return '/'
  }

  return true
})

export default router
