<template>
  <section class="page-shell page-shell--wide">
    <div class="page-intro">
      <p class="section-kicker">Admin Tools</p>
      <h1 class="page-title">Manage admin accounts</h1>
      <p class="page-subtitle">Create additional admins, rotate passwords, and deactivate accounts without returning to bootstrap secrets.</p>
    </div>

    <div class="panel form-panel mt-4">
      <div v-if="status.message" :class="['alert', `alert-${status.type}`]" role="alert">
        {{ status.message }}
      </div>

      <h2 class="h4 mb-3">Create admin user</h2>
      <form @submit.prevent="handleCreateUser" class="form-shell">
        <div class="row g-3">
          <div class="col-md-4">
            <label class="form-label">Username</label>
            <input v-model="createForm.username" class="form-control" type="text" required />
          </div>
          <div class="col-md-4">
            <label class="form-label">Display Name</label>
            <input v-model="createForm.display_name" class="form-control" type="text" required />
          </div>
          <div class="col-md-4">
            <label class="form-label">Password</label>
            <input v-model="createForm.password" class="form-control" type="password" minlength="8" required />
          </div>
        </div>

        <div class="d-flex gap-3 mt-4 flex-wrap">
          <button type="submit" class="btn btn-secondary" :disabled="createLoading">
            {{ createLoading ? 'Creating...' : 'Create Admin User' }}
          </button>
          <router-link class="btn btn-outline-secondary" to="/admin/facilities/new">Go to Facility Creation</router-link>
          <router-link class="btn btn-outline-secondary" to="/admin/audit-logs">View Audit Log</router-link>
        </div>
      </form>
    </div>

    <div class="panel table-panel mt-4">
      <div class="table-responsive">
        <table class="table app-table align-middle">
          <thead>
            <tr>
              <th>Username</th>
              <th>Display Name</th>
              <th>Status</th>
              <th>Created</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="adminUser in adminUsers" :key="adminUser.id">
              <td>{{ adminUser.username }}</td>
              <td>
                <input
                  v-model="adminUser.displayName"
                  class="form-control"
                  type="text"
                />
              </td>
              <td>
                <span :class="['badge', adminUser.isActive ? 'text-bg-success' : 'text-bg-secondary']">
                  {{ adminUser.isActive ? 'Active' : 'Inactive' }}
                </span>
              </td>
              <td>{{ formatDate(adminUser.createdAtUtc) }}</td>
              <td>
                <div class="d-flex flex-column gap-2">
                  <div class="d-flex gap-2 flex-wrap">
                    <button class="btn btn-sm btn-outline-secondary" type="button" @click="saveUser(adminUser)">
                      Save
                    </button>
                    <button class="btn btn-sm btn-outline-warning" type="button" @click="toggleActive(adminUser)">
                      {{ adminUser.isActive ? 'Deactivate' : 'Activate' }}
                    </button>
                  </div>
                  <div class="d-flex gap-2 flex-wrap">
                    <input
                      v-model="passwordDrafts[adminUser.id]"
                      class="form-control form-control-sm"
                      type="password"
                      minlength="8"
                      placeholder="New password"
                    />
                    <button class="btn btn-sm btn-outline-dark" type="button" @click="rotatePassword(adminUser)">
                      Rotate Password
                    </button>
                  </div>
                </div>
              </td>
            </tr>
            <tr v-if="adminUsers.length === 0">
              <td colSpan="5" class="empty-cell">
                <div class="table-empty-state">
                  <strong>No admin users found</strong>
                  <p>Create the first additional admin from the form above.</p>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </section>
</template>

<script setup>
import { onMounted, reactive, ref } from 'vue'
import { createAdminUser, getAdminUsers, rotateAdminUserPassword, updateAdminUser } from '../api'

const adminUsers = ref([])
const createLoading = ref(false)
const status = ref({ type: '', message: '' })
const passwordDrafts = reactive({})

const createForm = reactive({
  username: '',
  display_name: '',
  password: '',
})

const normalizeUser = (user) => ({
  id: user.id,
  username: user.username,
  displayName: user.display_name || user.displayName,
  isActive: user.is_active ?? user.isActive,
  createdAtUtc: user.created_at_utc || user.createdAtUtc,
})

const loadAdminUsers = async () => {
  const response = await getAdminUsers()
  adminUsers.value = response.data.map(normalizeUser)
}

const handleCreateUser = async () => {
  createLoading.value = true
  status.value = { type: '', message: '' }

  try {
    await createAdminUser(createForm)
    createForm.username = ''
    createForm.display_name = ''
    createForm.password = ''
    await loadAdminUsers()
    status.value = { type: 'success', message: 'Admin user created successfully.' }
  } catch (error) {
    status.value = {
      type: 'danger',
      message: error.response?.data?.message || 'Failed to create the admin user.',
    }
  } finally {
    createLoading.value = false
  }
}

const saveUser = async (adminUser) => {
  status.value = { type: '', message: '' }

  try {
    const response = await updateAdminUser(adminUser.id, {
      display_name: adminUser.displayName,
      is_active: adminUser.isActive,
    })
    Object.assign(adminUser, normalizeUser(response.data))
    status.value = { type: 'success', message: `Updated ${adminUser.username}.` }
  } catch (error) {
    status.value = {
      type: 'danger',
      message: error.response?.data?.message || `Failed to update ${adminUser.username}.`,
    }
  }
}

const toggleActive = async (adminUser) => {
  adminUser.isActive = !adminUser.isActive
  await saveUser(adminUser)
}

const rotatePassword = async (adminUser) => {
  status.value = { type: '', message: '' }
  const nextPassword = passwordDrafts[adminUser.id]

  if (!nextPassword || nextPassword.length < 8) {
    status.value = { type: 'danger', message: 'Password rotations require at least 8 characters.' }
    return
  }

  try {
    await rotateAdminUserPassword(adminUser.id, { password: nextPassword })
    passwordDrafts[adminUser.id] = ''
    status.value = { type: 'success', message: `Rotated password for ${adminUser.username}.` }
  } catch (error) {
    status.value = {
      type: 'danger',
      message: error.response?.data?.message || `Failed to rotate password for ${adminUser.username}.`,
    }
  }
}

const formatDate = (value) => new Date(value).toLocaleString()

onMounted(async () => {
  try {
    await loadAdminUsers()
  } catch {
    status.value = { type: 'danger', message: 'Failed to load admin users.' }
  }
})
</script>