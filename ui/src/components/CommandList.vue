<script setup lang="ts">
export type command = {
  title: string,
  command: string,
  workingDir: string,
  args: string[],
};

defineProps<{
  commands: command[]
}>();
</script>

<template>
  <div class="command-list">
    <details class="command-item" v-for="command in commands">
      <summary>
        <span class="command-title">{{command.title}}</span>
        <button class="command-run">Run</button>
      </summary>
      Filler Content
    </details>
  </div>
</template>

<style scoped>
.command-list {
  display: flex;
  flex-direction: column;
  width: 100%;
}

.command-item {
  width: 100%;
  display: flex;
  justify-content: space-evenly;
}

.command-item summary {
  width: 100%;
  display: flex;
  flex-direction: row;
  justify-content: space-evenly;
}

.command-title {
  align-self: flex-start;
}

.command-run {
  align-self: flex-end;
}
</style>