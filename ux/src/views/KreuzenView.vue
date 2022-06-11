<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <nav id="nav-top" class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container-fluid hstack row ms-0">
      <RouterLink class="navbar-brand p-0 mx-2 col-auto" to="/">
        <img src="/logo.svg" height="55"> DEFI
      </RouterLink>
      <ul class="nav col-auto ms-auto px-0">
        <li class="nav-item">
          <RouterLink class="nav-link p-2 link-light" to="/kreuzen">Home</RouterLink>
        </li>
        <li class="nav-item">
          <RouterLink class="nav-link p-2 link-secondary" to="/kreuzen">Admin</RouterLink>
        </li>
        <li class="nav-item">
          <RouterLink class="nav-link p-2 link-secondary" to="/kreuzen">Sessions</RouterLink>
        </li>
        <li class="nav-item">
          <RouterLink class="nav-link p-2 link-secondary" to="/kreuzen">Fragen eingeben</RouterLink>
        </li>
        <li class="nav-item">
          <RouterLink class="nav-link p-2 link-secondary" to="/kreuzen">FAQ</RouterLink>
        </li>
        <li class="nav-item">
          <RouterLink class="nav-link p-2 link-secondary" to="/kreuzen">Bugs</RouterLink>
        </li>
        <li class="nav-item">
          <RouterLink class="nav-link p-2 link-light" to="/login">Login</RouterLink>
        </li>
      </ul>
    </div>
  </nav>
  <RouterView></RouterView>
</template>

<style>
#nav-top {
  border-bottom: 1px solid var(--color-border);
}
</style>