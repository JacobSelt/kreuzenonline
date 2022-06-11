<script setup>
import QuestionCard from '@/components/QuestionCard.vue';
import QuestionSidebarList from '@/components/QuestionSidebarList.vue';
</script>

<template>
  <div class="row gap-2 container-fluid px-0 mx-0" style="height: calc(100% - 73px);">
    <QuestionSidebarList></QuestionSidebarList>

    <div class="col">
      <QuestionCard></QuestionCard>
    </div>
  </div>
</template>

<style>
.answer {
  border-bottom: 1px solid #FFFFFF;
}
.answer.chosen {
  color: var(--bs-light) !important;
}
.answer.right {
  color: var(--bs-green);
}
.answer.right.chosen {
  background-color: #1987547E;
}
.answer.wrong {
  color: var(--bs-red);
}
.answer.wrong.chosen {
  background-color: #dc35457E;
}
.answer > .letter {
  border: 1px solid;
  border-radius: 15px;
  width: 27px;
  height: 27px;
  text-align: center;
}
.answer.right > .letter {
  border: 1px solid var(--bs-green);
}
.answer.right.chosen > .letter {
  background-color: var(--bs-green);
}
.answer.wrong > .letter {
  border: 1px solid var(--bs-red);
}
.answer.wrong.chosen > .letter {
  background-color: var(--bs-red);
}

.card-dark {
  position: relative;
  display: flex;
  flex-direction: column;
  min-width: 0;
  word-wrap: break-word;
  background-color: var(--bs-dark);
  background-clip: border-box;
  border: 1px solid rgba(0,0,0,.125);
  border-radius: .25rem;
}

.list-group-item-dark {
  position: relative;
  display: block;
  padding: .5rem 1rem;
  color: rgba(var(--bs-light-rgb));
  text-decoration: none;
  background-color: var(--bs-dark);
  border: 1px solid rgba(255, 255, 255, 0.125);
}

.session-sidebar {
  background-color: var(--bs-dark);
  display: flex;
  flex: 0 0 auto;
  width: 400px; 
}
</style>