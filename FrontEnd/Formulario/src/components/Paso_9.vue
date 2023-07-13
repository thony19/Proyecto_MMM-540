<template>
  <div class="form_">
    <h2>Paso 9</h2>
    
    <div class="input-container ic1 input">
      Si escogiste esta opción, selecciona el área a la pertenece la carrera que deseas estudiar
      <div style="text-align: justify;">
        <label>
          <input type="radio" v-model="stepData.input9_1" name="input9_1" value="Educación (Formación de personal docente y ciencias de la educación)" required>
          Educación (Formación de personal docente y ciencias de la educación).
        </label>
        <br>
        <label>
          <input type="radio" v-model="stepData.input9_1" name="input9_1" value="Humanidades y artes" required>
          Humanidades y artes.
        </label>
        <br>
        <label>
          <input type="radio" v-model="stepData.input9_1" name="input9_1" value="Ciencias sociales, educación comercial y derecho (Periodismo e información, Educación comercial y administración, derecho)" required>
          Ciencias sociales, educación comercial y derecho (Periodismo e información, Educación comercial y administración, derecho).
        </label>
        <br>
        <label>
          <input type="radio" v-model="stepData.input9_1" name="input9_1" value="Ciencias (Ciencias de la vida, físicas, Matemáticas y estadística, informática)" required>
          Ciencias (Ciencias de la vida, físicas, Matemáticas y estadística, informática).
        </label>
        <label>
          <input type="radio" v-model="stepData.input9_1" name="input9_1" value="Ingeniería, industria y construcción" required>
          Ingeniería, industria y construcción.
        </label>
        <br>
        <label>
          <input type="radio" v-model="stepData.input9_1" name="input9_1" value="Agricultura (agronomía, veterinaria, silvicultura y pesca)" required>
          Agricultura (agronomía, veterinaria, silvicultura y pesca).
        </label>
        <br>
        <label>
          <input type="radio" v-model="stepData.input9_1" name="input9_1" value="Salud y servicios sociales (Medicina, servicios sociales)" required>
          Salud y servicios sociales (Medicina, servicios sociales).
        </label>
        <br>
        <label>
          <input type="radio" v-model="stepData.input9_1" name="input9_1" value="Servicios (Hotelería y turismo, oficiales de marina, protección del medio ambiente, servicios de seguridad)" required>
          Servicios (Hotelería y turismo, oficiales de marina, protección del medio ambiente, servicios de seguridad).
        </label>
      </div>
    </div>

    <button @click="previousStep">Anterior</button>
    <button @click="nextStep">Siguiente</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      stepData: {
        
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
