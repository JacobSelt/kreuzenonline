<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <RouterView />
</template>

<style>
html, body, #app {
  height: 100%;
  color: rgba(var(--bs-light-rgb));
  --bs-bg-opacity: 1;
  background-color: #272C31 !important;
}
/*
#343A40 -> gray-800
#2E3338 -> gray-833
#272C31 -> gray-867
#212529 -> gray-900
*/
</style>
