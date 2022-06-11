<script setup>
import { RouterLink } from 'vue-router'
</script>

<template>
  <div class="container-xl text-center">
    <h1>Home-Kreuzen</h1>
    <p>
      Bis jetzt gibts nur die Navigationsleiste oben.
      <br /> Links, die noch nicht funktionieren, sind dunkler.
    </p>
    <RouterLink to="/kreuzen/session/learn">Kreuz-Session</RouterLink>
  </div>
</template>
