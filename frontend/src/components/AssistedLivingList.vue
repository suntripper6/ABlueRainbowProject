<template>
  <FacilityList 
    title="Assisted Living Facilities" 
    kicker="Care Directory"
    subtitle="Browse local assisted living options with a clearer table layout and faster path into each provider record."
    :fetchData="getAssistedLiving"
    detailPath="assistedliving"
  />
</template>

<script setup>
import FacilityList from './FacilityList.vue'
import { getAssistedLiving } from '../api'
</script>
