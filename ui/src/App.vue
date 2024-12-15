<script setup lang="ts">
import type {command} from "@/components/CommandList.vue";
import CommandList from "@/components/CommandList.vue";

var commands: command[] = [
  {title: "echo", command: "echo", args: ['test'], workingDir: '~'},
  {title: 'test', command: 'test', args: ['test'], workingDir: '~'},
]
</script>

<template>
  <h1>Command Runner</h1>
  <div class="content">
    <CommandList :commands=commands></CommandList>
  </div>
</template>

<style scoped>
body {
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.content {
  display: flex;
  flex-direction: column;
  width: 70%;
  background: #001;
  border-radius: 10px;
}
</style>
