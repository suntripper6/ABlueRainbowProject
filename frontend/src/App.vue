<template>
  <div class="site-chrome d-flex flex-column min-vh-100">
    <Header />

    <main class="app-main flex-grow-1">
      <router-view></router-view>
    </main>

    <footer class="site-footer">
      <div class="footer-panel text-center text-lg-start d-flex flex-column flex-lg-row justify-content-between gap-2">
        <div><strong>A Blue Rainbow</strong> helps families compare care options with a calmer, clearer experience.</div>
        <div>&copy; {{ new Date().getFullYear() }} A Blue Rainbow</div>
      </div>
    </footer>
  </div>
</template>

<script setup>
import Header from './components/Header.vue'
</script>
