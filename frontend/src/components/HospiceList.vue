<template>
  <FacilityList 
    title="Hospice Care" 
    kicker="Care Directory"
    subtitle="Access hospice information with a calmer presentation and consistent actions."
    :fetchData="getHospice"
    detailPath="hospice"
  />
</template>

<script setup>
import FacilityList from './FacilityList.vue'
import { getHospice } from '../api'
</script>
