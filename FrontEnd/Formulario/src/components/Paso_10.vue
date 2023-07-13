<template>
  <div class="form_">
    <h2>Paso 4</h2>
    <!-- Pregunta 81 -->
    <div class="input-container ic1 input">
      81 Disfruto clasificando cosas según sus características comunes.
      <div>
        <label>
          <input
            type="radio"
            v-model="stepData.input88"
            name="pregunta81"
            value="si"
            required
          />
          Si
        </label>
        <label>
          <input
            type="radio"
            v-model="stepData.input88"
            name="pregunta81"
            value="no"
            required
          />
          No
        </label>
      </div>
    </div>

    <!-- Pregunta 82 -->
    <div class="input-container ic1 input">
      82 Los asuntos ecológicos son importantes para mí.
      <div>
        <label>
          <input
            type="radio"
            v-model="stepData.input89"
            name="pregunta82"
            value="si"
            required
          />
          Si
        </label>
        <label>
          <input
            type="radio"
            v-model="stepData.input89"
            name="pregunta82"
            value="no"
            required
          />
          No
        </label>
      </div>
    </div>

    <!-- Pregunta 83 -->
    <div class="input-container ic1 input">
      83 El senderismo y el camping me divierten.
      <div>
        <label>
          <input
            type="radio"
            v-model="stepData.input90"
            name="pregunta83"
            value="si"
            required
          />
          Si
        </label>
        <label>
          <input
            type="radio"
            v-model="stepData.input90"
            name="pregunta83"
            value="no"
            required
          />
          No
        </label>
      </div>
    </div>

    <!-- Pregunta 84 -->
    <div class="input-container ic1 input">
      84 Me gusta cuidar las plantas.
      <div>
        <label>
          <input
            type="radio"
            v-model="stepData.input91"
            name="pregunta84"
            value="si"
            required
          />
          Si
        </label>
        <label>
          <input
            type="radio"
            v-model="stepData.input91"
            name="pregunta84"
            value="no"
            required
          />
          No
        </label>
      </div>
    </div>

    <!-- Pregunta 85 -->
    <div class="input-container ic1 input">
      85 Creo que preservar nuestros Parques naturales es importante.
      <div>
        <label>
          <input
            type="radio"
            v-model="stepData.input92"
            name="pregunta85"
            value="si"
            required
          />
          Si
        </label>
        <label>
          <input
            type="radio"
            v-model="stepData.input92"
            name="pregunta85"
            value="no"
            required
          />
          No
        </label>
      </div>
    </div>

    <!-- Pregunta 86 -->
    <div class="input-container ic1 input">
      86 Colocar las cosas dándole una jerarquía u orden tiene sentido para mí.
      <div>
        <label>
          <input
            type="radio"
            v-model="stepData.input93"
            name="pregunta86"
            value="si"
            required
          />
          Si
        </label>
        <label>
          <input
            type="radio"
            v-model="stepData.input93"
            name="pregunta86"
            value="no"
            required
          />
          No
        </label>
      </div>
    </div>

    <!-- Pregunta 87 -->
    <div class="input-container ic1 input">
      87 Los animales son importantes en mi vida.
      <div>
        <label>
          <input
            type="radio"
            v-model="stepData.input94"
            name="pregunta87"
            value="si"
            required
          />
          Si
        </label>
        <label>
          <input
            type="radio"
            v-model="stepData.input94"
            name="pregunta87"
            value="no"
            required
          />
          No
        </label>
      </div>
    </div>

    <!-- Pregunta 88 -->
    <div class="input-container ic1 input">
      88 Reciclo los envases, el vidrio, el papel etc…
      <div>
        <label>
          <input
            type="radio"
            v-model="stepData.input95"
            name="pregunta88"
            value="si"
            required
          />
          Si
        </label>
        <label>
          <input
            type="radio"
            v-model="stepData.input95"
            name="pregunta88"
            value="no"
            required
          />
          No
        </label>
      </div>
    </div>

    <!-- Pregunta 89 -->
    <div class="input-container ic1 input">
      89 Me gusta la biología, la botánica y la zoología.
      <div>
        <label>
          <input
            type="radio"
            v-model="stepData.input96"
            name="pregunta89"
            value="si"
            required
          />
          Si
        </label>
        <label>
          <input
            type="radio"
            v-model="stepData.input96"
            name="pregunta89"
            value="no"
            required
          />
          No
        </label>
      </div>
    </div>

    <!-- Pregunta 90 -->
    <div class="input-container ic1 input">
      90 Paso gran parte del tiempo al aire libre.
      <div>
        <label>
          <input
            type="radio"
            v-model="stepData.input97"
            name="pregunta90"
            value="si"
            required
          />
          Si
        </label>
        <label>
          <input
            type="radio"
            v-model="stepData.input97"
            name="pregunta90"
            value="no"
            required
          />
          No
        </label>
      </div>
    </div>

    <!-- Pregunta 91 -->
    <div class="input-container ic1 input">
      91 Aprendo fácilmente ritmos.
      <div>
        <label>
          <input
            type="radio"
            v-model="stepData.input98"
            name="pregunta91"
            value="si"
            required
          />
          Si
        </label>
        <label>
          <input
            type="radio"
            v-model="stepData.input98"
            name="pregunta91"
            value="no"
            required
          />
          No
        </label>
      </div>
    </div>

    <!-- Pregunta 92 -->
    <div class="input-container ic1 input">
      92 Me doy cuenta si la música suena mal o está desentonada.
      <div>
        <label>
          <input
            type="radio"
            v-model="stepData.input99"
            name="pregunta92"
            value="si"
            required
          />
          Si
        </label>
        <label>
          <input
            type="radio"
            v-model="stepData.input99"
            name="pregunta92"
            value="no"
            required
          />
          No
        </label>
      </div>
    </div>

    <!-- Pregunta 93 -->
    <div class="input-container ic1 input">
      93 Siempre he estado interesado en tocar un instrumento o en cantar en un
      grupo musical o coro.
      <div>
        <label>
          <input
            type="radio"
            v-model="stepData.input100"
            name="pregunta93"
            value="si"
            required
          />
          Si
        </label>
        <label>
          <input
            type="radio"
            v-model="stepData.input100"
            name="pregunta93"
            value="no"
            required
          />
          No
        </label>
      </div>
    </div>

    <!-- Pregunta 94 -->
    <div class="input-container ic1 input">
      94 Me resulta fácil moverme según un ritmo concreto.
      <div>
        <label>
          <input
            type="radio"
            v-model="stepData.input101"
            name="pregunta94"
            value="si"
            required
          />
          Si
        </label>
        <label>
          <input
            type="radio"
            v-model="stepData.input101"
            name="pregunta94"
            value="no"
            required
          />
          No
        </label>
      </div>
    </div>

    <!-- Pregunta 95 -->
    <div class="input-container ic1 input">
      95 Soy consciente de los ruidos ambientales (Ej. La lluvia en los
      cristales, el tráfico en las calles, etc…)
      <div>
        <label>
          <input
            type="radio"
            v-model="stepData.input102"
            name="pregunta95"
            value="si"
            required
          />
          Si
        </label>
        <label>
          <input
            type="radio"
            v-model="stepData.input102"
            name="pregunta95"
            value="no"
            required
          />
          No
        </label>
      </div>
    </div>

    <!-- Pregunta 96 -->
    <div class="input-container ic1 input">
      96 Recuerdo las cosas poniéndoles un ritmo.
      <div>
        <label>
          <input
            type="radio"
            v-model="stepData.input103"
            name="pregunta96"
            value="si"
            required
          />
          Si
        </label>
        <label>
          <input
            type="radio"
            v-model="stepData.input103"
            name="pregunta96"
            value="no"
            required
          />
          No
        </label>
      </div>
    </div>

    <!-- Pregunta 97 -->
    <div class="input-container ic1 input">
      97 Me resulta difícil concentrarme mientras escucho la radio o la
      televisión.
      <div>
        <label>
          <input
            type="radio"
            v-model="stepData.input104"
            name="pregunta97"
            value="si"
            required
          />
          Si
        </label>
        <label>
          <input
            type="radio"
            v-model="stepData.input104"
            name="pregunta97"
            value="no"
            required
          />
          No
        </label>
      </div>
    </div>

    <!-- Pregunta 98 -->
    <div class="input-container ic1 input">
      98 Me gustan varios tipos de música.
      <div>
        <label>
          <input
            type="radio"
            v-model="stepData.input105"
            name="pregunta98"
            value="si"
            required
          />
          Si
        </label>
        <label>
          <input
            type="radio"
            v-model="stepData.input105"
            name="pregunta98"
            value="no"
            required
          />
          No
        </label>
      </div>
    </div>

    <!-- Pregunta 99 -->
    <div class="input-container ic1 input">
      99 Suelo canturrear o tamborilear sobre la mesa sin darme cuenta.
      <div>
        <label>
          <input
            type="radio"
            v-model="stepData.input106"
            name="pregunta99"
            value="si"
            required
          />
          Si
        </label>
        <label>
          <input
            type="radio"
            v-model="stepData.input106"
            name="pregunta99"
            value="no"
            required
          />
          No
        </label>
      </div>
    </div>

    <!-- Pregunta 100 -->
    <div class="input-container ic1 input">
      100 Me resulta fácil recordar canciones líricas.
      <div>
        <label>
          <input
            type="radio"
            v-model="stepData.input107"
            name="pregunta100"
            value="si"
            required
          />
          Si
        </label>
        <label>
          <input
            type="radio"
            v-model="stepData.input107"
            name="pregunta100"
            value="no"
            required
          />
          No
        </label>
      </div>
    </div>

    <!-- Pregunta 101 -->
    <div class="input-container ic1 input">
      101 Guardo mis cosas limpias y ordenadas.
      <div>
        <label>
          <input
            type="radio"
            v-model="stepData.input108"
            name="pregunta101"
            value="si"
            required
          />
          Si
        </label>
        <label>
          <input
            type="radio"
            v-model="stepData.input108"
            name="pregunta101"
            value="no"
            required
          />
          No
        </label>
      </div>
    </div>

    <!-- Pregunta 102 -->
    <div class="input-container ic1 input">
      102 Las instrucciones paso a paso son una gran ayuda.
      <div>
        <label>
          <input
            type="radio"
            v-model="stepData.input109"
            name="pregunta102"
            value="si"
            required
          />
          Si
        </label>
        <label>
          <input
            type="radio"
            v-model="stepData.input109"
            name="pregunta102"
            value="no"
            required
          />
          No
        </label>
      </div>
    </div>

    <!-- Pregunta 103 -->
    <div class="input-container ic1 input">
      103 Resolver problemas es fácil para mí.
      <div>
        <label>
          <input
            type="radio"
            v-model="stepData.input110"
            name="pregunta103"
            value="si"
            required
          />
          Si
        </label>
        <label>
          <input
            type="radio"
            v-model="stepData.input110"
            name="pregunta103"
            value="no"
            required
          />
          No
        </label>
      </div>
    </div>

    <!-- Pregunta 104 -->
    <div class="input-container ic1 input">
      104 Me siento mal con la gente que es desorganizada.
      <div>
        <label>
          <input
            type="radio"
            v-model="stepData.input111"
            name="pregunta104"
            value="si"
            required
          />
          Si
        </label>
        <label>
          <input
            type="radio"
            v-model="stepData.input111"
            name="pregunta104"
            value="no"
            required
          />
          No
        </label>
      </div>
    </div>

    <!-- Pregunta 105 -->
    <div class="input-container ic1 input">
      105 Puedo realizar cálculos mentales rápidamente.
      <div>
        <label>
          <input
            type="radio"
            v-model="stepData.input112"
            name="pregunta105"
            value="si"
            required
          />
          Si
        </label>
        <label>
          <input
            type="radio"
            v-model="stepData.input112"
            name="pregunta105"
            value="no"
            required
          />
          No
        </label>
      </div>
    </div>

    <!-- Pregunta 106 -->
    <div class="input-container ic1 input">
      106 Los puzzles que requieren razonamiento son divertidos.
      <div>
        <label>
          <input
            type="radio"
            v-model="stepData.input113"
            name="pregunta106"
            value="si"
            required
          />
          Si
        </label>
        <label>
          <input
            type="radio"
            v-model="stepData.input113"
            name="pregunta106"
            value="no"
            required
          />
          No
        </label>
      </div>
    </div>

    <!-- Pregunta 107 -->
    <div class="input-container ic1 input">
      107 No puedo comenzar un trabajo hasta que todas mis dudas se han
      resuelto.
      <div>
        <label>
          <input
            type="radio"
            v-model="stepData.input114"
            name="pregunta107"
            value="si"
            required
          />
          Si
        </label>
        <label>
          <input
            type="radio"
            v-model="stepData.input114"
            name="pregunta107"
            value="no"
            required
          />
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