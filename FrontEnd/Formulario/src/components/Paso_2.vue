<template>
  <div>
    <h2>Paso 2</h2>
    <input type="email" v-model="stepData.input2" placeholder="Ingrese su correo electrónico">
    <button @click="previousStep">Anterior</button>
    <button @click="nextStep">Siguiente</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      stepData: {
        input2: ''
      }
    };
  },
  methods: {
    previousStep() {
      this.$emit('previous');
    },
    nextStep() {
      this.$emit('next', this.stepData);
    }
  }
};
</script>
