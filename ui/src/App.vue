<script setup lang="ts">
import type {command} from "@/components/CommandList.vue";
import CommandList from "@/components/CommandList.vue";

var commands: command[] = [
  {title: "Echo", command: "echo", args: ['test'], workingDir: '~'},
  {title: 'Test', command: 'test', args: ['test'], workingDir: '~'},
]
</script>

<template>
  <h1>Command Runner</h1>
  <div class="content">
    <CommandList :commands=commands></CommandList>
  </div>
</template>

<style scoped>
.content {
  display: flex;
  flex-direction: column;
  width: 70%;
  background: #001;
  border-radius: 10px;
}
</style>
