<template>
  <section class="page-shell page-shell--wide">
    <div class="page-intro">
      <p class="section-kicker">{{ kicker }}</p>
      <div class="section-heading">
        <div>
          <h1 class="page-title">{{ title }}</h1>
          <p class="page-subtitle">{{ subtitle }}</p>
          <div class="page-meta">
            <span class="count-pill">{{ count }} facilities</span>
          </div>
        </div>
      </div>
    </div>

    <div class="mb-4">
      <div class="input-group max-w-md">
        <span class="input-group-text bg-white border-end-0">
          <i class="bi bi-search"></i>
        </span>
        <input
          placeholder="Search by name, city, address..."
          v-model="search"
          @input="handleSearchChange"
          class="form-control border-start-0 ps-0"
        />
      </div>
    </div>

    <div class="panel table-panel position-relative">
      <div v-if="loading" class="position-absolute w-100 h-100 top-0 start-0 d-flex justify-content-center align-items-center bg-white bg-opacity-75 z-index-10">
        <div class="spinner-border text-primary" role="status">
          <span class="visually-hidden">Loading...</span>
        </div>
      </div>
      <div class="table-responsive">
        <table class="table app-table align-middle">
          <thead>
            <tr>
              <th>Name</th>
              <th>Address</th>
              <th>City</th>
              <th>State</th>
              <th>Zip</th>
            </tr>
          </thead>
          <tbody>
            <template v-if="facilities.length > 0">
              <tr v-for="facility in facilities" :key="facility.id">
                <td>
                  <router-link :to="`/${detailPath}/${facility.id}`" class="fw-bold text-decoration-none">
                    {{ facility.name }}
                  </router-link>
                </td>
                <td>{{ facility.address || facility.address_line_1 }}</td>
                <td>{{ facility.city }}</td>
                <td>{{ facility.state }}</td>
                <td>{{ facility.zip_code || facility.zipcode }}</td>
              </tr>
            </template>
            <tr v-else>
              <td colSpan="5" class="empty-cell">
                <div class="table-empty-state">
                  <strong>No {{ title.toLowerCase() }} match your search</strong>
                  <p>Try adjusting your search terms or filters.</p>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <div v-if="totalPages > 1" class="d-flex justify-content-center mt-4">
      <nav aria-label="Page navigation">
        <ul class="pagination">
          <li class="page-item" :class="{ disabled: page === 1 }">
            <button class="page-link" @click="handlePageChange(1)">First</button>
          </li>
          <li class="page-item" :class="{ disabled: page === 1 }">
            <button class="page-link" @click="handlePageChange(page - 1)">Previous</button>
          </li>
          <li v-for="num in visiblePages" :key="num" class="page-item" :class="{ active: page === num }">
            <button class="page-link" @click="handlePageChange(num)">{{ num }}</button>
          </li>
          <li class="page-item" :class="{ disabled: page === totalPages }">
            <button class="page-link" @click="handlePageChange(page + 1)">Next</button>
          </li>
          <li class="page-item" :class="{ disabled: page === totalPages }">
            <button class="page-link" @click="handlePageChange(totalPages)">Last</button>
          </li>
        </ul>
      </nav>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import debounce from 'lodash/debounce'

const props = defineProps({
  title: String,
  subtitle: String,
  kicker: String,
  fetchData: Function,
  detailPath: String
})

const facilities = ref([])
const loading = ref(true)
const error = ref(null)
const page = ref(1)
const totalPages = ref(1)
const count = ref(0)
const search = ref('')

const fetchFacilities = async () => {
  loading.value = true
  try {
    const response = await props.fetchData({ page: page.value, search: search.value })
    facilities.value = response.data.results || []
    count.value = response.data.count || 0
    totalPages.value = Math.ceil((response.data.count || 0) / 10)
  } catch {
    error.value = `Failed to fetch ${props.title.toLowerCase()}.`
  } finally {
    loading.value = false
  }
}

const handleSearchChange = debounce(() => {
  page.value = 1
  fetchFacilities()
}, 500)

const handlePageChange = (newPage) => {
  page.value = newPage
  fetchFacilities()
}

const visiblePages = computed(() => {
  const range = []
  const maxVisiblePages = 5
  let start = Math.max(1, page.value - Math.floor(maxVisiblePages / 2))
  let end = Math.min(totalPages.value, start + maxVisiblePages - 1)

  if (end - start + 1 < maxVisiblePages) {
    start = Math.max(1, end - maxVisiblePages + 1)
  }

  for (let i = start; i <= end; i++) {
    range.push(i)
  }
  return range
})

onMounted(fetchFacilities)
</script>
