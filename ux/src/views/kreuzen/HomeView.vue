<script setup>
import { RouterLink } from 'vue-router'
import { onMounted } from 'vue'

onMounted(() => {
  const darkBtn = document.querySelector('#darkview');
  const lightBtn = document.querySelector('#lightview');
  const linkTag = document.querySelector('#theme');

  darkBtn.addEventListener('click', () => {
    linkTag.setAttribute('href', 'src/assets/dark.css')
  });

  lightBtn.addEventListener('click', () => {
    linkTag.setAttribute('href', 'src/assets/light.css')
  });
})
</script>

<template>
  <div class="container-xl text-center">
    <h1>Home-Kreuzen</h1>
    <p>
      Bis jetzt gibts nur die Navigationsleiste oben.
      <br /> Links, die noch nicht funktionieren, sind dunkler.
      <br /><br /> Hier nicht direkt verlinkte Funktionen:
    </p>
    <RouterLink to="/kreuzen/session/learn">Kreuz-Session</RouterLink>
    <div class="hstack gap-4" style="width: fit-content; margin: 0 auto;">
      <div id="lightview">Helles Thema</div>
      <div id="darkview">Dunkles Thema</div>
    </div>
  </div>
</template>