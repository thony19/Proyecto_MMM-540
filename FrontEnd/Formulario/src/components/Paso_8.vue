<template>
  <div class="form_">
    <h2>Paso 6</h2>
<!-- Pregunta 133 -->
<div class="input-container ic1 input">
  133 Me gusta comunicarme con mis amigos a través de cartas, e.mails o mensajes.
  <div>
    <label>
      <input type="radio" v-model="stepData.input140" name="pregunta133" value="si" required>
      Si
    </label>
    <label>
      <input type="radio" v-model="stepData.input140" name="pregunta133" value="no" required>
      No
    </label>
  </div>
</div>

<!-- Pregunta 134 -->
<div class="input-container ic1 input">
  134 Me resulta fácil explicar mis ideas a otros.
  <div>
    <label>
      <input type="radio" v-model="stepData.input141" name="pregunta134" value="si" required>
      Si
    </label>
    <label>
      <input type="radio" v-model="stepData.input141" name="pregunta134" value="no" required>
      No
    </label>
  </div>
</div>

<!-- Pregunta 135 -->
<div class="input-container ic1 input">
  135 Tengo buena memoria para los lugares, fechas, nombres, etc…
  <div>
    <label>
      <input type="radio" v-model="stepData.input142" name="pregunta135" value="si" required>
      Si
    </label>
    <label>
      <input type="radio" v-model="stepData.input142" name="pregunta135" value="no" required>
      No
    </label>
  </div>
</div>

<!-- Pregunta 136 -->
<div class="input-container ic1 input">
  136 Pasatiempos como los crucigramas y las sopas de letras son divertidos.
  <div>
    <label>
      <input type="radio" v-model="stepData.input143" name="pregunta136" value="si" required>
      Si
    </label>
    <label>
      <input type="radio" v-model="stepData.input143" name="pregunta136" value="no" required>
      No
    </label>
  </div>
</div>

<!-- Pregunta 137 -->
<div class="input-container ic1 input">
  137 Escribo por placer.
  <div>
    <label>
      <input type="radio" v-model="stepData.input144" name="pregunta137" value="si" required>
      Si
    </label>
    <label>
      <input type="radio" v-model="stepData.input144" name="pregunta137" value="no" required>
      No
    </label>
  </div>
</div>

<!-- Pregunta 138 -->
<div class="input-container ic1 input">
  138 Me gusta jugar con palabras como los anagramas, las palabras encadenadas etc…
  <div>
    <label>
      <input type="radio" v-model="stepData.input145" name="pregunta138" value="si" required>
      Si
    </label>
    <label>
      <input type="radio" v-model="stepData.input145" name="pregunta138" value="no" required>
      No
    </label>
  </div>
</div>

<!-- Pregunta 139 -->
<div class="input-container ic1 input">
  139 Me interesan los idiomas.
  <div>
    <label>
      <input type="radio" v-model="stepData.input146" name="pregunta139" value="si" required>
      Si
    </label>
    <label>
      <input type="radio" v-model="stepData.input146" name="pregunta139" value="no" required>
      No
    </label>
  </div>
</div>

<!-- Pregunta 140 -->
<div class="input-container ic1 input">
  140 Me gusta participar en los debates y en las exposiciones en público.
  <div>
    <label>
      <input type="radio" v-model="stepData.input147" name="pregunta140" value="si" required>
      Si
    </label>
    <label>
      <input type="radio" v-model="stepData.input147" name="pregunta140" value="no" required>
      No
    </label>
  </div>
</div>

<!-- Pregunta 141 -->
<div class="input-container ic1 input">
  141 Me gusta saber y replantearme mis creencias morales.
  <div>
    <label>
      <input type="radio" v-model="stepData.input148" name="pregunta141" value="si" required>
      Si
    </label>
    <label>
      <input type="radio" v-model="stepData.input148" name="pregunta141" value="no" required>
      No
    </label>
  </div>
</div>

