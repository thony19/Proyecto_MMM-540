<script setup>
import HelloWorld from './components/HelloWorld.vue'
import Form from './components/Form.vue';
</script>

<template>
  <div class="">
      <div>
        <a href="https://vitejs.dev" target="_blank">
          <img src="./assets/Logo_UNAH.png" class="logo" alt="Vite logo" />
        </a>
        <a href="https://vuejs.org/" target="_blank">
          <img src="./assets/vue.svg" class="logo vue" alt="Vue logo" />
        </a>
      </div>
      <!-- <HelloWorld msg="Estilos de Aprendizaje e Inteligencias múltiples" /> -->
      <Form></Form>
  </div>
</template>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
