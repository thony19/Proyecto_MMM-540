<template>
  <div class="form_">
    <h2>Paso 3</h2>

    <div class="input-container ic1 input">
    55 Prefiero discutir cuestiones concretas y no perder el tiempo con pláticas superficiales	
    <div>
        <label>
        <input type="radio" v-model="stepData.input62" name="pregunta55" value="si" required>
        Si
        </label>
        <label>
        <input type="radio" v-model="stepData.input62" name="pregunta55" value="no" required>
        No
        </label>
    </div>
    </div>

    <div class="input-container ic1 input">
    56 Me impaciento cuando me dan explicaciones irrelevantes e incoherentes	
    <div>
        <label>
        <input type="radio" v-model="stepData.input63" name="pregunta56" value="si" required>
        Si
        </label>
        <label>
        <input type="radio" v-model="stepData.input63" name="pregunta56" value="no" required>
        No
        </label>
    </div>
    </div>

    <div class="input-container ic1 input">
    57 Compruebo antes si las cosas funcionan realmente	
    <div>
        <label>
        <input type="radio" v-model="stepData.input64" name="pregunta57" value="si" required>
        Si
        </label>
        <label>
        <input type="radio" v-model="stepData.input64" name="pregunta57" value="no" required>
        No
        </label>
    </div>
    </div>

    <div class="input-container ic1 input">
    58 Hago varios borradores antes de la redacción definitiva de un trabajo	
    <div>
        <label>
        <input type="radio" v-model="stepData.input65" name="pregunta58" value="si" required>
        Si
        </label>
        <label>
        <input type="radio" v-model="stepData.input65" name="pregunta58" value="no" required>
        No
        </label>
    </div>
    </div>

    <div class="input-container ic1 input">
    59 Soy consciente de que en las discusiones ayudo a mantener a los demás centrados en el tema, evitando divagaciones	
    <div>
        <label>
        <input type="radio" v-model="stepData.input66" name="pregunta59" value="si" required>
        Si
        </label>
        <label>
        <input type="radio" v-model="stepData.input66" name="pregunta59" value="no" required>
        No
        </label>
    </div>
    </div>

    <div class="input-container ic1 input">
    60 Observo que, con frecuencia, soy uno/a de los/as más objetivos/as y desapasionados/as en las discusiones	
    <div>
        <label>
        <input type="radio" v-model="stepData.input67" name="pregunta60" value="si" required>
        Si
        </label>
        <label>
        <input type="radio" v-model="stepData.input67" name="pregunta60" value="no" required>
        No
        </label>
    </div>
    </div>

    <div class="input-container ic1 input">
    61 Cuando algo va mal, le quito importancia y trato de hacerlo mejor	
    <div>
        <label>
        <input type="radio" v-model="stepData.input68" name="pregunta61" value="si" required>
        Si
        </label>
        <label>
        <input type="radio" v-model="stepData.input68" name="pregunta61" value="no" required>
        No
        </label>
    </div>
    </div>

    <div class="input-container ic1 input">
    62 Rechazo ideas originales y espontáneas si no las veo prácticas	
    <div>
        <label>
        <input type="radio" v-model="stepData.input69" name="pregunta62" value="si" required>
        Si
        </label>
        <label>
        <input type="radio" v-model="stepData.input69" name="pregunta62" value="no" required>
        No
        </label>
    </div>
    </div>

    <div class="input-container ic1 input">
    63 Me gusta sopesar diversas alternativas antes de tomar una decisión	
    <div>
        <label>
        <input type="radio" v-model="stepData.input70" name="pregunta63" value="si" required>
        Si
        </label>
        <label>
        <input type="radio" v-model="stepData.input70" name="pregunta63" value="no" required>
        No
        </label>
    </div>
    </div>

    <div class="input-container ic1 input">
    64 Con frecuencia miro hacia delante para prever el futuro	
    <div>
        <label>
        <input type="radio" v-model="stepData.input71" name="pregunta64" value="si" required>
        Si
        </label>
        <label>
        <input type="radio" v-model="stepData.input71" name="pregunta64" value="no" required>
        No
        </label>
    </div>
    </div>

    <div class="input-container ic1 input">
    65 En los debates y discusiones prefiero desempeñar un papel secundario antes que ser el/la líder o el/la que más participa	
    <div>
        <label>
        <input type="radio" v-model="stepData.input72" name="pregunta65" value="si" required>
        Si
        </label>
        <label>
        <input type="radio" v-model="stepData.input72" name="pregunta65" value="no" required>
        No
        </label>
    </div>
    </div>

    <div class="input-container ic1 input">
    66 Me molestan las personas que no actúan con lógica	
    <div>
        <label>
        <input type="radio" v-model="stepData.input73" name="pregunta66" value="si" required>
        Si
        </label>
        <label>
        <input type="radio" v-model="stepData.input73" name="pregunta66" value="no" required>
        No
        </label>
    </div>
    </div>

    <div class="input-container ic1 input">
    67 Me resulta incómodo tener que planificar y prever las cosas	
    <div>
        <label>
        <input type="radio" v-model="stepData.input74" name="pregunta67" value="si" required>
        Si
        </label>
        <label>
        <input type="radio" v-model="stepData.input74" name="pregunta67" value="no" required>
        No
        </label>
    </div>
    </div>

    <div class="input-container ic1 input">
    68 Creo que el fin justifica los medios en muchos casos	
    <div>
        <label>
        <input type="radio" v-model="stepData.input75" name="pregunta68" value="si" required>
        Si
        </label>
        <label>
        <input type="radio" v-model="stepData.input75" name="pregunta68" value="no" required>
        No
        </label>
    </div>
    </div>

    <div class="input-container ic1 input">
    69 Suelo reflexionar sobre los asuntos y problemas	
    <div>
        <label>
        <input type="radio" v-model="stepData.input76" name="pregunta69" value="si" required>
        Si
        </label>
        <label>
        <input type="radio" v-model="stepData.input76" name="pregunta69" value="no" required>
        No
        </label>
    </div>
    </div>

    <div class="input-container ic1 input">
    70 El trabajar a conciencia me llena de satisfacción y orgullo	
    <div>
        <label>
        <input type="radio" v-model="stepData.input77" name="pregunta70" value="si" required>
        Si
        </label>
        <label>
        <input type="radio" v-model="stepData.input77" name="pregunta70" value="no" required>
        No
        </label>
    </div>
    </div>

    <div class="input-container ic1 input">
    71 Ante los acontecimientos trato de descubrir los principios y teorías en que se basan	
    <div>
        <label>
        <input type="radio" v-model="stepData.input78" name="pregunta71" value="si" required>
        Si
        </label>
        <label>
        <input type="radio" v-model="stepData.input78" name="pregunta71" value="no" required>
        No
        </label>
    </div>
    </div>

    <div class="input-container ic1 input">
    72 Con tal de conseguir el objetivo que pretendo soy capaz de herir sentimientos ajenos	
    <div>
        <label>
        <input type="radio" v-model="stepData.input79" name="pregunta72" value="si" required>
        Si
        </label>
        <label>
        <input type="radio" v-model="stepData.input79" name="pregunta72" value="no" required>
        No
        </label>
    </div>
    </div>

    <div class="input-container ic1 input">
    73 No me importa hacer todo lo necesario para que sea efectivo mi trabajo	
    <div>
        <label>
        <input type="radio" v-model="stepData.input80" name="pregunta73" value="si" required>
        Si
        </label>
        <label>
        <input type="radio" v-model="stepData.input80" name="pregunta73" value="no" required>
        No
        </label>
    </div>
    </div>

    <div class="input-container ic1 input">
    74 Con frecuencia soy una de las personas que más anima las fiestas	
    <div>
        <label>
        <input type="radio" v-model="stepData.input81" name="pregunta74" value="si" required>
        Si
        </label>
        <label>
        <input type="radio" v-model="stepData.input81" name="pregunta74" value="no" required>
        No
        </label>
    </div>
    </div>

    <div class="input-container ic1 input">
    75 Me aburro enseguida con el trabajo metódico y minucioso	
    <div>
        <label>
        <input type="radio" v-model="stepData.input82" name="pregunta75" value="si" required>
        Si
        </label>
        <label>
        <input type="radio" v-model="stepData.input82" name="pregunta75" value="no" required>
        No
        </label>
    </div>
    </div>

    <div class="input-container ic1 input">
    76 La gente con frecuencia cree que soy poco sensible a sus sentimientos	
    <div>
        <label>
        <input type="radio" v-model="stepData.input83" name="pregunta76" value="si" required>
        Si
        </label>
        <label>
        <input type="radio" v-model="stepData.input83" name="pregunta76" value="no" required>
        No
        </label>
    </div>
    </div>

    <div class="input-container ic1 input">
    77 Suelo dejarme llevar por mis intuiciones	
    <div>
        <label>
        <input type="radio" v-model="stepData.input84" name="pregunta77" value="si" required>
        Si
        </label>
        <label>
        <input type="radio" v-model="stepData.input84" name="pregunta77" value="no" required>
        No
        </label>
    </div>
    </div>

    <div class="input-container ic1 input">
    78 Si trabajo en grupo procuro que se siga un método y un orden	
    <div>
        <label>
        <input type="radio" v-model="stepData.input85" name="pregunta78" value="si" required>
        Si
        </label>
        <label>
        <input type="radio" v-model="stepData.input85" name="pregunta78" value="no" required>
        No
        </label>
    </div>
    </div>

    <div class="input-container ic1 input">
    79 Con frecuencia me interesa averiguar lo que piensa la gente	
    <div>
        <label>
        <input type="radio" v-model="stepData.input86" name="pregunta79" value="si" required>
        Si
        </label>
        <label>
        <input type="radio" v-model="stepData.input86" name="pregunta79" value="no" required>
        No
        </label>
    </div>
    </div>

    <div class="input-container ic1 input">
    80 Esquivo los temas subjetivos, ambiguos y poco claros	
    <div>
        <label>
        <input type="radio" v-model="stepData.input87" name="pregunta80" value="si" required>
        Si
        </label>
        <label>
        <input type="radio" v-model="stepData.input87" name="pregunta80" value="no" required>
        No
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
