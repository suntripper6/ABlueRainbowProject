<template>
  <section class="page-shell">
    <div class="page-intro">
      <p class="section-kicker">Admin Access</p>
      <h1 class="page-title">Sign in to manage facility records</h1>
      <p class="page-subtitle">Use a persisted admin account to create, edit, or remove facility records.</p>
    </div>

    <div class="panel form-panel mt-4">
      <div v-if="status.message" :class="['alert', `alert-${status.type}`]" role="alert">
        {{ status.message }}
      </div>

      <form @submit.prevent="handleSubmit" class="form-shell">
        <div class="mb-4">
          <label class="form-label">Username</label>
          <input
            v-model="form.username"
            type="text"
            class="form-control"
            autocomplete="username"
            required
          />
        </div>

        <div class="mb-4">
          <label class="form-label">Password</label>
          <input
            v-model="form.password"
            type="password"
            class="form-control"
            autocomplete="current-password"
            required
          />
        </div>

        <div class="d-flex gap-3 flex-wrap align-items-center">
          <button type="submit" class="btn btn-secondary" :disabled="loading">
            <span v-if="loading" class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>
            <span v-else>Sign In</span>
          </button>
          <span v-if="isAuthenticated" class="text-muted">Signed in as {{ authState.username }}</span>
        </div>
      </form>
    </div>
  </section>
</template>

<script setup>
import { reactive, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { loginAdmin } from '../api'
import { authState, isAuthenticated, setAuthSession } from '../auth'

const router = useRouter()
const route = useRoute()

const form = reactive({
  username: '',
  password: '',
})
const loading = ref(false)
const status = ref({ type: '', message: '' })

const handleSubmit = async () => {
  loading.value = true
  status.value = { type: '', message: '' }

  try {
    const response = await loginAdmin(form)
    setAuthSession(response.data)
    status.value = { type: 'success', message: 'Signed in successfully.' }
    const redirectPath = typeof route.query.redirect === 'string' ? route.query.redirect : '/'
    await router.push(redirectPath)
  } catch {
    status.value = { type: 'danger', message: 'Sign in failed. Check your credentials.' }
  } finally {
    loading.value = false
  }
}
</script>