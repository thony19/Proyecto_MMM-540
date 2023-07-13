<template>
  <div class="form_">
    <h2>Paso 2</h2>
    <!-- FORMULARIO!! -->
        <div class="input-container ic1 input">
          28 Me gusta analizar y dar vueltas a las cosas
          <div>
            <label>
            <input type="radio" v-model="stepData.input35" name="pregunta28" value="si" required>
              Si
            </label>
            <label>
              <input type="radio" v-model="stepData.input35" name="pregunta28" value="no" required>
              No
            </label>
          </div>
        </div>

        <div class="input-container ic1 input">
          29 Me molesta que la gente no se tome en serio las cosas
          <div>
            <label>
            <input type="radio" v-model="stepData.input36" name="pregunta29" value="si" required>
              Si
            </label>
            <label>
              <input type="radio" v-model="stepData.input36" name="pregunta29" value="no" required>
              No
            </label>
          </div>
        </div>

        <div class="input-container ic1 input">
          30 Me atrae experimentar y practicar las últimas técnicas y novedades
          <div>
            <label>
            <input type="radio" v-model="stepData.input37" name="pregunta30" value="si" required>
              Si
            </label>
            <label>
              <input type="radio" v-model="stepData.input37" name="pregunta30" value="no" required>
              No
            </label>
          </div>
        </div>

        <div class="input-container ic1 input">
          31 Soy cauteloso/a a la hora de sacar conclusiones
          <div>
            <label>
            <input type="radio" v-model="stepData.input38" name="pregunta31" value="si" required>
              Si
            </label>
            <label>
              <input type="radio" v-model="stepData.input38" name="pregunta31" value="no" required>
              No
            </label>
          </div>
        </div>

        <div class="input-container ic1 input">
          32 Prefiero contar con el mayor número de fuentes de información. Cuantos más datos reúna para reflexionar, mejor.
          <div>
            <label>
            <input type="radio" v-model="stepData.input39" name="pregunta32" value="si" required>
              Si
            </label>
            <label>
              <input type="radio" v-model="stepData.input39" name="pregunta32" value="no" required>
              No
            </label>
          </div>
        </div>

        <div class="input-container ic1 input">
          33 Tiendo a ser perfeccionista
          <div>
            <label>
            <input type="radio" v-model="stepData.input40" name="pregunta33" value="si" required>
              Si
            </label>
            <label>
              <input type="radio" v-model="stepData.input40" name="pregunta33" value="no" required>
              No
            </label>
          </div>
        </div>

        <div class="input-container ic1 input">
          34 Prefiero oír las opiniones de los demás antes de exponer la mía
          <div>
            <label>
            <input type="radio" v-model="stepData.input41" name="pregunta34" value="si" required>
              Si
            </label>
            <label>
              <input type="radio" v-model="stepData.input41" name="pregunta34" value="no" required>
              No
            </label>
          </div>
        </div>

        <div class="input-container ic1 input">
          35 Me gusta afrontar la vida espontáneamente y no tener que planificar todo previamente
          <div>
            <label>
            <input type="radio" v-model="stepData.input42" name="pregunta35" value="si" required>
              Si
            </label>
            <label>
              <input type="radio" v-model="stepData.input42" name="pregunta35" value="no" required>
              No
            </label>
          </div>
        </div>

        <div class="input-container ic1 input">
          36 En las discusiones me gusta observar cómo actúan los demás participantes
          <div>
            <label>
            <input type="radio" v-model="stepData.input43" name="pregunta36" value="si" required>
              Si
            </label>
            <label>
              <input type="radio" v-model="stepData.input43" name="pregunta36" value="no" required>
              No
            </label>
          </div>
        </div>

        <div class="input-container ic1 input">
          37 Me siento incómodo/a con las personas calladas y demasiado analíticas
          <div>
            <label>
            <input type="radio" v-model="stepData.input44" name="pregunta37" value="si" required>
              Si
            </label>
            <label>
              <input type="radio" v-model="stepData.input44" name="pregunta37" value="no" required>
              No
            </label>
          </div>
        </div>

        <div class="input-container ic1 input">
          38 Juzgo con frecuencia las ideas de los demás por su valor práctico
          <div>
            <label>
            <input type="radio" v-model="stepData.input45" name="pregunta38" value="si" required>
              Si
            </label>
            <label>
              <input type="radio" v-model="stepData.input45" name="pregunta38" value="no" required>
              No
            </label>
          </div>
        </div>

        <div class="input-container ic1 input">
          39 Me agobio si me obligan a acelerar mucho el trabajo para cumplir un plazo
          <div>
            <label>
            <input type="radio" v-model="stepData.input46" name="pregunta39" value="si" required>
              Si
            </label>
            <label>
              <input type="radio" v-model="stepData.input46" name="pregunta39" value="no" required>
              No
            </label>
          </div>
        </div>

        <div class="input-container ic1 input">
          40 En las reuniones apoyo las ideas prácticas y realistas
          <div>
            <label>
            <input type="radio" v-model="stepData.input47" name="pregunta40" value="si" required>
              Si
            </label>
            <label>
              <input type="radio" v-model="stepData.input47" name="pregunta40" value="no" required>
              No
            </label>
          </div>
        </div>

        <div class="input-container ic1 input">
          41 Es mejor gozar del momento presente que deleitarse pensando en el pasado o en el futuro
          <div>
            <label>
            <input type="radio" v-model="stepData.input48" name="pregunta41" value="si" required>
              Si
            </label>
            <label>
              <input type="radio" v-model="stepData.input48" name="pregunta41" value="no" required>
              No
            </label>
          </div>
        </div>

        <div class="input-container ic1 input">
          42 Me molestan las personas que siempre desean apresurar las cosas
          <div>
            <label>
            <input type="radio" v-model="stepData.input49" name="pregunta42" value="si" required>
              Si
            </label>
            <label>
              <input type="radio" v-model="stepData.input49" name="pregunta42" value="no" required>
              No
            </label>
          </div>
        </div>

        <div class="input-container ic1 input">
          43 Aporto ideas nuevas y espontáneas en los grupos de discusión
          <div>
            <label>
            <input type="radio" v-model="stepData.input50" name="pregunta43" value="si" required>
              Si
            </label>
            <label>
              <input type="radio" v-model="stepData.input50" name="pregunta43" value="no" required>
              No
            </label>
          </div>
        </div>

        <div class="input-container ic1 input">
          44 Pienso que son más consistentes las decisiones fundamentadas en un minucioso análisis que las basadas en la intuición
          <div>
            <label>
            <input type="radio" v-model="stepData.input51" name="pregunta44" value="si" required>
              Si
            </label>
            <label>
              <input type="radio" v-model="stepData.input51" name="pregunta44" value="no" required>
              No
            </label>
          </div>
        </div>

        <div class="input-container ic1 input">
          45 Detecto frecuentemente la inconsistencia y puntos débiles en las argumentaciones de los demás
          <div>
            <label>
            <input type="radio" v-model="stepData.input52" name="pregunta45" value="si" required>
              Si
            </label>
            <label>
              <input type="radio" v-model="stepData.input52" name="pregunta45" value="no" required>
              No
            </label>
          </div>
        </div>

        <div class="input-container ic1 input">
          46 Creo que es preciso saltarse las normas muchas más veces que cumplirlas
          <div>
            <label>
            <input type="radio" v-model="stepData.input53" name="pregunta46" value="si" required>
              Si
            </label>
            <label>
              <input type="radio" v-model="stepData.input53" name="pregunta46" value="no" required>
              No
            </label>
          </div>
        </div>

        <div class="input-container ic1 input">
          47 A menudo caigo en la cuenta de otras formas mejores y más prácticas de hacer las cosas
          <div>
            <label>
            <input type="radio" v-model="stepData.input54" name="pregunta47" value="si" required>
              Si
            </label>
            <label>
              <input type="radio" v-model="stepData.input54" name="pregunta47" value="no" required>
              No
            </label>
          </div>
        </div>

        <div class="input-container ic1 input">
          48 En conjunto hablo más que escucho
          <div>
            <label>
            <input type="radio" v-model="stepData.input55" name="pregunta48" value="si" required>
              Si
            </label>
            <label>
              <input type="radio" v-model="stepData.input55" name="pregunta48" value="no" required>
              No
            </label>
          </div>
        </div>

        <div class="input-container ic1 input">
          49 Prefiero distanciarme de los hechos y observarlos desde otras perspectivas
          <div>
            <label>
            <input type="radio" v-model="stepData.input56" name="pregunta49" value="si" required>
              Si
            </label>
            <label>
              <input type="radio" v-model="stepData.input56" name="pregunta49" value="no" required>
              No
            </label>
          </div>
        </div>

        <div class="input-container ic1 input">
          50 Estoy convencido/a que debe imponerse la lógica y el razonamiento
          <div>
            <label>
            <input type="radio" v-model="stepData.input57" name="pregunta50" value="si" required>
              Si
            </label>
            <label>
              <input type="radio" v-model="stepData.input57" name="pregunta50" value="no" required>
              No
            </label>
          </div>
        </div>

        <div class="input-container ic1 input">
          51 Me gusta buscar nuevas experiencias
          <div>
            <label>
            <input type="radio" v-model="stepData.input58" name="pregunta51" value="si" required>
              Si
            </label>
            <label>
              <input type="radio" v-model="stepData.input58" name="pregunta=51" value="no" required>
              No
            </label>
          </div>
        </div>

        <div class="input-container ic1 input">
          52 Me gusta experimentar y aplicar las cosas
          <div>
            <label>
            <input type="radio" v-model="stepData.input59" name="pregunta52" value="si" required>
              Si
            </label>
            <label>
              <input type="radio" v-model="stepData.input59" name="pregunta52" value="no" required>
              No
            </label>
          </div>
        </div>

        <div class="input-container ic1 input">
          53 Pienso que debemos llegar pronto al grano, al meollo de los temas.
          <div>
            <label>
            <input type="radio" v-model="stepData.input60" name="pregunta53" value="si" required>
              Si
            </label>
            <label>
              <input type="radio" v-model="stepData.input60" name="pregunta53" value="no" required>
              No
            </label>
          </div>
        </div>

        <div class="input-container ic1 input">
          54 Siempre trato de conseguir conclusiones e ideas claras
          <div>
            <label>
            <input type="radio" v-model="stepData.input61" name="pregunta54" value="si" required>
              Si
            </label>
            <label>
              <input type="radio" v-model="stepData.input61" name="pregunta54" value="no" required>
              No
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
        // input2: ''
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
