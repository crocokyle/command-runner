<script setup lang="ts">
export type command = {
  id: number,
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
        <label for="input-{{arg}}">{{arg}}:</label>
        <input type="text" id="input-{{arg}}">
      </div>
      <div class="command-output open" id="output-{{command.id}}">

      </div>
    </details>
  </div>
</template>

<style scoped>
.command-list {
  display: flex;
  flex-direction: column;
  gap: 1em;
  width: 100%;
}

.command-item {
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  border-radius: 10px;
  background: #112;
  padding: 1em;
}

.command-item summary {
  width: 100%;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}

.command-title {
  font-size: 1.5em;
  justify-self: flex-start;
}

.command-item .command-title::after {
  content: ' (click for args)';
  font-size: 12pt;
  filter: opacity(50%);
}

.command-item[open] .command-title::after {
  content: '';
}

.command-run {
  justify-self: flex-end;
  width: 5em;
  border-radius: 0.5em 1em;
  border: #99a;
  background: #223;
  color: #99a;
}

.command-run:hover {
  background: #334;
}

.command-arg {
  width: 85%;
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-top: 0.5em;
  padding: 1em;
  background: #334;
  border-radius: 1em;
}

.command-arg label {
  font-size: 1.2em;
}

</style>