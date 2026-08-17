<template>
  <div class="landing-root">
    <section class="hero-shell">
      <div class="hero-logo-row">
        <div class="visual-frame hero-logo-frame">
          <img src="/img/logo.png" class="site-logo" alt="A Blue Rainbow logo" />
        </div>
      </div>

      <div class="hero-panel">
        <div class="hero-copy">
          <p class="hero-badge">Gentle Care Navigation</p>
          <h1 class="hero-title">A calmer way to move through senior care options.</h1>
          <p class="hero-subtitle">
            A Blue Rainbow brings assisted living, home health, skilled nursing, and hospice resources into one quieter, easier-to-scan directory for caregivers and families.
          </p>
          <div class="hero-actions">
            <router-link to="/assistedliving" class="btn btn-primary">Browse Resources</router-link>
            <router-link to="/feedback" class="btn btn-secondary">Share Feedback</router-link>
          </div>
        </div>
        <div class="hero-rail">
          <div class="hero-stats">
            <div class="stat-card">
              <span>Care categories</span>
              <strong>4</strong>
            </div>
            <div class="stat-card">
              <span>Core actions</span>
              <strong>Search, review, update</strong>
            </div>
            <div class="stat-card">
              <span>Built for</span>
              <strong>Caregivers first</strong>
            </div>
          </div>
          <div class="hero-note-card">
            <span class="hero-note-label">Why it works</span>
            <p>Search, compare, and revisit provider records without losing your place in the directory.</p>
          </div>
        </div>
      </div>

      <div class="resource-grid">
        <router-link to="/assistedliving" class="resource-card">
          <span class="card-tag">Residential</span>
          <h3>Assisted Living</h3>
          <p>Compare facilities with a cleaner overview and faster drill-down into details.</p>
        </router-link>
        <router-link to="/homehealth" class="resource-card">
          <span class="card-tag">At Home</span>
          <h3>Home Health</h3>
          <p>Review home care providers in a more legible table and detail experience.</p>
        </router-link>
        <router-link to="/skillednursing" class="resource-card">
          <span class="card-tag">Medical</span>
          <h3>Skilled Nursing</h3>
          <p>Scan available nursing facilities with clearer navigation and stronger hierarchy.</p>
        </router-link>
        <router-link to="/hospice" class="resource-card">
          <span class="card-tag">Supportive</span>
          <h3>Hospice</h3>
          <p>Access hospice information with a calmer presentation and consistent actions.</p>
        </router-link>
      </div>
    </section>
  </div>
</template>

<script setup>
</script>
