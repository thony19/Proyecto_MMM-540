<script >
export default {
  data() {
    return {
      currentStep: 0,
      steps: [
        { title: 'Paso 1', input_01: '', input_02: '', input_03: '', input_04: ''  },
        { title: 'Paso 2', input_11: '', input_12: '', input_13: '', input_14: ''  },
        { title: 'Paso 3', input_21: '', input_22: '', input_23: '', input_24: ''  },
        { title: 'Paso 4', input_01: '', input_02: '', input_03: '', input_04: ''  },
        { title: 'Paso 5', input_11: '', input_12: '', input_13: '', input_14: ''  },
        { title: 'Paso 6', input_21: '', input_22: '', input_23: '', input_24: ''  },
        { title: 'Paso 7', input_01: '', input_02: '', input_03: '', input_04: ''  },
        { title: 'Paso 8', input_11: '', input_12: '', input_13: '', input_14: ''  },
        { title: 'Paso 9', input_21: '', input_22: '', input_23: '', input_24: ''  }
      ],
      labels: [
        "Selecciona tu género",
        "Selecciona tu grupo"
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
    },
    async submitForm() {
    try {
      const response = await fetch('http://localhost:5173/submit', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.formData) // Suponiendo que tienes un objeto formData con los datos del formulario
      });

      if (response.ok) {
        // Solicitud exitosa
        const responseData = await response.json();
        console.log(responseData); // Hacer algo con los datos de respuesta del backend
      } else {
        // Error en la solicitud
        console.error('Error en la solicitud al backend');
      }
    } catch (error) {
      console.error('Error en la comunicación con el backend', error);
    }
  }
  }
};
</script>

