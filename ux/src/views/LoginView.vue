<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <main class="bg-dark w-100 h-100">
    <form class="form-signin bg-dark">
      <img class="mb-4" src="/logo.svg" width="253">
      <h1 class="h3 mb-3 fw-normal">Bitte anmelden</h1>

      <div class="form-floating pb-2">
        <input type="email" class="form-control" id="floatingInput" placeholder="name@example.com">
        <label class="text-dark" for="floatingInput">Nutzername</label>
      </div>
      <div class="form-floating pb-3">
        <input type="password" class="form-control" id="floatingPassword" placeholder="Password">
        <label class="text-dark" for="floatingPassword">Passwort</label>
      </div>

      <div class="checkbox mb-3">
        <label>
          <input type="checkbox" value="remember-me"> angemeldet bleiben
        </label>
      </div>
      <button class="w-100 btn btn-lg btn-primary mb-3" type="submit">Anmelden</button>

      <RouterLink class="nav-link text-muted mb-3" to="/login">Passwort vergessen?</RouterLink>
    </form>
  </main>
</template>

<style>
.form-signin {
  position: absolute;
  width: 100%;
  max-width: 330px;
  padding: 15px;
  text-align: center;
  top: 50%;
  left: 50%;
  transform: translateX(-50%) translateY(-50%);
  color: var(--bs-light);
}
</style>