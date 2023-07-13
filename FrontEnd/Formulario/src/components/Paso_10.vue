<template>
  <div class="form_">
    <h2>Paso 10</h2>
    
    <div class="input-container ic1 input">
      ¿Por qué crees importante estudiar una carrera universitaria?
      <div style="text-align: justify;">
        <label>
          <input type="radio" v-model="stepData.input10_1" name="input10_1" value="Para tener mejores oportunidades de empleo" required>
          Para tener mejores oportunidades de empleo.
        </label>
        <br>
        <label>
          <input type="radio" v-model="stepData.input10_1" name="input10_1" value="Para tener oportunidad de hacer amistades" required>
          Para tener oportunidad de hacer amistades.
        </label>
        <br>
        <label>
          <input type="radio" v-model="stepData.input10_1" name="input10_1" value="Ciencias sociales, educación comercial y derecho (Periodismo e información, Educación comercial y administración, derecho)" required>
          Ciencias sociales, educación comercial y derecho (Periodismo e información, Educación comercial y administración, derecho).
        </label>
        <br>
        <label>
          <input type="radio" v-model="stepData.input10_1" name="input10_1" value="Ciencias (Ciencias de la vida, físicas, Matemáticas y estadística, informática)" required>
          Ciencias (Ciencias de la vida, físicas, Matemáticas y estadística, informática).
        </label>
        <label>
          <input type="radio" v-model="stepData.input10_1" name="input10_1" value="Para tener formas de pensar, vivir y abrir puertas del mundo" required>
          Para tener formas de pensar, vivir y abrir puertas del mundo.
        </label>
        <br>
        <label>
          <input type="radio" v-model="stepData.input10_1" name="input10_1" value="Tener otra visión de las cosas" required>
          Tener otra visión de las cosas.
        </label>
        <br>
        <label>
          <input type="radio" v-model="stepData.input10_1" name="input10_1" value="Salud y servicios sociales (Medicina, servicios sociales)" required>
          Salud y servicios sociales (Medicina, servicios sociales).
        </label>
        <br>
        <label>
          <input type="radio" v-model="stepData.input10_1" name="input10_1" value="Capacitarme para trabajar en lo que me gusta" required>
          Capacitarme para trabajar en lo que me gusta.
        </label>
        <br>
        <label>
          <input type="radio" v-model="stepData.input10_1" name="input10_1" value="Porque mi padres me exigen que tenga un título universitario" required>
          Porque mi padres me exigen que tenga un título universitario.
        </label>
      </div>
    </div>

    <div class="input-container ic1 input">
      ¿Dónde quieres trabajar?
      <div style="text-align: justify;">
        <label>
          <input type="radio" v-model="stepData.input10_2" name="input10_2" value="En una empresa, dedicándome al área que más me llama la atención" required>
          En una empresa, dedicándome al área que más me llama la atención.
        </label>
        <br>
        <label>
          <input type="radio" v-model="stepData.input10_2" name="input10_2" value="Donde me den trabajo" required>
          Donde me den trabajo.
        </label>
      </div>
    </div>

    <div class="input-container ic1 input">
      ¿Por qué crees que importante estudiar una carrera universitaria?
      <div style="text-align: justify;">
        <label>
          <input type="radio" v-model="stepData.input10_3" name="input10_3" value="Porque mis padres me exigen que tenga el título" required>
          Porque mis padres me exigen que tenga el título.
        </label>
        <br>
        <label>
          <input type="radio" v-model="stepData.input10_3" name="input10_3" value="Porque de ésta manera tengo más oportunidades de empleo" required>
          Porque de ésta manera tengo más oportunidades de empleo.
        </label>
      </div>
    </div>

    <button @click="previousStep">Anterior</button>
    <button @click="submitForm">Enviar</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      stepData: {
        // input4: "",
      },
    };
  },
  methods: {
    previousStep() {
      this.$emit("previous");
    },
    submitForm() {
      this.$emit("submit", this.stepData);
    },
  },
};
</script>