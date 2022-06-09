<script setup>
import { RouterLink } from 'vue-router'
</script>

<template>
  <div class="h-100">
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container-fluid hstack row ms-0">
      <RouterLink class="navbar-brand p-0 mx-2 col-auto" to="/">
        <img src="/logo.svg" height="55" /> DEFI
      </RouterLink>
      <ul class="nav col-auto ms-auto px-0">
        <li class="nav-item">
          <RouterLink class="nav-link p-2 link-light" to="/kreuzen">Kreuzen</RouterLink>
        </li>
        <li class="nav-item">
          <a class="nav-link link-light" href="https://defi.server.uni-frankfurt.de/bscw/bscw.cgi/">Files</a>
        </li>
        <li class="nav-item" style="font-size: 22px; padding: 3px 8px 0px 8px;">
          <a class="link-light" href="https://www.facebook.com/defiffm/">
            <i class="bi bi-facebook"></i>
          </a>
        </li>
        <li class="nav-item" style="font-size: 22px; padding: 3px 8px 0px 8px;">
          <a class="link-light" href="https://www.instagram.com/defi.ffm/">
            <i class="bi bi-instagram"></i>
          </a>
        </li>
      </ul>
    </div>
  </nav>
  <div class="d-flex text-center text-white bg-dark" style="height: calc(100% - 71px)">
    <div class="cover-container d-flex w-100 p-3 pt-0 mx-auto flex-column">
      <main class="px-3" style="padding-top: 10%;">
        <h1>Willkommen zum neuen DEFI!</h1>
        <p class="lead pt-4">
          Der KreuzenOnline-Server wurde von Grund auf neuprogrammiert.
          <br />Wir hoffen, dass Ihr so nun besser und mit mehr Spaß kreuzen könnt.
          <br />
          <br />Sollten Euch Fehler auffallen oder ihr Verbesserungsvorschläge haben, schickt uns bitte eine kurze Nachricht!
        </p>
        <p class="lead pt-4">
          <RouterLink
            class="btn btn-lg btn-secondary fw-bold border-white bg-white"
            style="color: #333"
            to="/kreuzen"
          >Lass mich kreuzen!</RouterLink>
        </p>
      </main>

      <footer class="mt-auto text-white-50 hstack gap-3" style="align-self: center;">
        <RouterLink class="link-light" to="/kontakt">Kontakt</RouterLink>
        <div class="vr"></div>
        <RouterLink class="link-light" to="/impressum">Impressum</RouterLink>
      </footer>
    </div>
  </div>
  </div>
</template>
