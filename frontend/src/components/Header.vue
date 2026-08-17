<template>
  <header class="site-header">
    <nav class="navbar navbar-expand-lg navbar-dark site-nav">
      <div class="container-fluid px-0">
        <router-link class="navbar-brand brand-mark" to="/">A Blue Rainbow</router-link>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#mynavbar">
          <span class="navbar-toggler-icon"></span>
        </button>
        
        <div class="collapse navbar-collapse" id="mynavbar">
          <ul class="navbar-nav me-auto">
            <li class="nav-item">
              <router-link class="nav-link" to="/">Home</router-link>
            </li>
            <li class="nav-item dropdown">
              <a 
                class="nav-link dropdown-toggle" 
                href="#" 
                role="button" 
                data-bs-toggle="dropdown" 
                aria-expanded="false"
              >
                Resources
              </a>
              <ul class="dropdown-menu">
                <li><router-link class="dropdown-item" to="/assistedliving">Assisted Living</router-link></li>
                <li><router-link class="dropdown-item" to="/homehealth">Home Health Care</router-link></li>
                <li><router-link class="dropdown-item" to="/skillednursing">Skilled Nursing</router-link></li>
                <li><router-link class="dropdown-item" to="/hospice">Hospice</router-link></li>
              </ul>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/feedback">Feedback</router-link>
            </li>
          </ul>
          
          <div class="d-flex align-items-center gap-3 flex-column flex-lg-row ms-lg-auto">
            <form class="d-flex top-search" action="/search" method="GET">
              <input 
                type="search" 
                class="form-control" 
                aria-label="Search" 
                placeholder="Search facilities by name" 
                name="q" 
              />
              <button class="btn btn-outline-secondary" type="submit">Search</button>
            </form>
            
            <div class="d-flex align-items-center gap-2">
              <router-link v-if="isAuthenticated" class="btn btn-light" to="/admin/facilities/new">Add Facility</router-link>
              <router-link v-if="isAuthenticated" class="btn btn-outline-light" to="/admin/users">Manage Admins</router-link>
              <router-link v-if="isAuthenticated" class="btn btn-outline-light" to="/admin/audit-logs">Audit Log</router-link>
              <span v-if="isAuthenticated" class="text-white-50 small">{{ authState.username }}</span>
              <button v-if="isAuthenticated" class="btn btn-outline-light" type="button" @click="handleLogout">Logout</button>
              <router-link v-else class="btn btn-outline-light" to="/login">Admin Login</router-link>
            </div>
          </div>
        </div>
      </div>
    </nav>
  </header>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { authState, clearAuthSession, isAuthenticated } from '../auth'

const router = useRouter()

const handleLogout = async () => {
  clearAuthSession()
  await router.push('/')
}
</script>