<!-- Pregunta 142 -->
<div class="input-container ic1 input">
  142 Aprendo mejor cuando el tema “toca mis sentimientos”.
  <div>
    <label>
      <input type="radio" v-model="stepData.input149" name="pregunta142" value="si" required>
      Si
    </label>
    <label>
      <input type="radio" v-model="stepData.input149" name="pregunta142" value="no" required>
      No
    </label>
  </div>
</div>

<!-- Pregunta 143 -->
<div class="input-container ic1 input">
  143 La justicia es importante para mí.
  <div>
    <label>
      <input type="radio" v-model="stepData.input150" name="pregunta143" value="si" required>
      Si
    </label>
    <label>
      <input type="radio" v-model="stepData.input150" name="pregunta143" value="no" required>
      No
    </label>
  </div>
</div>

<!-- Pregunta 144 -->
<div class="input-container ic1 input">
  144 Suelo aprender de los errores y aciertos que he tenido en mi vida.
  <div>
    <label>
      <input type="radio" v-model="stepData.input151" name="pregunta144" value="si" required>
      Si
    </label>
    <label>
      <input type="radio" v-model="stepData.input151" name="pregunta144" value="no" required>
      No
    </label>
  </div>
</div>

<!-- Pregunta 145 -->
<div class="input-container ic1 input">
  145 Puedo expresar como me siento fácilmente.
  <div>
    <label>
      <input type="radio" v-model="stepData.input152" name="pregunta145" value="si" required>
      Si
    </label>
    <label>
      <input type="radio" v-model="stepData.input152" name="pregunta145" value="no" required>
      No
    </label>


  </div>
</div>

<!-- Pregunta 146 -->
<div class="input-container ic1 input">
  146 Trabajar solo puede ser tan productivo como trabajar en grupo.
  <div>
    <label>
      <input type="radio" v-model="stepData.input153" name="pregunta146" value="si" required>
      Si
    </label>
    <label>
      <input type="radio" v-model="stepData.input153" name="pregunta146" value="no" required>
      No
    </label>
  </div>
</div>

<!-- Pregunta 147 -->
<div class="input-container ic1 input">
  147 Antes de aceptar hacer algo necesito saber por qué tengo que hacerlo.
  <div>
    <label>
      <input type="radio" v-model="stepData.input154" name="pregunta147" value="si" required>
      Si
    </label>
    <label>
      <input type="radio" v-model="stepData.input154" name="pregunta147" value="no" required>
      No
    </label>
  </div>
</div>

<!-- Pregunta 148 -->
<div class="input-container ic1 input">
  148 Cuando creo que algo vale la pena me esfuerzo al cien por cien.
  <div>
    <label>
      <input type="radio" v-model="stepData.input155" name="pregunta148" value="si" required>
      Si
    </label>
    <label>
      <input type="radio" v-model="stepData.input155" name="pregunta148" value="no" required>
      No
    </label>
  </div>
</div>

<!-- Pregunta 149 -->
<div class="input-container ic1 input">
  149 Me gusta participar de las causas que ayudan a otros.
  <div>
    <label>
      <input type="radio" v-model="stepData.input156" name="pregunta149" value="si" required>
      Si
    </label>
    <label>
      <input type="radio" v-model="stepData.input156" name="pregunta149" value="no" required>
      No
    </label>
  </div>
</div>

<!-- Pregunta 150 -->
<div class="input-container ic1 input">
  150 Me afectan e importan los comentarios que los demás hagan de mí.
  <div>
    <label>
      <input type="radio" v-model="stepData.input157" name="pregunta150" value="si" required>
      Si
    </label>
    <label>
      <input type="radio" v-model="stepData.input157" name="pregunta150" value="no" required>
      No
    </label>
  </div>
</div>

<!-- Pregunta 151 -->
<div class="input-container ic1 input">
  151 Puedo imaginar ideas en mi mente.
  <div>
    <label>
      <input type="radio" v-model="stepData.input158" name="pregunta151" value="si" required>
      Si
    </label>
    <label>
      <input type="radio" v-model="stepData.input158" name="pregunta151" value="no" required>
      No
    </label>
  </div>
