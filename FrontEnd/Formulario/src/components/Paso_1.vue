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
          <input class="input" placeholder=" " type="text" v-model="stepData.name" required>
          <div class="cut"></div>
          <label for="firstname" class="placeholder">Nombre</label>
        </div>
        <div class="input-container ic1">
          <input class="input" placeholder=" " type="text" v-model="stepData.surname" required>
          <div class="cut"></div>
          <label for="surname" class="placeholder">Apellido</label>
        </div>
        <div class="input-container ic1" >
          <input class="input" placeholder=" " type="email" v-model="stepData.gmail" required>
          <div class="cut"></div>
          <label for="gmail" class="placeholder">Correo Electrónico</label>
        </div>
        <div class="input-container ic1">
          <input class="input" placeholder=" " type="date" v-model="stepData.date" required>
          <div class="cut"></div>
          <label for="date" class="placeholder">Fecha de Nacimiento</label>
        </div>
        <div class="input-container ic1 input imput_select">
          <select v-model="stepData.gender" required>
            <option value="" disabled selected>Seleccione una opción</option>
            <option value="Femenino">Femenino</option>
            <option value="Masculino">Masculino</option>
            <option value="Otro">Otro</option>
          </select>
          <label for="gender" class="placeholder">Selecciona tu Género</label>
        </div>
        <div class="input-container ic1 input imput_select">
          <select v-model="stepData.group" required>
            <option value="" disabled selected>Seleccione una opción</option>
            <option value="Estudiante">Estudiante</option>
            <option value="Docente">Docente</option>
            <option value="Club Deportivo de la Universidad">Club Deportivo de la Universidad</option>
            <option value="Publico General">Publico General</option>
          </select>
          <label for="group" class="placeholder">Selecciona tu Grupo</label>
        </div>
        <div class="input-container ic1">
          <input class="input" placeholder=" " type="text" v-model="stepData.specialty" required>
          <div class="cut"></div>
          <label for="specialty" class="placeholder">Escribe tu especialidad</label>
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
            <input type="radio" v-model="stepData.Honey_1" name="pregunta1" value=1 required>
              Si
            </label>
            <label>
              <input type="radio" v-model="stepData.Honey_1" name="pregunta1" value=0 required>
              No
            </label>
          </div>
        </div>

        <div class="input-container ic1 input">
          2 Estoy seguro/a de lo que es bueno y lo que es malo, lo que está bien y lo que está mal.
          <div>
            <label>
            <input type="radio" v-model="stepData.Honey_2" name="pregunta2" value=1 required>
              Si
            </label>
            <label>
              <input type="radio" v-model="stepData.Honey_2" name="pregunta2" value=0 required>
              No
            </label>
          </div>
        </div>

        <div class="input-container ic1 input">
          3 Muchas veces actúo sin mirar las consecuencias
          <div>
            <label>
            <input type="radio" v-model="stepData.Honey_3" name="pregunta3" value=1 required>
              Si
            </label>
            <label>
              <input type="radio" v-model="stepData.Honey_3" name="pregunta3" value=0 required>
              No
            </label>
          </div>
        </div>

        <div class="input-container ic1 input">
          4 Normalmente trato de resolver los problemas metódicamente y paso a paso
          <div>
            <label>
            <input type="radio" v-model="stepData.Honey_4" name="pregunta4" value=1 required>
              Si
            </label>
            <label>
              <input type="radio" v-model="stepData.Honey_4" name="pregunta4" value=0 required>
              No
            </label>
          </div>
        </div>

        <div class="input-container ic1 input">
          5 Creo que los formalismos coartan y limitan la actuación libre de las personas
          <div>
            <label>
            <input type="radio" v-model="stepData.Honey_5" name="pregunta5" value=1 required>
              Si
            </label>
            <label>
              <input type="radio" v-model="stepData.Honey_5" name="pregunta5" value=0 required>
              No
            </label>
          </div>
        </div>

        <div class="input-container ic1 input">
          6 Me interesa saber cuáles son los sistemas de valores de los demás y con qué criterios actúan
          <div>
            <label>
            <input type="radio" v-model="stepData.Honey_6" name="pregunta6" value=1 required>
              Si
            </label>
            <label>
              <input type="radio" v-model="stepData.Honey_6" name="pregunta6" value=0 required>
              No
            </label>
          </div>
        </div>

        <div class="input-container ic1 input">
          7 Pienso que el actuar intuitivamente puede ser siempre tan válido como actuar reflexivamente.
          <div>
            <label>
            <input type="radio" v-model="stepData.Honey_7" name="pregunta7" value=1 required>
              Si
            </label>
            <label>
              <input type="radio" v-model="stepData.Honey_7" name="pregunta7" value=0 required>
              No
            </label>
          </div>
        </div>

        <div class="input-container ic1 input">
          8 Creo que lo más importante es que las cosas funcionen
          <div>
            <label>
            <input type="radio" v-model="stepData.Honey_8" name="pregunta8" value=1 required>
              Si
            </label>
            <label>
              <input type="radio" v-model="stepData.Honey_8" name="pregunta8" value=0 required>
              No
            </label>
          </div>
        </div>

        <div class="input-container ic1 input">
          9 Procuro estar al tanto de lo que ocurre aquí y ahora
          <div>
            <label>
            <input type="radio" v-model="stepData.Honey_9" name="pregunta9" value=1 required>
              Si
            </label>
            <label>
              <input type="radio" v-model="stepData.Honey_9" name="pregunta9" value=0 required>
              No
            </label>
          </div>
        </div>

        <div class="input-container ic1 input">
          10 Disfruto cuando tengo tiempo para preparar mi trabajo y realizarlo a conciencia
          <div>
            <label>
            <input type="radio" v-model="stepData.Honey_10" name="pregunta10" value=1 required>
              Si
            </label>
            <label>
              <input type="radio" v-model="stepData.Honey_10" name="pregunta10" value=0 required>
              No
            </label>
          </div>
        </div>

        <div class="input-container ic1 input">
          11 Estoy a gusto siguiendo un orden en las comidas, en el estudio, haciendo ejercicio regularmente
          <div>
            <label>
            <input type="radio" v-model="stepData.Honey_11" name="pregunta11" value=1 required>
              Si
            </label>
            <label>
              <input type="radio" v-model="stepData.Honey_11" name="pregunta11" value=0 required>
              No
            </label>
          </div>
        </div>

        <div class="input-container ic1 input">
          12 Cuando escucho una nueva idea enseguida comienzo a pensar cómo ponerla en práctica
          <div>
            <label>
            <input type="radio" v-model="stepData.Honey_12" name="pregunta12" value=1required>
              Si
            </label>
            <label>
              <input type="radio" v-model="stepData.Honey_12" name="pregunta12" value=0 required>
              No
            </label>
          </div>
        </div>

        <div class="input-container ic1 input">
          13 Prefiero las ideas originales y novedosas aunque no sean prácticas
          <div>
            <label>
            <input type="radio" v-model="stepData.Honey_13" name="pregunta13" value=1 required>
              Si
            </label>
            <label>
              <input type="radio" v-model="stepData.Honey_13" name="pregunta13" value=0 required>
              No
            </label>
          </div>
        </div>

        <div class="input-container ic1 input">
          14 Admito y me ajusto a las normas sólo si me sirven para lograr mis objetivos
          <div>
            <label>
            <input type="radio" v-model="stepData.Honey_14" name="pregunta14" value=1 required>
              Si
            </label>
            <label>
              <input type="radio" v-model="stepData.Honey_14" name="pregunta14" value=0 required>
              No
            </label>
          </div>
        </div>

        <div class="input-container ic1 input">
          15 Normalmente encajo bien con personas reflexivas, y me cuesta sintonizar con personas demasiado espontáneas, imprevisibles
          <div>
            <label>
            <input type="radio" v-model="stepData.Honey_15" name="pregunta15" value=1 required>
              Si
            </label>
            <label>
              <input type="radio" v-model="stepData.Honey_15" name="pregunta15" value=0 required>
              No
            </label>
          </div>
        </div>

        <div class="input-container ic1 input">
          16 Escucho con más frecuencia que hablo
          <div>
            <label>
            <input type="radio" v-model="stepData.Honey_16" name="pregunta16" value=1 required>
              Si
            </label>
            <label>
              <input type="radio" v-model="stepData.Honey_16" name="pregunta16" value=0 required>
              No
            </label>
          </div>
        </div>

        <div class="input-container ic1 input">
          17 Prefiero las cosas estructuradas a las desordenadas
          <div>
            <label>
            <input type="radio" v-model="stepData.Honey_17" name="pregunta17" value=1 required>
              Si
            </label>
            <label>
              <input type="radio" v-model="stepData.Honey_17" name="pregunta17" value=0 required>
              No
            </label>
          </div>
        </div>

        <div class="input-container ic1 input">
          18 Cuando poseo cualquier información, trato de interpretarla bien antes de manifestar alguna conclusión
          <div>
            <label>
            <input type="radio" v-model="stepData.Honey_18" name="pregunta18" value=1 required>
              Si
            </label>
            <label>
              <input type="radio" v-model="stepData.Honey_18" name="pregunta18" value=0 required>
              No
            </label>
          </div>
        </div>

        <div class="input-container ic1 input">
          19 Antes de hacer algo estudio con cuidado sus ventajas e inconvenientes
          <div>
            <label>
            <input type="radio" v-model="stepData.Honey_19" name="pregunta19" value=1 required>
              Si
            </label>
            <label>
              <input type="radio" v-model="stepData.Honey_19" name="pregunta19" value=0 required>
              No
            </label>
          </div>
        </div>

        <div class="input-container ic1 input">
          20 Me entusiasmo con el reto de hacer algo nuevo y diferente
          <div>
            <label>
            <input type="radio" v-model="stepData.Honey_20" name="pregunta20" value=1 required>
              Si
            </label>
            <label>
              <input type="radio" v-model="stepData.Honey_20" name="pregunta20" value=0 required>
              No
            </label>
          </div>
        </div>

        <div class="input-container ic1 input">
          21 Casi siempre procuro ser coherente con mis criterios y sistemas de valores. Tengo principios y los sigo
          <div>
            <label>
              <input type="radio" v-model="stepData.Honey_21" name="pregunta21" value=1 required>
              Si
            </label>
            <label>
              <input type="radio" v-model="stepData.Honey_21" name="pregunta21" value=0 required>
              No
            </label>
          </div>
        </div>

        <div class="input-container ic1 input">
          22 Cuando hay una discusión no me gusta ir con rodeos
          <div>
            <label>
              <input type="radio" v-model="stepData.Honey_22" name="pregunta22" value=1 required>
              Si
            </label>
            <label>
              <input type="radio" v-model="stepData.Honey_22" name="pregunta22" value=0 required>
              No
            </label>
          </div>
        </div>

        <div class="input-container ic1 input">
          23 Me disgusta implicarme afectivamente en el ambiente de la escuela. Prefiero mantener relaciones distantes
          <div>
            <label>
              <input type="radio" v-model="stepData.Honey_23" name="pregunta23" value=1 required>
              Si
            </label>
            <label>
              <input type="radio" v-model="stepData.Honey_23" name="pregunta=23" value=0 required>
              No
            </label>
          </div>
        </div>

        <div class="input-container ic1 input">
          24 Me gustan más las personas realistas y concretas que las teóricas
          <div>
            <label>
            <input type="radio" v-model="stepData.Honey_24" name="pregunta24" value=1 required>
              Si
            </label>
            <label>
              <input type="radio" v-model="stepData.Honey_24" name="pregunta24" value=0 required>
              No
            </label>
          </div>
        </div>

        <div class="input-container ic1 input">
          25 Me cuesta ser creativo/a, romper estructuras
          <div>
            <label>
              <input type="radio" v-model="stepData.Honey_25" name="pregunta25" value=1 required>
              Si
            </label>
            <label>
              <input type="radio" v-model="stepData.Honey_25" name="pregunta25" value=0 required>
              No
            </label>
          </div>
        </div>

        <div class="input-container ic1 input">
          26 Me siento a gusto con personas espontáneas y divertidas
          <div>
            <label>
              <input type="radio" v-model="stepData.Honey_26" name="pregunta26" value=1 required>
              Si
            </label>
            <label>
              <input type="radio" v-model="stepData.Honey_26" name="pregunta26" value=0 required>
              No
            </label>
          </div>
        </div>

        <div class="input-container ic1 input">
          27 La mayoría de las veces expreso abiertamente cómo me siento
          <div>
            <label>
            <input type="radio" v-model="stepData.Honey_27" name="pregunta27" value=1 required>
              Si
            </label>
            <label>
              <input type="radio" v-model="stepData.Honey_27" name="pregunta27" value=0 required>
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
        name: '',
        surname: '',
        gmail: '',
        date: '',
        gender: '',
        group: '',
        specialty: '',
        Honey_27: '',
        Honey_26: '',
        Honey_25: '',
        Honey_24: '',
        Honey_23: '',
        Honey_22: '',
        Honey_21: '',
        Honey_20: '',
        Honey_19: '',
        Honey_18: '',
        Honey_17: '',
        Honey_16: '',
        Honey_15: '',
        Honey_14: '',
        Honey_13: '',
        Honey_12: '',
        Honey_11: '',
        Honey_10: '',
        Honey_9: '',
        Honey_8: '',
        Honey_7: '',
        Honey_6: '',
        Honey_5: '',
        Honey_4: '',
        Honey_3: '',
        Honey_2: '',
        Honey_1: ''
      }
    };
  },
  methods: {
    nextStep() {
      let pass = true;
      for (var i in this.stepData) {
        if (this.stepData[i] == '') {
          pass = false;
        }
      }

      if (pass) this.$emit('next', this.stepData);
    }
  }
};
</script>
