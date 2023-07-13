<template>
  <div class="form_">
    <h2>Paso 8</h2>
    <h3>Relación con las TIC's</h3>
    <h4>Recuerda, las TIC's es la abreviatura de Tecnologías de la Información y Comunicación (teléfonos, televisores, computadoras, tablets, entre otros, junto con todos sus usos y aplicaciones)</h4>

    <!-- Pregunta 1 -->
    <div class="input-container ic1 input">
      1 Al usar las TIC's, tu puedes Participar en un foro/chat
      <div>
        <label>
          <input type="radio" v-model="stepData.RelTIC1" name="RelTIC1" value="si" required>
          Si
        </label>
        <label>
          <input type="radio" v-model="stepData.RelTIC1" name="RelTIC1" value="no" required>
          No
        </label>
      </div>
    </div>

    <!-- Pregunta 2 -->
    <div class="input-container ic1 input">
      2 Al usar las TIC's, tu puedes Buscar en internet
      <div>
        <label>
          <input type="radio" v-model="stepData.RelTIC2" name="RelTIC2" value="si" required>
          Si
        </label>
        <label>
          <input type="radio" v-model="stepData.RelTIC2" name="RelTIC2" value="no" required>
          No
        </label>
      </div>
    </div>

    <!-- Pregunta 3 -->
    <div class="input-container ic1 input">
      3 Al usar las TIC's, tu puedes Enviar un e-mail
      <div>
        <label>
          <input type="radio" v-model="stepData.RelTIC3" name="RelTIC3" value="si" required>
          Si
        </label>
        <label>
          <input type="radio" v-model="stepData.RelTIC3" name="RelTIC3" value="no" required>
          No
        </label>
      </div>
    </div>

    <!-- Pregunta 4 -->
    <div class="input-container ic1 input">
      4 Al usar las TIC's, tu puedes Hacer dibujos
      <div>
        <label>
          <input type="radio" v-model="stepData.RelTIC4" name="RelTIC4" value="si" required>
          Si
        </label>
        <label>
          <input type="radio" v-model="stepData.RelTIC4" name="RelTIC4" value="no" required>
          No
        </label>
      </div>
    </div>

    <!-- Pregunta 5 -->
    <div class="input-container ic1 input">
      5 Al usar las TIC's, tu puedes Guardar documentos en carpetas
      <div>
        <label>
          <input type="radio" v-model="stepData.RelTIC5" name="RelTIC5" value="si" required>
          Si
        </label>
        <label>
          <input type="radio" v-model="stepData.RelTIC5" name="RelTIC5" value="no" required>
          No
        </label>
      </div>
    </div>

    <!-- Pregunta 6 -->
    <div class="input-container ic1 input">
      1 Al usar las TIC's, tu puedes Navegar de manera segura
      <div>
        <label>
          <input type="radio" v-model="stepData.RelTIC6" name="RelTIC6" value="si" required>
          Si
        </label>
        <label>
          <input type="radio" v-model="stepData.RelTIC6" name="RelTIC6" value="no" required>
          No
        </label>
      </div>
    </div>

    <!-- Pregunta 7 -->
    <div class="input-container ic1 input">
      7 Al usar las TIC's, tu puedes Programar
      <div>
        <label>
          <input type="radio" v-model="stepData.RelTIC7" name="RelTIC7" value="si" required>
          Si
        </label>
        <label>
          <input type="radio" v-model="stepData.RelTIC7" name="RelTIC7" value="no" required>
          No
        </label>
      </div>
    </div>

    <!-- Pregunta 8 -->
    <div class="input-container ic1 input">
      8 Al usar las TIC's, tu puedes Usar apps para aprender
      <div>
        <label>
          <input type="radio" v-model="stepData.RelTIC8" name="RelTIC8" value="si" required>
          Si
        </label>
        <label>
          <input type="radio" v-model="stepData.RelTIC8" name="RelTIC8" value="no" required>
          No
        </label>
      </div>
    </div>

    <!-- Pregunta 9 -->
    <div class="input-container ic1 input">
      9 Piensas que el uso de las TIC's Hace que sea más fácil aprender
      <div>
        <label>
          <input type="radio" v-model="stepData.RelTIC9" name="RelTIC9" value="si" required>
          Si
        </label>
        <label>
          <input type="radio" v-model="stepData.RelTIC9" name="RelTIC9" value="no" required>
          No
        </label>
      </div>
    </div>

    <!-- Pregunta 10 -->
    <div class="input-container ic1 input">
      10 Piensas que el uso de las TIC's Hace que sea más interesante
      <div>
        <label>
          <input type="radio" v-model="stepData.RelTIC10" name="RelTIC10" value="si" required>
          Si
        </label>
        <label>
          <input type="radio" v-model="stepData.RelTIC10" name="RelTIC10" value="no" required>
          No
        </label>
      </div>
    </div>

    <!-- Pregunta 11 -->
    <div class="input-container ic1 input">
      11 Piensas que el uso de las TIC's Hace que me pueda concentrar
      <div>
        <label>
          <input type="radio" v-model="stepData.RelTIC11" name="RelTIC11" value="si" required>
          Si
        </label>
        <label>
          <input type="radio" v-model="stepData.RelTIC11" name="RelTIC11" value="no" required>
          No
        </label>
      </div>
    </div>

    <!-- Pregunta 12 -->
    <div class="input-container ic1 input">
      12 Me gusta aprender más cosas de las TIC
      <div>
        <label>
          <input type="radio" v-model="stepData.RelTIC12" name="RelTIC12" value="si" required>
          Si
        </label>
        <label>
          <input type="radio" v-model="stepData.RelTIC12" name="RelTIC12" value="no" required>
          No
        </label>
      </div>
    </div>

    <!-- Pregunta 13 -->
    <div class="input-container ic1 input">
      13 Prefiero trabajar con las TIC
      <div>
        <label>
          <input type="radio" v-model="stepData.RelTIC13" name="RelTIC13" value="si" required>
          Si
        </label>
        <label>
          <input type="radio" v-model="stepData.RelTIC13" name="RelTIC13" value="no" required>
          No
        </label>
      </div>
    </div>

    <!-- Pregunta 14 -->
    <div class="input-container ic1 input">
      14 ¿Cómo te ves en 3 años?
      <div style="text-align: justify;">
        <label>
          <input type="radio" v-model="stepData.RelTIC14" name="RelTIC14" value="Estudiando" required>
          Estudiando
        </label>
        <br>
        <label>
          <input type="radio" v-model="stepData.RelTIC14" name="RelTIC14" value="Trabajando" required>
          Trabajando
        </label>
      </div>
    </div>

    <!-- Pregunta 15 -->
    <div class="input-container ic1 input">
      15 ¿Cómo te ves en 6 años?
      <div style="text-align: justify;">
        <label>
          <input type="radio" v-model="stepData.RelTIC15" name="RelTIC15" value="Estudiando" required>
          Estudiando
        </label>
        <br>
        <label>
          <input type="radio" v-model="stepData.RelTIC15" name="RelTIC15" value="Contratado en una empresa" required>
          Contratado en una empresa
        </label>
        <label>
          <input type="radio" v-model="stepData.RelTIC15" name="RelTIC15" value="Dirigiendo una empresa" required>
          Dirigiendo una empresa
        </label>
        <br>
        <label>
          <input type="radio" v-model="stepData.RelTIC15" name="RelTIC15" value="Con un negocio propio" required>
          Con un negocio propio
        </label>
      </div>
    </div>

    <!-- Pregunta 16 -->
    <div class="input-container ic1 input">
      16 ¿Sabes que carrera quieres estudiar?
      <div style="text-align: justify;">
        <label>
          <input type="radio" v-model="stepData.RelTIC16" name="RelTIC16" value="No lo sé, todavía no me decido" required>
          No lo sé, todavía no me decido
        </label>
        <br>
        <label>
          <input type="radio" v-model="stepData.RelTIC16" name="RelTIC16" value="Desde pequeño(a) siempre he sabido lo que quiero estudiar" required>
          Desde pequeño(a) siempre he sabido lo que quiero estudiar
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
