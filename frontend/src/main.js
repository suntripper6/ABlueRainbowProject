import { createApp } from 'vue'
import App from './App.vue'
import { initializeAuthSession } from './auth'
import router from './router'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.bundle.min.js'
import './index.css'
import './abr.css'

initializeAuthSession()

const app = createApp(App)
app.use(router)
app.mount('#root')
