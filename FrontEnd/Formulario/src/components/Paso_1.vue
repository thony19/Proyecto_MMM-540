<template>
  <div class="form_">
    <h2>Paso 1</h2>
    <!-- <input type="text" v-model="stepData.input1" placeholder="Ingrese su nombre"> -->

    <h2 class="title">Estilos de Aprendizaje e Inteligencias múltiples</h2>
      <p class="subtitle">Estimado/a alumno/a:
          <br>
          De antemano agradecemos tu valiosa colaboración al responder este cuestionario que forma parte de una reflexión más amplia que pretende contribuir a mejorar la calidad de la educación científica en nuestro país. 
          <br>
          Toda la información que nos aportes será de uso estrictamente confidencial.
      </p>
      <div class="input-container ic1" >
          <input class="input" placeholder=" " type="text" v-model="stepData.input1" required>
          <div class="cut"></div>
          <label for="firstname" class="placeholder">Primer Nombre</label>
        </div>
        <div class="input-container ic1">
          <input class="input" placeholder=" " type="text" v-model="stepData.input2" required>
          <div class="cut"></div>
          <label for="lastname" class="placeholder">Segundo Nombre</label>
        </div>
        <div class="input-container ic1" >
          <input class="input" placeholder=" " type="email" v-model="stepData.input3" required>
          <div class="cut"></div>
          <label for="firstname" class="placeholder">Correo Electrónico</label>
        </div>
        <div class="input-container ic1">
          <input class="input" placeholder=" " type="date" v-model="stepData.input4" required>
          <div class="cut"></div>
          <label for="lastname" class="placeholder">Fecha de Nacimiento</label>
        </div>
        <div class="input-container ic1 input imput_select">
          <select v-model="stepData.input5" required>
            <option value="" disabled selected>Seleccione una opción</option>
            <option value="opcion1">Femenino</option>
            <option value="opcion2">Masculino</option>
            <option value="opcion3">Otro:</option>
          </select>
          <label for="lastname" class="placeholder">Selecciona tu Género</label>
        </div>
        <div class="input-container ic1 input imput_select">
          <select v-model="stepData.input6" required>
            <option value="" disabled selected>Seleccione una opción</option>
            <option value="opcion1">Estudiante</option>
            <option value="opcion2">Docente</option>
            <option value="opcion3">Club Deportivo de la Universidad</option>
            <option value="opcion3">Publico General</option>
          </select>
          <label for="lastname" class="placeholder">Selecciona tu Grupo</label>
        </div>
        <div class="input-container ic1">
          <input class="input" placeholder=" " type="text" v-model="stepData.input7" required>
          <div class="cut"></div>
          <label for="lastname" class="placeholder">Escribe tu especialidad</label>
        </div>
        <div class="input-container ic1 input" style="padding: 15px;">
          Agradecimiento<br>
          Reiteramos nuestros agradecimientos a tu valiosa colaboración personal al responder este test que forma
          parte de un proyecto de investigación educativa con el fin de fortalecer la educación científica de nuestro país.<br>
        </div>
        <div class="input-container ic1 input" style="padding: 15px;">
          Instrucciones Cuestionario Honey-Alonso<br>
          Instrucciones para responder al cuestionario:<br><br>

          * Este cuestionario ha sido diseñado para identificar tu estilo preferido de aprender. NO es un test de inteligencia, ni de personalidad.<br>
          * No hay límite de tiempo para contestar el cuestionario.<br>
          * No hay respuestas correctas o erróneas. Será útil en la medida que seas<br>
          sincero/a en tus respuestas.<br>
          * Si estás más de acuerdo que en desacuerdo con la frase, señala en Si.<br>
            Si, por el contrario, estás más en desacuerdo que de acuerdo, señala en No.<br>
          * Por favor, contesta a todas las afirmaciones<br>
        </div>

        <!-- FORMULARIO!! -->
        <div class="input-container ic1 input">
          1 Tengo fama de decir lo que pienso claramente y sin rodeos
          <div>
            <label>
            <input type="radio" v-model="stepData.input8" name="pregunta1" value="si" required>
              Si
            </label>
            <label>
              <input type="radio" v-model="stepData.input8" name="pregunta1" value="no" required>
              No
            </label>
          </div>
        </div>

        <div class="input-container ic1 input">
          2 Estoy seguro/a de lo que es bueno y lo que es malo, lo que está bien y lo que está mal.
          <div>
            <label>
            <input type="radio" v-model="stepData.input9" name="pregunta2" value="si" required>
              Si
            </label>
            <label>
              <input type="radio" v-model="stepData.input9" name="pregunta2" value="no" required>
              No
            </label>
          </div>
        </div>

        <div class="input-container ic1 input">
          3 Muchas veces actúo sin mirar las consecuencias
          <div>
            <label>
            <input type="radio" v-model="stepData.input10" name="pregunta3" value="si" required>
              Si
            </label>
            <label>
              <input type="radio" v-model="stepData.input10" name="pregunta3" value="no" required>
              No
            </label>
          </div>
        </div>

        <div class="input-container ic1 input">
          4 Normalmente trato de resolver los problemas metódicamente y paso a paso
          <div>
            <label>
            <input type="radio" v-model="stepData.input11" name="pregunta4" value="si" required>
              Si
            </label>
            <label>
              <input type="radio" v-model="stepData.input11" name="pregunta4" value="no" required>
              No
            </label>
          </div>
        </div>

        <div class="input-container ic1 input">
          5 Creo que los formalismos coartan y limitan la actuación libre de las personas
          <div>
            <label>
            <input type="radio" v-model="stepData.input12" name="pregunta5" value="si" required>
              Si
            </label>
            <label>
              <input type="radio" v-model="stepData.input12" name="pregunta5" value="no" required>
              No
            </label>
          </div>
        </div>

        <div class="input-container ic1 input">
          6 Me interesa saber cuáles son los sistemas de valores de los demás y con qué criterios actúan
          <div>
            <label>
            <input type="radio" v-model="stepData.input13" name="pregunta6" value="si" required>
              Si
            </label>
            <label>
              <input type="radio" v-model="stepData.input13" name="pregunta6" value="no" required>
              No
            </label>
          </div>
        </div>

        <div class="input-container ic1 input">
          7 Pienso que el actuar intuitivamente puede ser siempre tan válido como actuar reflexivamente.
          <div>
            <label>
            <input type="radio" v-model="stepData.input14" name="pregunta7" value="si" required>
              Si
            </label>
            <label>
              <input type="radio" v-model="stepData.input14" name="pregunta7" value="no" required>
              No
            </label>
          </div>
        </div>

        <div class="input-container ic1 input">
          8 Creo que lo más importante es que las cosas funcionen
          <div>
            <label>
            <input type="radio" v-model="stepData.input15" name="pregunta8" value="si" required>
              Si
            </label>
            <label>
              <input type="radio" v-model="stepData.input15" name="pregunta8" value="no" required>
              No
            </label>
          </div>
        </div>

        <div class="input-container ic1 input">
          9 Procuro estar al tanto de lo que ocurre aquí y ahora
          <div>
            <label>
            <input type="radio" v-model="stepData.input16" name="pregunta9" value="si" required>
              Si
            </label>
            <label>
              <input type="radio" v-model="stepData.input16" name="pregunta9" value="no" required>
              No
            </label>
          </div>
        </div>

        <div class="input-container ic1 input">
          10 Disfruto cuando tengo tiempo para preparar mi trabajo y realizarlo a conciencia
          <div>
            <label>
            <input type="radio" v-model="stepData.input17" name="pregunta10" value="si" required>
              Si
            </label>
            <label>
              <input type="radio" v-model="stepData.input17" name="pregunta10" value="no" required>
              No
            </label>
          </div>
        </div>

        <div class="input-container ic1 input">
          11 Estoy a gusto siguiendo un orden en las comidas, en el estudio, haciendo ejercicio regularmente
          <div>
            <label>
            <input type="radio" v-model="stepData.input18" name="pregunta11" value="si" required>
              Si
            </label>
            <label>
              <input type="radio" v-model="stepData.input18" name="pregunta11" value="no" required>
              No
            </label>
          </div>
        </div>

        <div class="input-container ic1 input">
          12 Cuando escucho una nueva idea enseguida comienzo a pensar cómo ponerla en práctica
          <div>
            <label>
            <input type="radio" v-model="stepData.input19" name="pregunta12" value="si" required>
              Si
            </label>
            <label>
              <input type="radio" v-model="stepData.input19" name="pregunta12" value="no" required>
              No
            </label>
          </div>
        </div>

        <div class="input-container ic1 input">
          13 Prefiero las ideas originales y novedosas aunque no sean prácticas
          <div>
            <label>
            <input type="radio" v-model="stepData.input20" name="pregunta13" value="si" required>
              Si
            </label>
            <label>
              <input type="radio" v-model="stepData.input20" name="pregunta13" value="no" required>
              No
            </label>
          </div>
        </div>

        <div class="input-container ic1 input">
          14 Admito y me ajusto a las normas sólo si me sirven para lograr mis objetivos
          <div>
            <label>
            <input type="radio" v-model="stepData.input21" name="pregunta14" value="si" required>
              Si
            </label>
            <label>
              <input type="radio" v-model="stepData.input21" name="pregunta14" value="no" required>
              No
            </label>
          </div>
        </div>

        <div class="input-container ic1 input">
          15 Normalmente encajo bien con personas reflexivas, y me cuesta sintonizar con personas demasiado espontáneas, imprevisibles
          <div>
            <label>
            <input type="radio" v-model="stepData.input22" name="pregunta15" value="si" required>
              Si
            </label>
            <label>
              <input type="radio" v-model="stepData.input22" name="pregunta15" value="no" required>
              No
            </label>
          </div>
        </div>

        <div class="input-container ic1 input">
          16 Escucho con más frecuencia que hablo
          <div>
            <label>
            <input type="radio" v-model="stepData.input23" name="pregunta16" value="si" required>
              Si
            </label>
            <label>
              <input type="radio" v-model="stepData.input23" name="pregunta16" value="no" required>
              No
            </label>
          </div>
        </div>

        <div class="input-container ic1 input">
          17 Prefiero las cosas estructuradas a las desordenadas
          <div>
            <label>
            <input type="radio" v-model="stepData.input24" name="pregunta17" value="si" required>
              Si
            </label>
            <label>
              <input type="radio" v-model="stepData.input24" name="pregunta17" value="no" required>
              No
            </label>
          </div>
        </div>

        <div class="input-container ic1 input">
          18 Cuando poseo cualquier información, trato de interpretarla bien antes de manifestar alguna conclusión
          <div>
            <label>
            <input type="radio" v-model="stepData.input25" name="pregunta18" value="si" required>
              Si
            </label>
            <label>
              <input type="radio" v-model="stepData.input25" name="pregunta18" value="no" required>
              No
            </label>
          </div>
        </div>

        <div class="input-container ic1 input">
          19 Antes de hacer algo estudio con cuidado sus ventajas e inconvenientes
          <div>
            <label>
            <input type="radio" v-model="stepData.input26" name="pregunta19" value="si" required>
              Si
            </label>
            <label>
              <input type="radio" v-model="stepData.input26" name="pregunta19" value="no" required>
              No
            </label>
          </div>
        </div>

        <div class="input-container ic1 input">
          20 Me entusiasmo con el reto de hacer algo nuevo y diferente
          <div>
            <label>
            <input type="radio" v-model="stepData.input27" name="pregunta20" value="si" required>
              Si
            </label>
            <label>
              <input type="radio" v-model="stepData.input27" name="pregunta20" value="no" required>
              No
            </label>
          </div>
        </div>

        <div class="input-container ic1 input">
          21 Casi siempre procuro ser coherente con mis criterios y sistemas de valores. Tengo principios y los sigo
          <div>
            <label>
            <input type="radio" v-model="stepData.input28" name="pregunta21" value="si" required>
              Si
            </label>
            <label>
              <input type="radio" v-model="stepData.input28" name="pregunta21" value="no" required>
              No
            </label>
          </div>
        </div>

        <div class="input-container ic1 input">
          22 Cuando hay una discusión no me gusta ir con rodeos
          <div>
            <label>
            <input type="radio" v-model="stepData.input29" name="pregunta22" value="si" required>
              Si
            </label>
            <label>
              <input type="radio" v-model="stepData.input29" name="pregunta22" value="no" required>
              No
            </label>
          </div>
        </div>

        <div class="input-container ic1 input">
          23 Me disgusta implicarme afectivamente en el ambiente de la escuela. Prefiero mantener relaciones distantes
          <div>
            <label>
            <input type="radio" v-model="stepData.input30" name="pregunta23" value="si" required>
              Si
            </label>
            <label>
              <input type="radio" v-model="stepData.input30" name="pregunta=23" value="no" required>
              No
            </label>
          </div>
        </div>

        <div class="input-container ic1 input">
          24 Me gustan más las personas realistas y concretas que las teóricas
          <div>
            <label>
            <input type="radio" v-model="stepData.input31" name="pregunta24" value="si" required>
              Si
            </label>
            <label>
              <input type="radio" v-model="stepData.input31" name="pregunta24" value="no" required>
              No
            </label>
          </div>
        </div>

        <div class="input-container ic1 input">
          25 Me cuesta ser creativo/a, romper estructuras
          <div>
            <label>
            <input type="radio" v-model="stepData.input32" name="pregunta25" value="si" required>
              Si
            </label>
            <label>
              <input type="radio" v-model="stepData.input32" name="pregunta25" value="no" required>
              No
            </label>
          </div>
        </div>

        <div class="input-container ic1 input">
          26 Me siento a gusto con personas espontáneas y divertidas
          <div>
            <label>
            <input type="radio" v-model="stepData.input33" name="pregunta26" value="si" required>
              Si
            </label>
            <label>
              <input type="radio" v-model="stepData.input33" name="pregunta26" value="no" required>
              No
            </label>
          </div>
        </div>

        <div class="input-container ic1 input">
          27 La mayoría de las veces expreso abiertamente cómo me siento
          <div>
            <label>
            <input type="radio" v-model="stepData.input34" name="pregunta27" value="si" required>
              Si
            </label>
            <label>
              <input type="radio" v-model="stepData.input34" name="pregunta27" value="no" required>
              No
            </label>
          </div>
        </div>

    <button @click="nextStep">Siguiente</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      stepData: {
        input1: ''
      }
    };
  },
  methods: {
    nextStep() {
      this.$emit('next', this.stepData);
    }
  }
};
</script>
