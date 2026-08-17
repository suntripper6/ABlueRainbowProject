<template>
  <FacilityList 
    title="Skilled Nursing Facilities" 
    kicker="Care Directory"
    subtitle="Scan available nursing facilities with clearer navigation and stronger hierarchy."
    :fetchData="getSkilledNursing"
    detailPath="skillednursing"
  />
</template>

<script setup>
import FacilityList from './FacilityList.vue'
import { getSkilledNursing } from '../api'
</script>
