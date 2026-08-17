<template>
  <FacilityList 
    title="Home Health Agencies" 
    kicker="Care Directory"
    subtitle="Review home care providers in a more legible table and detail experience."
    :fetchData="getHomeHealth"
    detailPath="homehealth"
  />
</template>

<script setup>
import FacilityList from './FacilityList.vue'
import { getHomeHealth } from '../api'
</script>
