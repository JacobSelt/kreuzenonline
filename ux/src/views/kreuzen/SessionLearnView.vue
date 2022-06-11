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