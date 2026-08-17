<template>
  <section class="page-shell">
    <div class="page-intro">
      <p class="section-kicker">Admin Tools</p>
      <h1 class="page-title">Create a new facility record</h1>
      <p class="page-subtitle">Add a new provider listing to the directory with the correct facility category and contact details.</p>
    </div>

    <div class="panel form-panel mt-4">
      <div v-if="status.message" :class="['alert', `alert-${status.type}`]" role="alert">
        {{ status.message }}
      </div>

      <form @submit.prevent="handleSubmit" class="form-shell">
        <div class="row g-3">
          <div class="col-md-6">
            <label class="form-label">Facility Category</label>
            <select v-model="form.resourcePath" class="form-select" required>
              <option v-for="option in categoryOptions" :key="option.value" :value="option.value">
                {{ option.label }}
              </option>
            </select>
          </div>

          <div class="col-md-6">
            <label class="form-label">Provider</label>
            <select v-model.number="form.provider_id" class="form-select" required>
              <option v-for="provider in filteredProviders" :key="provider.id" :value="provider.id">
                {{ provider.facility_name || provider.facilityName }}
              </option>
            </select>
          </div>

          <div class="col-12">
            <label class="form-label">Facility Name</label>
            <input v-model="form.name" class="form-control" type="text" required />
          </div>

          <div class="col-12">
            <label class="form-label">Address</label>
            <input v-model="form.address" class="form-control" type="text" required />
          </div>

          <div class="col-md-4">
            <label class="form-label">City</label>
            <input v-model="form.city" class="form-control" type="text" required />
          </div>

          <div class="col-md-4">
            <label class="form-label">State</label>
            <input v-model="form.state" class="form-control" type="text" required />
          </div>

          <div class="col-md-4">
            <label class="form-label">Zip Code</label>
            <input v-model="form.zip_code" class="form-control" type="text" required />
          </div>

          <div class="col-md-6">
            <label class="form-label">Phone Number</label>
            <input v-model="form.phone_number" class="form-control" type="text" />
          </div>

          <div class="col-md-6">
            <label class="form-label">Official Website</label>
            <input v-model="form.official_website" class="form-control" type="url" />
          </div>

          <div class="col-12">
            <label class="form-label">Map Link</label>
            <input v-model="form.map" class="form-control" type="url" />
          </div>
        </div>

        <div class="d-flex gap-3 mt-4 flex-wrap">
          <button type="submit" class="btn btn-secondary" :disabled="loading || !form.provider_id">
            {{ loading ? 'Creating...' : 'Create Facility' }}
          </button>
          <router-link class="btn btn-outline-secondary" to="/">Cancel</router-link>
        </div>
      </form>
    </div>
  </section>
</template>

<script setup>
import { computed, onMounted, reactive, ref, watch } from 'vue'
import { useRouter } from 'vue-router'
import { createFacility, getProviders } from '../api'

const router = useRouter()

const categoryOptions = [
  { value: 'assistedliving', label: 'Assisted Living', providerType: 'Assisted Living' },
  { value: 'homehealth', label: 'Home Health', providerType: 'Home Health' },
  { value: 'skillednursing', label: 'Skilled Nursing', providerType: 'Skilled Nursing' },
  { value: 'hospice', label: 'Hospice', providerType: 'Hospice' },
]

const form = reactive({
  resourcePath: 'assistedliving',
  provider_id: null,
  name: '',
  address: '',
  city: '',
  state: '',
  zip_code: '',
  phone_number: '',
  official_website: '',
  map: '',
})

const providers = ref([])
const loading = ref(false)
const status = ref({ type: '', message: '' })

const selectedCategory = computed(() =>
  categoryOptions.find(option => option.value === form.resourcePath) ?? categoryOptions[0],
)

const filteredProviders = computed(() => {
  const providerType = selectedCategory.value.providerType
  return providers.value.filter(provider => (provider.facility_type || provider.facilityType) === providerType)
})

const syncProviderSelection = () => {
  const currentProviderStillValid = filteredProviders.value.some(provider => provider.id === form.provider_id)
  if (currentProviderStillValid) {
    return
  }

  form.provider_id = filteredProviders.value[0]?.id ?? null
}

const handleSubmit = async () => {
  loading.value = true
  status.value = { type: '', message: '' }

  try {
    const payload = {
      name: form.name,
      address: form.address,
      city: form.city,
      state: form.state,
      zip_code: form.zip_code,
      phone_number: form.phone_number,
      official_website: form.official_website,
      map: form.map,
      provider_id: form.provider_id,
    }

    const response = await createFacility(form.resourcePath, payload)
    await router.push(`/${form.resourcePath}/${response.data.id}`)
  } catch {
    status.value = { type: 'danger', message: 'Failed to create the facility record.' }
  } finally {
    loading.value = false
  }
}

onMounted(async () => {
  try {
    const response = await getProviders()
    providers.value = response.data
    syncProviderSelection()
  } catch {
    status.value = { type: 'danger', message: 'Failed to load provider options.' }
  }
})

watch(() => form.resourcePath, syncProviderSelection)
watch(filteredProviders, syncProviderSelection)
</script>