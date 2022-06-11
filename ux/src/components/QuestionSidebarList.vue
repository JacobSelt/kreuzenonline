<template>
  <div class="col session-sidebar flex-column h-100 collapse collapse-horizontal show pt-2 px-0" id="session-sidebar">
    <div class="m-0 p-1 row" id="session-sidebar-header">
      <div class="hstack">
        <div class="p-1 px-2" id="session-sidebar-header-type">KLAUSUR</div>
        <div class="ms-auto text-muted" style="">24/250</div>
      </div>
      <h5 class="card-title pt-1">Sessionname</h5>
    </div>
    <div class="m-0 row flex-grow-1" style="background-color: var(--color-second); border-bottom: 1px solid var(--color-border);">
      FRAGEN
    </div>
    <div class="m-0 row py-2" id="session-sidebar-time">
      <div class="hstack px-0">
        <div class="px-3">
          <i class="bi bi-x-lg"></i>
        </div>
        <div class="px-2 ms-auto">
          <h6 class="mb-0 fw-bold text-center">10m 43s</h6>
          <p class="mb-0 text-muted text-center">SITZUNG</p>
        </div>
        <div class="px-2">
          <h6 class="mb-0 fw-bold text-center">14s</h6>
          <p class="mb-0 text-muted text-center">FRAGE</p>
        </div>
        <div class="ms-auto px-2" style="font-size: 1.8rem;">
          <i class="bi bi-pause"></i>
        </div>
      </div>
    </div>
    <div class="m-0 row p-2">
      <h6 class="mb-0 text-muted" id="session-sidebar-results">ZUR AUSWERTUNG</h6>
    </div>
  </div>
  <div class="col p-0 mt-2" id="session-sidebar-toggler" data-bs-toggle="collapse" data-bs-target="#session-sidebar" aria-expanded="true" aria-controls="session-sidebar">
    <i class="bi bi-chevron-left"></i>
  </div>
</template>

<style>
.session-sidebar {
  background-color: var(--color-dark);
  border-right: 1px solid var(--color-border);
  display: flex;
  flex: 0 0 auto;
  width: 400px; 
}
#session-sidebar-header {
  border-bottom: 1px solid var(--color-border);
  width: 400px;
}
#session-sidebar-header-type {
  border: 1px solid;
  border-radius: 30px;
  width: fit-content;
  float: left;
  font-size: 0.8rem;
}
#session-sidebar-time {
  border-bottom: 1px solid var(--color-border);
}
#session-sidebar-time > div > p {
  font-size: 0.7rem;
}
#session-sidebar-results {
  width: fit-content;
  margin-left: auto;
  margin-right: auto;
  font-size: 0.9rem;
}
#session-sidebar-toggler {
  width: 27px;
  height: 27px;
  flex: 0 0 auto;
  border: 1px solid var(--color-border);
  border-radius: 15px;
  text-align: center;
}
#session-sidebar-toggler > i {
  font-size: 0.9rem;
}
</style>