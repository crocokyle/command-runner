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
      <div class="command-arg" v-for="arg in command.args">
        <label for="input-{{arg}}">{{arg}}</label>
        <input type="text" id="input-{{arg}}">
      </div>
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
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.command-item summary {
  width: 100%;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}

.command-title {
  justify-self: flex-start;
}

.command-run {
  justify-self: flex-end;
}

.command-arg {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding-left: 1em;
}
</style>