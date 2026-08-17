<template>
  <div v-if="loading" class="text-center py-5">
    <div class="spinner-border text-primary" role="status">
      <span class="visually-hidden">Loading...</span>
    </div>
  </div>

  <div v-else-if="error || !facility" class="container py-5">
    <div class="alert alert-danger" role="alert">
      {{ error || 'Facility not found.' }}
    </div>
    <router-link to="/" class="btn btn-secondary mt-3">Back to Home</router-link>
  </div>

  <section v-else class="page-shell">
    <div class="panel detail-panel">
      <div v-if="status.message" :class="['alert', `alert-${status.type}`]" role="alert">
        {{ status.message }}
      </div>
      <p class="section-kicker">{{ kicker }}</p>

      <template v-if="editing">
        <div class="row g-3">
          <div class="col-12">
            <label class="form-label">Facility Name</label>
            <input v-model="editForm.name" class="form-control" type="text" required />
          </div>
          <div class="col-12">
            <label class="form-label">Address</label>
            <input v-model="editForm.address" class="form-control" type="text" required />
          </div>
          <div class="col-md-4">
            <label class="form-label">City</label>
            <input v-model="editForm.city" class="form-control" type="text" required />
          </div>
          <div class="col-md-4">
            <label class="form-label">State</label>
            <input v-model="editForm.state" class="form-control" type="text" required />
          </div>
          <div class="col-md-4">
            <label class="form-label">Zip Code</label>
            <input v-model="editForm.zip_code" class="form-control" type="text" required />
          </div>
          <div class="col-md-6">
            <label class="form-label">Phone Number</label>
            <input v-model="editForm.phone_number" class="form-control" type="text" />
          </div>
          <div class="col-md-6">
            <label class="form-label">Website</label>
            <input v-model="editForm.official_website" class="form-control" type="url" />
          </div>
          <div class="col-12">
            <label class="form-label">Map Link</label>
            <input v-model="editForm.map" class="form-control" type="url" />
          </div>
        </div>
      </template>
      <template v-else>
        <h1 class="page-title">{{ facility.name }}</h1>
        <p class="detail-address">{{ facility.address || facility.address_line_1 }}</p>
        <p class="detail-description">
          {{ facility.city }}, {{ facility.state }} {{ facility.zip_code || facility.zipcode || facility.zipCode }}
        </p>
      </template>

      <div class="detail-grid mt-4">
        <div class="detail-card">
          <h3>Phone</h3>
          <p>{{ displayFacility.phone_number || displayFacility.phoneNumber || 'Not listed' }}</p>
        </div>
        <div class="detail-card">
          <h3>Website</h3>
          <a v-if="displayFacility.official_website || displayFacility.officialWebsite" :href="displayFacility.official_website || displayFacility.officialWebsite" class="detail-link" target="_blank" rel="noreferrer">
            Visit official site
          </a>
          <p v-else>Not listed</p>
        </div>
        <div class="detail-card">
          <h3>Map</h3>
          <a v-if="displayFacility.map" :href="displayFacility.map" class="detail-link" target="_blank" rel="noreferrer">
            Open map
          </a>
          <p v-else>Not listed</p>
        </div>
      </div>

      <div class="action-row mt-5">
        <a v-if="displayFacility.map" :href="displayFacility.map" target="_blank" rel="noreferrer" class="btn btn-success me-2">
          Find on Map
        </a>
        <button v-if="isAuthenticated && editing" type="button" class="btn btn-secondary me-2" :disabled="saving" @click="saveChanges">
          {{ saving ? 'Saving...' : 'Save Changes' }}
        </button>
        <button v-if="isAuthenticated" type="button" class="btn btn-outline-secondary me-2" :disabled="saving || deleting" @click="toggleEditing">
          {{ editing ? 'Cancel Edit' : 'Edit Facility' }}
        </button>
        <button v-if="isAuthenticated" type="button" class="btn btn-outline-danger me-2" :disabled="saving || deleting" @click="removeFacility">
          {{ deleting ? 'Deleting...' : 'Delete Facility' }}
        </button>
        <router-link to="/" class="btn btn-outline-secondary">Back to Search</router-link>
      </div>
    </div>
  </section>
</template>

<script setup>
import { computed, ref, onMounted, watch } from 'vue'
import { useRouter } from 'vue-router'
import { deleteFacility, updateFacility } from '../api'
import { isAuthenticated } from '../auth'

const props = defineProps({
  kicker: String,
  fetchData: Function,
  id: String,
  resourcePath: String,
})

const router = useRouter()
const facility = ref(null)
const loading = ref(true)
const error = ref(null)
const editing = ref(false)
const saving = ref(false)
const deleting = ref(false)
const status = ref({ type: '', message: '' })
const editForm = ref({})

const displayFacility = computed(() => facility.value || {})

const buildEditableSnapshot = (source) => ({
  name: source.name || '',
  address: source.address || source.address_line_1 || '',
  city: source.city || '',
  state: source.state || '',
  zip_code: source.zip_code || source.zipcode || source.zipCode || '',
  phone_number: source.phone_number || source.phoneNumber || '',
  official_website: source.official_website || source.officialWebsite || '',
  map: source.map || '',
})

const buildUpdatePayload = () => ({
  ...facility.value,
  ...editForm.value,
  id: facility.value.id,
  provider_id: facility.value.provider_id,
})

const loadFacility = async () => {
  loading.value = true
  status.value = { type: '', message: '' }
  try {
    const response = await props.fetchData(props.id)
    facility.value = response.data
    editForm.value = buildEditableSnapshot(response.data)
  } catch {
    error.value = 'Failed to fetch facility details.'
  } finally {
    loading.value = false
  }
}

const toggleEditing = () => {
  editing.value = !editing.value
  if (editing.value && facility.value) {
    editForm.value = buildEditableSnapshot(facility.value)
  }
}

const saveChanges = async () => {
  saving.value = true
  status.value = { type: '', message: '' }

  try {
    const payload = buildUpdatePayload()
    await updateFacility(props.resourcePath, props.id, payload)
    facility.value = { ...facility.value, ...payload }
    editForm.value = buildEditableSnapshot(facility.value)
    editing.value = false
    status.value = { type: 'success', message: 'Facility updated successfully.' }
  } catch {
    status.value = { type: 'danger', message: 'Failed to update this facility.' }
  } finally {
    saving.value = false
  }
}

const removeFacility = async () => {
  if (!window.confirm('Delete this facility record? This action cannot be undone.')) {
    return
  }

  deleting.value = true
  status.value = { type: '', message: '' }

  try {
    await deleteFacility(props.resourcePath, props.id)
    await router.push(`/${props.resourcePath}`)
  } catch {
    status.value = { type: 'danger', message: 'Failed to delete this facility.' }
  } finally {
    deleting.value = false
  }
}

onMounted(loadFacility)
watch(() => props.id, loadFacility)
</script>
