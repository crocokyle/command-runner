<script setup lang="ts">
import CommandList from "@/components/CommandList.vue";

var commands: command[] = [
  {id: 0, title: "Echo", command: "echo", args: [{id: 0, title: 'test'}, {id: 1, title: 'best'}], workingDir: '~'},
  {id: 1, title: 'Test', command: 'test', args: [{id: 0, title: 'test'}], workingDir: '~'},
] // Populate with a fetch later
</script>

<template>
  <h1>Command Runner</h1>
  <CommandList :commands=commands />

</template>
