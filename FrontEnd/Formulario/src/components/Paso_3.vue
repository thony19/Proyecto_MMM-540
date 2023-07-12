<template>
  <div>
    <h2>Paso 3</h2>
    <textarea v-model="stepData.input3" placeholder="Ingrese un mensaje"></textarea>
    <button @click="previousStep">Anterior</button>
    <button @click="submitForm">Enviar</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      stepData: {
        input3: ''
      }
    };
  },
  methods: {
    previousStep() {
      this.$emit('previous');
    },
    submitForm() {
      this.$emit('submit', this.stepData);
    }
  }
};
</script>
