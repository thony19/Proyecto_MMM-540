<template>
  <div id="app">
    <div class="progress-bar">
      <div class="progress" :style="{ width: progressPercentage + '%' }"></div>
    </div>

    <form>
      <fieldset v-for="(step, index) in steps" :key="index" v-show="currentStep === index">
        <h2>{{ step.title }}</h2>
        <input type="text" v-model="step.input1" required>
        <input type="text" v-model="step.input2" required>
        <button v-if="currentStep > 0" @click.prevent="previousStep">Anterior</button>
        <button v-if="currentStep < steps.length - 1" @click.prevent="nextStep">Siguiente</button>
        <button v-else type="submit">Enviar</button>
      </fieldset>
    </form>
  </div>
</template>

<script >
export default {
  data() {
    return {
      currentStep: 0,
      steps: [
        { title: 'Paso 1', input1: '', input2: '' },
        { title: 'Paso 2', input1: '', input2: '' },
        { title: 'Paso 3', input1: '', input2: '' }
      ]
    };
  },
  computed: {
    progressPercentage() {
      return (this.currentStep / (this.steps.length - 1)) * 100;
    }
  },
  methods: {
    nextStep() {
      this.currentStep++;
    },
    previousStep() {
      this.currentStep--;
    }
  }
};
</script>

<style scoped>
.progress-bar {
  width: 100%;
  height: 10px;
  background-color: #ccc;
  margin-bottom: 20px;
}

.progress {
  height: 100%;
  background-color: #4CAF50;
  transition: width 0.3s ease;
}
</style>