<template>
  <div id="app">

    <div class="progress-bar">
      <div class="progress" :style="{ width: progressPercentage + '%' }"></div>
    </div>

    <form class="form">
      <h2 class="title">Estilos de Aprendizaje e Inteligencias múltiples</h2>
      <p class="subtitle">Estimado/a alumno/a:
          <br>
          De antemano agradecemos tu valiosa colaboración al responder este cuestionario que forma parte de una reflexión más amplia que pretende contribuir a mejorar la calidad de la educación científica en nuestro país. 
          <br>
          Toda la información que nos aportes será de uso estrictamente confidencial.
      </p>
      <fieldset v-for="(step, index) in steps" :key="index" v-show="currentStep === index">
        <h2>{{ step.title }}</h2>
        <div class="input-container ic1" >
          <input class="input" placeholder=" " type="text" v-model="step.input_01" required>
          <div class="cut"></div>
          <label for="firstname" class="placeholder">Primer Nombre</label>
        </div>
        <div class="input-container ic1">
          <input class="input" placeholder=" " type="text" v-model="step.input_02" required>
          <div class="cut"></div>
          <label for="lastname" class="placeholder">Segundo Nombre</label>
        </div>
        <div class="input-container ic1" >
          <input class="input" placeholder=" " type="email" v-model="step.input_03" required>
          <div class="cut"></div>
          <label for="firstname" class="placeholder">Correo Electrónico</label>
        </div>
        <div class="input-container ic1">
          <input class="input" placeholder=" " type="date" v-model="step.input_04" required>
          <div class="cut"></div>
          <label for="lastname" class="placeholder">Fecha de Nacimiento</label>
        </div>
        <div class="input-container ic1">
          <select v-model="step.selectValue_1" required>
            <option value="" disabled selected>Seleccione una opción</option>
            <option value="opcion1">Femenino</option>
            <option value="opcion2">Masculino</option>
            <option value="opcion3">Otro:</option>
          </select>
          <label for="lastname" class="placeholder">Selecciona tu Género</label>
        </div>
        <div class="input-container ic1">
          <select v-model="step.selectValue_2" required>
            <option value="" disabled selected>Seleccione una opción</option>
            <option value="opcion1">Estudiante</option>
            <option value="opcion2">Docente</option>
            <option value="opcion3">Club Deportivo de la Universidad</option>
            <option value="opcion3">Publico General</option>
          </select>
          <label for="lastname" class="placeholder">Selecciona tu Grupo</label>
        </div>
        <div class="input-container ic1">
          <!-- <p>Escribe tu especialidad<br>
              Ejemplos:<br>
              -Estudiante de Instituto Nacional Mejía.<br>
              -Docente de Matemática del Instituto Nacional Mejía.<br>
              -Preparador de arqueros.<br>
              -Estudiante de la Universidad Católica.<br>
          </p> -->
          <input class="input" placeholder=" " type="text" v-model="step.input_05" required>
          <div class="cut"></div>
          <label for="lastname" class="placeholder">Escribe tu especialidad</label>
        </div>
        <div class="input-container ic1 input">
          Agradecimiento<br>
          Reiteramos nuestros agradecimientos a tu valiosa colaboración personal al responder este test que forma
          parte de un proyecto de investigación educativa con el fin de fortalecer la educación científica de nuestro país.<br>
        </div>
        <div class="input-container ic1 input">
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
        <div class="input-container ic1">
          <!-- <input class="input" placeholder=" "  type="radio" v-model="step.input_06" required>
          1 Tengo fama de decir lo que pienso claramente y sin rodeos	
          <input class="input" placeholder=" "  type="radio" v-model="step.input_07" required> -->
          1 Tengo fama de decir lo que pienso claramente y sin rodeos
          <div>
            <label for="si_1">Si</label>
            <input type="radio" id="si_1" v-model="step.radioValue_1" value="si" required>
          </div>
          <div>
            <label for="option2">No</label>
            <input type="radio" id="option2" v-model="step.radioValue_2" value="no" required>
          </div>
          2 Estoy seguro/a de lo que es bueno y lo que es malo, lo que está bien y lo que está mal.	
          <div>
            <label for="si_2">Si</label>
            <input type="radio" id="si_2" v-model="step.radioValue_3" value="si" required>
          </div>
          <div>
            <label for="option2">No</label>
            <input type="radio" id="option4" v-model="step.radioValue_4" value="no" required>
          </div>
          3 Muchas veces actúo sin mirar las consecuencias	
          <div>
            <label for="si_3">Si</label>
            <input type="radio" id="si_3" v-model="step.radioValue_5" value="si" required>
          </div>
          <div>
            <label for="option2">No</label>
            <input type="radio" id="option2" v-model="step.radioValue_6" value="no" required>
          </div>
          4 Normalmente trato de resolver los problemas metódicamente y paso a paso	
          <div>
            <label for="option1">Si</label>
            <input type="radio" id="option1" v-model="step.radioValue_7" value="si" required>
          </div>
          <div>
            <label for="option2">No</label>
            <input type="radio" id="option2" v-model="step.radioValue_8" value="no" required>
          </div>
          5 Creo que los formalismos coartan y limitan la actuación libre de las personas
          <div>
            <label for="option1">Si</label>
            <input type="radio" id="option1" v-model="step.radioValue_9" value="si" required>
          </div>
          <div>
            <label for="option2">No</label>
            <input type="radio" id="option2" v-model="step.radioValue_10" value="no" required>
          </div>
          6 Me interesa saber cuáles son los sistemas de valores de los demás y con qué criterios actúan	
          <div>
            <label for="option1">Si</label>
            <input type="radio" id="option1" v-model="step.radioValue_11" value="si" required>
          </div>
          <div>
            <label for="option2">No</label>
            <input type="radio" id="option2" v-model="step.radioValue_12" value="no" required>
          </div>
          7 Pienso que el actuar intuitivamente puede ser siempre tan válido como actuar reflexivamente.	
          <div>
            <label for="option1">Si</label>
            <input type="radio" id="option1" v-model="step.radioValue_12" value="si" required>
          </div>
          <div>
            <label for="option2">No</label>
            <input type="radio" id="option2" v-model="step.radioValue_13" value="no" required>
          </div>
          8 Creo que lo más importante es que las cosas funcionen	
          <div>
            <label for="option1">Si</label>
            <input type="radio" id="option1" v-model="step.radioValue_14" value="si" required>
          </div>
          <div>
            <label for="option2">No</label>
            <input type="radio" id="option2" v-model="step.radioValue_15" value="no" required>
          </div>
          9 Procuro estar al tanto de lo que ocurre aquí y ahora	
          <div>
            <label for="option1">Si</label>
            <input type="radio" id="option1" v-model="step.radioValue_16" value="si" required>
          </div>
          <div>
            <label for="option2">No</label>
            <input type="radio" id="option2" v-model="step.radioValue_17" value="no" required>
          </div>
          10 Disfruto cuando tengo tiempo para preparar mi trabajo y realizarlo a conciencia	
          <div>
            <label for="option1">Si</label>
            <input type="radio" id="option1" v-model="step.radioValue_18" value="si" required>
          </div>
          <div>
            <label for="option2">No</label>
            <input type="radio" id="option2" v-model="step.radioValue_19" value="no" required>
          </div>
          11 Estoy a gusto siguiendo un orden en las comidas, en el estudio, haciendo ejercicio regularmente	
          <div>
            <label for="option1">Si</label>
            <input type="radio" id="option1" v-model="step.radioValue_20" value="si" required>
          </div>
          <div>
            <label for="option2">No</label>
            <input type="radio" id="option2" v-model="step.radioValue_21" value="no" required>
          </div>
          12 Cuando escucho una nueva idea enseguida comienzo a pensar cómo ponerla en práctica	
          <div>
            <label for="option1">Si</label>
            <input type="radio" id="option1" v-model="step.radioValue_22" value="si" required>
          </div>
          <div>
            <label for="option2">No</label>
            <input type="radio" id="option2" v-model="step.radioValue_23" value="no" required>
          </div>
          13 Prefiero las ideas originales y novedosas aunque no sean prácticas	
          <div>
            <label for="option1">Si</label>
            <input type="radio" id="option1" v-model="step.radioValue_24" value="si" required>
          </div>
          <div>
            <label for="option2">No</label>
            <input type="radio" id="option2" v-model="step.radioValue_25" value="no" required>
          </div>
          14 Admito y me ajusto a las normas sólo si me sirven para lograr mis objetivos	
          <div>
            <label for="option1">Si</label>
            <input type="radio" id="option1" v-model="step.radioValue_26" value="si" required>
          </div>
          <div>
            <label for="option2">No</label>
            <input type="radio" id="option2" v-model="step.radioValue_27" value="no" required>
          </div>
          15 Normalmente encajo bien con personas reflexivas, y me cuesta sintonizar con personas demasiado espontáneas, imprevisibles	
          <div>
            <label for="option1">Si</label>
            <input type="radio" id="option1" v-model="step.radioValue_28" value="si" required>
          </div>
          <div>
            <label for="option2">No</label>
            <input type="radio" id="option2" v-model="step.radioValue_29" value="no" required>
          </div>
          16 Escucho con más frecuencia que hablo	
          <div>
            <label for="option1">Si</label>
            <input type="radio" id="option1" v-model="step.radioValue_30" value="si" required>
          </div>
          <div>
            <label for="option2">No</label>
            <input type="radio" id="option2" v-model="step.radioValue_31" value="no" required>
          </div>
          17 Prefiero las cosas estructuradas a las desordenadas	
          <div>
            <label for="option1">Si</label>
            <input type="radio" id="option1" v-model="step.radioValue_32" value="si" required>
          </div>
          <div>
            <label for="option2">No</label>
            <input type="radio" id="option2" v-model="step.radioValue_33" value="no" required>
          </div>
          18 Cuando poseo cualquier información, trato de interpretarla bien antes de manifestar alguna conclusión	
          <div>
            <label for="option1">Si</label>
            <input type="radio" id="option1" v-model="step.radioValue_34" value="si" required>
          </div>
          <div>
            <label for="option2">No</label>
            <input type="radio" id="option2" v-model="step.radioValue_35" value="no" required>
          </div>
          19 Antes de hacer algo estudio con cuidado sus ventajas e inconvenientes	
          <div>
            <label for="option1">Si</label>
            <input type="radio" id="option1" v-model="step.radioValue_36" value="si" required>
          </div>
          <div>
            <label for="option2">No</label>
            <input type="radio" id="option2" v-model="step.radioValue_37" value="no" required>
          </div>
          20 Me entusiasmo con el reto de hacer algo nuevo y diferente	
          <div>
            <label for="option1">Si</label>
            <input type="radio" id="option1" v-model="step.radioValue_38" value="si" required>
          </div>
          <div>
            <label for="option2">No</label>
            <input type="radio" id="option2" v-model="step.radioValue_39" value="no" required>
          </div>
          21 Casi siempre procuro ser coherente con mis criterios y sistemas de valores. Tengo principios y los sigo	
          <div>
            <label for="option1">Si</label>
            <input type="radio" id="option1" v-model="step.radioValue_40" value="si" required>
          </div>
          <div>
            <label for="option2">No</label>
            <input type="radio" id="option2" v-model="step.radioValue_41" value="no" required>
          </div>
          22 Cuando hay una discusión no me gusta ir con rodeos	
          <div>
            <label for="option1">Si</label>
            <input type="radio" id="option1" v-model="step.radioValue_42" value="si" required>
          </div>
          <div>
            <label for="option2">No</label>
            <input type="radio" id="option2" v-model="step.radioValue_43" value="no" required>
          </div>
          23 Me disgusta implicarme afectivamente en el ambiente de la escuela. Prefiero mantener relaciones distantes	
          <div>
            <label for="option1">Si</label>
            <input type="radio" id="option1" v-model="step.radioValue_44" value="si" required>
          </div>
          <div>
            <label for="option2">No</label>
            <input type="radio" id="option2" v-model="step.radioValue_45" value="no" required>
          </div>
          24 Me gustan más las personas realistas y concretas que las teóricas	
          <div>
            <label for="option1">Si</label>
            <input type="radio" id="option1" v-model="step.radioValue_46" value="si" required>
          </div>
          <div>
            <label for="option2">No</label>
            <input type="radio" id="option2" v-model="step.radioValue_47" value="no" required>
          </div>
          25 Me cuesta ser creativo/a, romper estructuras	
          <div>
            <label for="option1">Si</label>
            <input type="radio" id="option1" v-model="step.radioValue_48" value="si" required>
          </div>
          <div>
            <label for="option2">No</label>
            <input type="radio" id="option2" v-model="step.radioValue_49" value="no" required>
          </div>
          26 Me siento a gusto con personas espontáneas y divertidas	
          <div>
            <label for="option1">Si</label>
            <input type="radio" id="option1" v-model="step.radioValue_50" value="si" required>
          </div>
          <div>
            <label for="option2">No</label>
            <input type="radio" id="option2" v-model="step.radioValue_51" value="no" required>
          </div>
          27 La mayoría de las veces expreso abiertamente cómo me siento
          <div class="cut"></div>
          <div>
            <label for="option1">Si</label>
            <input type="radio" id="option1" v-model="step.radioValue_52" value="si" required>
          </div>
          <div>
            <label for="option2">No</label>
            <input type="radio" id="option2" v-model="step.radioValue_53" value="no" required>
          </div>
        </div>



        <button v-if="currentStep > 0" @click.prevent="previousStep">Anterior</button>
        <button v-if="currentStep < steps.length - 1" @click.prevent="nextStep">Siguiente</button>
        <button v-else type="submit">Enviar</button>
      </fieldset>
    </form>
  </div>
</template>

<style scoped>
/* Configuraciones */
body {
  align-items: center;
  background-color: #000;
  display: flex;
  justify-content: center;
  min-height: 100vh;
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
  color: #eee;
  font-family: sans-serif;
  font-size: 36px;
  font-weight: 600;
  margin-top: 30px;
}
.subtitle {
  color: #eee;
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
  padding: 4px 20px 0;
  width: 100%;
}

.cut {
  background-color: #15172b;
  border-radius: 10px;
  height: 20px;
  left: 20px;
  position: absolute;
  top: -20px;
  transform: translateY(0);
  transition: transform 200ms;
  width: 20%;
}

.input:focus ~ .cut,
.input:not(:placeholder-shown) ~ .cut {
  transform: translateY(8px);
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
  color: #dc2f55;
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
