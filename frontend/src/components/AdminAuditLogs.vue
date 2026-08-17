<template>
  <section class="page-shell page-shell--wide">
    <div class="page-intro">
      <p class="section-kicker">Admin Tools</p>
      <h1 class="page-title">Audit log</h1>
      <p class="page-subtitle">Review recent admin sign-ins, facility mutations, and admin-account changes.</p>
    </div>

    <div class="panel form-panel mt-4">
      <div class="row g-3 align-items-end">
        <div class="col-md-2">
          <label class="form-label">Entries</label>
          <select v-model.number="take" class="form-select">
            <option :value="25">25</option>
            <option :value="50">50</option>
            <option :value="100">100</option>
          </select>
        </div>
        <div class="col-md-3">
          <label class="form-label">Actor</label>
          <input v-model="filters.actorUsername" class="form-control" type="text" placeholder="admin username" />
        </div>
        <div class="col-md-3">
          <label class="form-label">Action Type</label>
          <select v-model="filters.actionType" class="form-select">
            <option value="">All actions</option>
            <option v-for="action in actionOptions" :key="action" :value="action">{{ action }}</option>
          </select>
        </div>
        <div class="col-md-2">
          <label class="form-label">From</label>
          <input v-model="filters.occurredAfter" class="form-control" type="datetime-local" />
        </div>
        <div class="col-md-2">
          <label class="form-label">To</label>
          <input v-model="filters.occurredBefore" class="form-control" type="datetime-local" />
        </div>
      </div>

      <div class="d-flex gap-3 align-items-end flex-wrap mt-3">
        <button class="btn btn-secondary" type="button" :disabled="loading" @click="loadLogs">
          {{ loading ? 'Refreshing...' : 'Apply Filters' }}
        </button>
        <button class="btn btn-outline-secondary" type="button" :disabled="loading" @click="resetFilters">
          Reset
        </button>
        <button class="btn btn-outline-dark" type="button" :disabled="loading" @click="downloadCsv">
          Export CSV
        </button>
      </div>

      <div v-if="status.message" :class="['alert', `alert-${status.type}`, 'mt-3']" role="alert">
        {{ status.message }}
      </div>
    </div>

    <div class="panel table-panel mt-4">
      <div class="table-responsive">
        <table class="table app-table align-middle">
          <thead>
            <tr>
              <th>Time</th>
              <th>Actor</th>
              <th>Action</th>
              <th>Entity</th>
              <th>Description</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="log in logs" :key="log.id">
              <td>{{ formatDate(log.occurred_at_utc || log.occurredAtUtc) }}</td>
              <td>{{ log.actor_username || log.actorUsername }}</td>
              <td><code>{{ log.action_type || log.actionType }}</code></td>
              <td>{{ formatEntity(log) }}</td>
              <td>
                <div>{{ log.description }}</div>
                <small v-if="log.metadata_json || log.metadataJson" class="text-muted d-block mt-1">
                  {{ log.metadata_json || log.metadataJson }}
                </small>
              </td>
            </tr>
            <tr v-if="logs.length === 0">
              <td colSpan="5" class="empty-cell">
                <div class="table-empty-state">
                  <strong>No audit entries found</strong>
                  <p>Refresh after performing an admin action.</p>
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
import { exportAdminAuditLogs, getAdminAuditLogs } from '../api'

const take = ref(50)
const loading = ref(false)
const logs = ref([])
const status = ref({ type: '', message: '' })
const actionOptions = [
  'admin_user.login',
  'admin_user.created',
  'admin_user.updated',
  'admin_user.password_rotated',
  'facility.created',
  'facility.updated',
  'facility.deleted',
]
const filters = reactive({
  actorUsername: '',
  actionType: '',
  occurredAfter: '',
  occurredBefore: '',
})

const buildParams = () => ({
  take: take.value,
  actor_username: filters.actorUsername || undefined,
  action_type: filters.actionType || undefined,
  occurred_after_utc: toIso(filters.occurredAfter),
  occurred_before_utc: toIso(filters.occurredBefore),
})

const loadLogs = async () => {
  loading.value = true
  status.value = { type: '', message: '' }

  try {
    const response = await getAdminAuditLogs(buildParams())
    logs.value = response.data
  } catch {
    status.value = { type: 'danger', message: 'Failed to load audit logs.' }
  } finally {
    loading.value = false
  }
}

const downloadCsv = async () => {
  loading.value = true
  status.value = { type: '', message: '' }

  try {
    const response = await exportAdminAuditLogs(buildParams())
    const blobUrl = window.URL.createObjectURL(new Blob([response.data], { type: 'text/csv' }))
    const link = document.createElement('a')
    link.href = blobUrl
    link.download = `admin-audit-logs-${new Date().toISOString().replace(/[:.]/g, '-')}.csv`
    document.body.appendChild(link)
    link.click()
    link.remove()
    window.URL.revokeObjectURL(blobUrl)
  } catch {
    status.value = { type: 'danger', message: 'Failed to export audit logs.' }
  } finally {
    loading.value = false
  }
}

const resetFilters = async () => {
  filters.actorUsername = ''
  filters.actionType = ''
  filters.occurredAfter = ''
  filters.occurredBefore = ''
  await loadLogs()
}

const formatDate = (value) => new Date(value).toLocaleString()
const formatEntity = (log) => `${log.entity_type || log.entityType} #${log.entity_id || log.entityId}`
const toIso = (value) => (value ? new Date(value).toISOString() : undefined)

onMounted(loadLogs)
</script>