</div>

<!-- Pregunta 152 -->
<div class="input-container ic1 input">
  152 Reordenar y cambiar la decoración de mi cuarto es divertido para mí.
  <div>
    <label>
      <input type="radio" v-model="stepData.input159" name="pregunta152" value="si" required>
      Si
    </label>
    <label>
      <input type="radio" v-model="stepData.input159" name="pregunta152" value="no" required>
      No
    </label>
  </div>
</div>

<!-- Pregunta 153 -->
<div class="input-container ic1 input">
  153 Me resulta fácil interpretar y leer mapas y diagramas.
  <div>
    <label>
      <input type="radio" v-model="stepData.input160" name="pregunta153" value="si" required>
      Si
    </label>
    <label>
      <input type="radio" v-model="stepData.input160" name="pregunta153" value="no" required>
      No
    </label>
  </div>
</div>

<!-- Pregunta 154 -->
<div class="input-container ic1 input">
  154 Me gusta ver películas, diapositivas y otras presentaciones visuales.
  <div>
    <label>
      <input type="radio" v-model="stepData.input161" name="pregunta154" value="si" required>
      Si
    </label>
    <label>
      <input type="radio" v-model="stepData.input161" name="pregunta154" value="no" required>
      No
    </label>
  </div>
</div>

<!-- Pregunta 155 -->
<div class="input-container ic1 input">
  155 Aprendo más a través de imágenes que leyendo.
  <div>
    <label>
      <input type="radio" v-model="stepData.input162" name="pregunta155" value="si" required>
      Si
    </label>
    <label>
      <input type="radio" v-model="stepData.input162" name="pregunta155" value="no" required>
      No
    </label>
  </div>
</div>

<!-- Pregunta 156 -->
<div class="input-container ic1 input">
  156 Los rompecabezas y puzzles en tres dimensiones me divierten mucho.
  <div>
    <label>
      <input type="radio" v-model="stepData.input163" name="pregunta156" value="si" required>
      Si
    </label>
    <label>
      <input type="radio" v-model="stepData.input163" name="pregunta156" value="no" required>
      No
    </label>
  </div>
</div>

<!-- Pregunta 157 -->
<div class="input-container ic1 input">
  157 Suelo dibujar en los libros y cuadernos sin darme cuenta.
  <div>
    <label>
      <input type="radio" v-model="stepData.input164" name="pregunta157" value="si" required>
      Si
    </label>
    <label>
      <input type="radio" v-model="stepData.input164" name="pregunta157" value="no" required>
      No
    </label>
  </div>
</div>

<!-- Pregunta 158 -->
<div class="input-container ic1 input">
  158 Pintar y dibujar son cosas divertidas para mí.
  <div>
    <label>
      <input type="radio" v-model="stepData.input165" name="pregunta158" value="si" required>
      Si
    </label>
    <label>
      <input type

="radio" v-model="stepData.input165" name="pregunta158" value="no" required>
      No
    </label>
  </div>
</div>

<!-- Pregunta 159 -->
<div class="input-container ic1 input">
  159 Comprendo mejor las cosas a través de gráficos y tablas.
  <div>
    <label>
      <input type="radio" v-model="stepData.input166" name="pregunta159" value="si" required>
      Si
    </label>
    <label>
      <input type="radio" v-model="stepData.input166" name="pregunta159" value="no" required>
      No
    </label>
  </div>
</div>

<!-- Pregunta 160 -->
<div class="input-container ic1 input">
  160 Recuerdo las cosas imaginándomelas visualmente.
  <div>
    <label>
      <input type="radio" v-model="stepData.input167" name="pregunta160" value="si" required>
      Si
    </label>
    <label>
      <input type="radio" v-model="stepData.input167" name="pregunta160" value="no" required>
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
