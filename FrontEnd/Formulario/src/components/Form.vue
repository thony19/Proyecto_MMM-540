<template>
  <div >
    <component :is="currentStep" @next="nextStep" @previous="previousStep" @submit="submitForm"></component>
  </div>
</template>

<script>
import Paso_1 from './Paso_1.vue';
import Paso_2 from './Paso_2.vue';
import Paso_3 from './Paso_3.vue';
import Paso_4 from './Paso_4.vue';
import Paso_5 from './Paso_5.vue';
import Paso_6 from './Paso_6.vue';
import Paso_7 from './Paso_7.vue';
import Paso_8 from './Paso_8.vue';
import Paso_9 from './Paso_9.vue';
import Paso_10 from './Paso_10.vue';
// import Paso_4Vue from ''

export default {
  components: {
    Paso_1,
    Paso_2,
    Paso_3,
    Paso_4,
    Paso_5,
    Paso_6,
    Paso_7,
    Paso_8,
    Paso_9,
    Paso_10
},
  data() {
    return {
      currentStep: 'Paso_1',
      formData: {}
    };
  },
  methods: {
    nextStep(data) {
      this.formData = { ...this.formData, ...data };
      if (this.currentStep === 'Paso_1') {
        this.currentStep = 'Paso_2';
      } else if (this.currentStep === 'Paso_2') {
        this.currentStep = 'Paso_3';
      } else if (this.currentStep === 'Paso_3') {
        this.currentStep = 'Paso_4';
      } else if (this.currentStep === 'Paso_4') {
        this.currentStep = 'Paso_5';
      } else if (this.currentStep === 'Paso_5') {
        this.currentStep = 'Paso_6';
      } else if (this.currentStep === 'Paso_6') {
        this.currentStep = 'Paso_7';
      } else if (this.currentStep === 'Paso_7') {
        this.currentStep = 'Paso_8';
      } else if (this.currentStep === 'Paso_8') {
        this.currentStep = 'Paso_9';
      } else if (this.currentStep === 'Paso_9') {
        this.currentStep = 'Paso_10';
      } 
    },
    previousStep() {
      if (this.currentStep === 'Paso_2') {
        this.currentStep = 'Paso_1';
      } else if (this.currentStep === 'Paso_3') {
        this.currentStep = 'Paso_2';
      } else if (this.currentStep === 'Paso_4') {
        this.currentStep = 'Paso_3';
      } else if (this.currentStep === 'Paso_5') {
        this.currentStep = 'Paso_4';
      } else if (this.currentStep === 'Paso_6') {
        this.currentStep = 'Paso_5';
      } else if (this.currentStep === 'Paso_7') {
        this.currentStep = 'Paso_6';
      } else if (this.currentStep === 'Paso_8') {
        this.currentStep = 'Paso_7';
      } else if (this.currentStep === 'Paso_9') {
        this.currentStep = 'Paso_8';
      } else if (this.currentStep === 'Paso_10') {
        this.currentStep = 'Paso_9';
      }
    },
    submitForm(data) {
      this.formData = { ...this.formData, ...data };
      console.log(this.formData); // Aquí puedes hacer lo que desees con los datos del formulario
    }
  }
};
</script>

<style >
/* Configuraciones */
body {
  align-items: center;
  background-color: #eee;
  display: flex;
  justify-content: center;
  min-height: 100vh;
}

h2 {
  color: #fff;
}

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


/* Formulario */
.form {
  background-color: #15172b;
  border-radius: 20px;
  box-sizing: border-box;
  padding: 20px;
}
.title {
  color: #fff;
  font-family: sans-serif;
  font-size: 36px;
  font-weight: 600;
  margin-top: 30px;
}
.subtitle {
  color: #fff;
  font-family: sans-serif;
  font-size: 16px;
  font-weight: 600;
  margin-top: 10px;
}
.input-container {
  min-height: 50px;
  position: relative;
  width: 100%;
}
.ic1 {
  margin-top: 40px;
}
.ic2 {
  margin-top: 30px;
}
.input {
  background-color: #303245;
  border-radius: 12px;
  border: 0;
  box-sizing: border-box;
  color: #eee;
  font-size: 18px;
  min-height: 50px;
  outline: 0;
  padding: 8px 20px;
  width: 100%;
}

.input-container:hover {
    border-color: #646cff;
}

.cut {
  background-color: transparent;
  border-radius: 10px;
  height: 20px;
  left: 20px;
  position: absolute;
  top: -20px;
  transform: translateY(0);
  transition: transform 200ms;
  width: 25%;
}

.input:focus ~ .cut,
.input:not(:placeholder-shown) ~ .cut {
  transform: translateY(8px);
  background-color: #15172b;
}

.placeholder {
  color: #65657b;
  font-family: sans-serif;
  left: 20px;
  line-height: 14px;
  pointer-events: none;
  position: absolute;
  transform-origin: 0 50%;
  transition: transform 200ms, color 200ms;
  top: 20px;
}

.input:focus ~ .placeholder,
.input:not(:placeholder-shown) ~ .placeholder {
  transform: translateY(-30px) translateX(10px) scale(0.75);
}

.input:not(:placeholder-shown) ~ .placeholder {
  color: #808097;
}

.input:focus ~ .placeholder {
  color: #2fdc6c;
}

.imput_select {
  display: flex;
  justify-content: end;
  align-items: center;
}

.submit {
  background-color: #08d;
  border-radius: 12px;
  border: 0;
  box-sizing: border-box;
  color: #eee;
  cursor: pointer;
  font-size: 18px;
  height: 50px;
  margin-top: 38px;
  /* // outline: 0; */
  text-align: center;
  width: 100%;
}
.submit:active {
  background-color: #06b;
}

</style>