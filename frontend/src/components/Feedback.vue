<template>
  <section class="page-shell">
    <div class="page-intro">
      <p class="section-kicker">Feedback</p>
      <h1 class="page-title">Tell us what would help families more</h1>
      <p class="page-subtitle">Share ideas, corrections, or gaps in the directory through a calmer feedback form.</p>
    </div>
    
    <div class="panel form-panel mt-4">
      <div v-if="status.message" :class="['alert', `alert-${status.type}`]" role="alert">
        {{ status.message }}
      </div>
      
      <form @submit.prevent="handleSubmit" class="form-shell">
        <div class="mb-4">
          <label class="form-label">Your Name</label>
          <input 
            type="text" 
            class="form-control"
            placeholder="How should we address you?"
            v-model="formData.name"
            required
          />
        </div>

        <div class="mb-4">
          <label class="form-label">Email Address</label>
          <input 
            type="email" 
            class="form-control"
            placeholder="Where can we reach you if we have questions?"
            v-model="formData.email"
            required
          />
        </div>

        <div class="mb-4">
          <label class="form-label">Your Comments</label>
          <textarea 
            class="form-control"
            rows="5" 
            placeholder="What can we improve?"
            v-model="formData.comments"
            required
          ></textarea>
        </div>

        <button 
          type="submit" 
          class="btn btn-secondary"
          :disabled="loading"
        >
          <span v-if="loading" class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>
          <span v-else>Send Feedback</span>
        </button>
      </form>
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue'
import { postFeedback } from '../api'

const formData = ref({ name: '', email: '', comments: '' })
const status = ref({ type: '', message: '' })
const loading = ref(false)

const handleSubmit = async () => {
  loading.value = true
  try {
    await postFeedback(formData.value)
    status.value = { type: 'success', message: 'Thank you for your feedback!' }
    formData.value = { name: '', email: '', comments: '' }
  } catch {
    status.value = { type: 'danger', message: 'Failed to send feedback. Please try again.' }
  } finally {
    loading.value = false
  }
}
</script>
