<template>
  <div class="card-themed top-50 translate-middle-y">
    <div class="card-body">
      <p>
        In einer prospektiven Kohortenstudie zeigt sich ein Zusammenhang zwischen dem Ausmaß des Alkoholkonsums und dem Lungenkrebsrisiko. Berücksichtigt man jedoch zusätzlich das Ausmaß des Zigarettenrauchens durch statistische Kontrolle/Adjustierung, so ist der Zusammenhang zwischen Alkoholkonsum und Lungenkrebsrisiko nicht mehr nachweisbar.
        <br /><br />Wie wird die Variable „Alkoholkonsum“ im Rahmen der untersuchten Forschungsfrage am besten bezeichnet?
      </p>
    
      <div class="hstack gap-4 py-2 px-3 answer wrong" style="border-top: 1px solid var(--color-border);">
        <div class="letter">A</div>
        <div>Confounder</div>
        <div class="ms-auto">20%</div>
      </div>
      <div class="hstack gap-4 py-2 px-3 answer wrong">
        <div class="letter">B</div>
        <div>kausaler Risikofaktor</div>
        <div class="ms-auto">20%</div>
      </div>
      <div class="hstack gap-4 py-2 px-3 answer wrong">
        <div class="letter">C</div>
        <div>Mediator</div>
        <div class="ms-auto">20%</div>
      </div>
      <div class="hstack gap-4 py-2 px-3 answer wrong">
        <div class="letter">D</div>
        <div>Moderator</div>
        <div class="ms-auto">20%</div>
      </div>
      <div class="hstack gap-4 py-2 px-3 answer right chosen">
        <div class="letter">E</div>
        <div class="">Risikoindikator</div>
        <div class="ms-auto">20%</div>
      </div>
    </div>
  </div>
</template>

<style>
.answer {
  border-bottom: 1px solid var(--color-border);
}
.answer.right {
  color: var(--color-green);
}
.answer.right.chosen {
  background-color: var(--color-green-50);
}
.answer.wrong {
  color: var(--color-red);
}
.answer.wrong.chosen {
  background-color: var(--color-red-50);
}
.answer.chosen {
  color: var(--color-contrast) !important;
}
.answer > .letter {
  border: 1px solid;
  border-radius: 15px;
  width: 27px;
  height: 27px;
  text-align: center;
}
.answer.right > .letter {
  border: 1px solid var(--color-green);
}
.answer.right.chosen > .letter {
  background-color: var(--color-green);
}
.answer.wrong > .letter {
  border: 1px solid var(--color-red);
}
.answer.wrong.chosen > .letter {
  background-color: var(--color-red);
}

.card-themed {
  position: relative;
  display: flex;
  flex-direction: column;
  min-width: 0;
  word-wrap: break-word;
  background-color: var(--color-second);
  background-clip: border-box;
  border: 1px solid var(--color-border);
  border-radius: .5rem;

  width: 100%;
  max-width: 1200px;
  margin: auto;
  border: 1px solid var(--color-border);
}
.list-group-item-dark {
  position: relative;
  display: block;
  padding: .5rem 1rem;
  color: var(--color-contrast);
  text-decoration: none;
  background-color: var(--color-dark);
  border: 1px solid var(--color-border);
}
</style>