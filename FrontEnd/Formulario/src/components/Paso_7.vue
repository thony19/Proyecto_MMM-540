<template>
  <div class="form_">
    <h2>Paso 7</h2>
    <h3>Indicadores socioeconómicos</h3>
    <!-- Pregunta 1 -->
    <div class="input-container ic1 input">
      1 Selecciona tu grupo étnico
      <div style="text-align: justify;">
        <label>
          <input type="radio" v-model="stepData.socioEcon1" name="socioEcon1" value="Mestizo" required>
          Mestizo
        </label>
        <br>
        <label>
          <input type="radio" v-model="stepData.socioEcon1" name="socioEcon1" value="Indígena" required>
          Indígena
        </label>
        <br>
        <label>
          <input type="radio" v-model="stepData.socioEcon1" name="socioEcon1" value="Afroecuatoriano" required>
          Afroecuatoriano
        </label>
        <br>
        <label>
          <input type="radio" v-model="stepData.socioEcon1" name="socioEcon1" value="Montubio" required>
          Montubio
        </label>
        <br>
        <label>
          <input type="radio" v-model="stepData.socioEcon1" name="socioEcon1" value="Otro" required>
          Otro
        </label>
      </div>
    </div>

    <!-- Pregunta 2 -->
    <div class="input-container ic1 input imput_select">
      2 Selecciona la parroquia donde vives
      <select v-model="stepData.input6" required>
        <option value="" disabled selected>Seleccione una opción</option>
        <option value="Estudiante">Analgasí</option>
        <option value="Docente">Amaguaña</option>
        <option value="Club Deportivo de la Universidad">Atahualpa</option>
        <option value="Publico General">Belisario Quevedo</option>
        <option value="Estudiante">Calacalí</option>
        <option value="Docente">Calderón</option>
        <option value="Club Deportivo de la Universidad">Carcelén</option>
        <option value="Publico General">Centro Histórico</option>
        <option value="Estudiante">Chavezpamba</option>
        <option value="Docente">Checa</option>
        <option value="Club Deportivo de la Universidad">Chilbulo</option>
        <option value="Publico General">Chillogallo</option>
        <option value="Estudiante">Chimbacalle</option>
        <option value="Docente">Cochapamba</option>
        <option value="Club Deportivo de la Universidad">Comité del Pueblo</option>
        <option value="Publico General">Concepción</option>
        <option value="Estudiante">Conocoto</option>
        <option value="Docente">Cotocollao</option>
        <option value="Club Deportivo de la Universidad">Cumbayá</option>
        <option value="Publico General">El Condado</option>
        <option value="Estudiante">El Inca</option>
        <option value="Docente">El Quinche</option>
        <option value="Club Deportivo de la Universidad">Gualea</option>
        <option value="Publico General">Guamaní</option>
        <option value="Estudiante">Guangopolo</option>
        <option value="Docente">Guayllabamba</option>
        <option value="Club Deportivo de la Universidad">Iñaquito</option>
        <option value="Publico General">Itchimbía</option>
        <option value="Estudiante">Jipijapa</option>
        <option value="Docente">Kennedy</option>
        <option value="Club Deportivo de la Universidad">La Argelia</option>
        <option value="Publico General">La Ecuatoriana</option>
        <option value="Estudiante">La Ecuatoriana</option>
        <option value="Docente">La Ferroviaria</option>
        <option value="Club Deportivo de la Universidad">La Libertad</option>
        <option value="Publico General">La Mena</option>
        <option value="Estudiante">La Merced</option>
        <option value="Docente">Llano Chico</option>
        <option value="Club Deportivo de la Universidad">Lloa</option>
        <option value="Publico General">Magdalena</option>
        <option value="Estudiante">Marical Sucre</option>
        <option value="Docente">Nanegal</option>
        <option value="Club Deportivo de la Universidad">Nanegalito</option>
        <option value="Publico General">Nayón</option>
        <option value="Estudiante">Nono</option>
        <option value="Docente">Pacto</option>
        <option value="Club Deportivo de la Universidad">Perucho</option>
        <option value="Publico General">Pifo</option>
        <option value="Estudiante">Píntag</option>
        <option value="Docente">Pomasqui</option>
        <option value="Club Deportivo de la Universidad">Ponceano</option>
        <option value="Publico General">Puéllaro</option>
        <option value="Estudiante">Puembo</option>
        <option value="Docente">Puengasí</option>
        <option value="Club Deportivo de la Universidad">Quitumbe</option>
        <option value="Publico General">Rumipamba</option>
        <option value="Estudiante">San Antonio de Pichincha</option>
        <option value="Docente">San Bartolo</option>
        <option value="Club Deportivo de la Universidad">San José de Minas</option>
        <option value="Publico General">San Juan</option>
        <option value="Estudiante">Solanda</option>
        <option value="Docente">Tababela</option>
        <option value="Club Deportivo de la Universidad">Tumbaco</option>
        <option value="Publico General">Yaruquí</option>
        <option value="Estudiante">Zámbiza</option>
      </select>
    </div>

    <!-- Pregunta 3 -->
    <div class="input-container ic1 input">
      3 ¿Cuál es el nivel educativo más alto que ha terminado tu padre (padrastro o representante)?
      <div style="text-align: justify;">
        <label>
          <input type="radio" v-model="stepData.socioEcon3" name="socioEcon3" value="Primaria completa o incompleta" required>
          Primaria completa o incompleta
        </label>
        <br>
        <label>
          <input type="radio" v-model="stepData.socioEcon3" name="socioEcon3" value="Secundaria incompleta" required>
          Secundaria incompleta
        </label>
        <br>
        <label>
          <input type="radio" v-model="stepData.socioEcon3" name="socioEcon3" value="Secundaria completa" required>
          Secundaria completa
        </label>
        <br>
        <label>
          <input type="radio" v-model="stepData.socioEcon3" name="socioEcon3" value="Superior no universitario (Ej: Instituto Superior, etc)" required>
          Superior no universitario (Ej: Instituto Superior, etc)
        </label>
        <br>
        <label>
          <input type="radio" v-model="stepData.socioEcon3" name="socioEcon3" value="Estudios universitarios incompletos" required>
          Estudios universitarios incompletos
        </label>
        <br>
        <label>
          <input type="radio" v-model="stepData.socioEcon3" name="socioEcon3" value="Estudios universitarios completos" required>
          Estudios universitarios completos
        </label>
        <br>
        <label>
          <input type="radio" v-model="stepData.socioEcon3" name="socioEcon3" value="Postgrado" required>
          Postgrado
        </label>
        <br>
        <label>
          <input type="radio" v-model="stepData.socioEcon3" name="socioEcon3" value="Lo desconozco" required>
          Lo desconozco
        </label>
      </div>
    </div>

    <!-- Pregunta 4 -->
    <div class="input-container ic1 input">
      4 ¿Cuál es el nivel educativo más alto que ha terminado tu madre (madrastra o representante)?
      <div style="text-align: justify;">
        <label>
          <input type="radio" v-model="stepData.socioEcon4" name="socioEcon4" value="Primaria completa o incompleta" required>
          Primaria completa o incompleta
        </label>
        <br>
        <label>
          <input type="radio" v-model="stepData.socioEcon4" name="socioEcon4" value="Secundaria incompleta" required>
          Secundaria incompleta
        </label>
        <br>
        <label>
          <input type="radio" v-model="stepData.socioEcon4" name="socioEcon4" value="Secundaria completa" required>
          Secundaria completa
        </label>
        <br>
        <label>
          <input type="radio" v-model="stepData.socioEcon4" name="socioEcon4" value="Superior no universitario (Ej: Instituto Superior, etc)" required>
          Superior no universitario (Ej: Instituto Superior, etc)
        </label>
        <br>
        <label>
          <input type="radio" v-model="stepData.socioEcon4" name="socioEcon4" value="Estudios universitarios incompletos" required>
          Estudios universitarios incompletos
        </label>
        <br>
        <label>
          <input type="radio" v-model="stepData.socioEcon4" name="socioEcon4" value="Estudios universitarios completos" required>
          Estudios universitarios completos
        </label>
        <br>
        <label>
          <input type="radio" v-model="stepData.socioEcon4" name="socioEcon4" value="Postgrado" required>
          Postgrado
        </label>
        <br>
        <label>
          <input type="radio" v-model="stepData.socioEcon4" name="socioEcon4" value="Lo desconozco" required>
          Lo desconozco
        </label>
      </div>
    </div>

    <!-- Pregunta 5 -->
    <div class="input-container ic1 input">
      5 El nivel ocupacional del padre/padrastro/representante es
      <div style="text-align: justify;">
        <label>
          <input type="radio" v-model="stepData.socioEcon5" name="socioEcon5" value="Población inactiva" required>
          Población inactiva
        </label>
        <br>
        <label>
          <input type="radio" v-model="stepData.socioEcon5" name="socioEcon5" value="Labores domésticas en el propio hogar" required>
          Labores domésticas en el propio hogar
        </label>
        <br>
        <label>
          <input type="radio" v-model="stepData.socioEcon5" name="socioEcon5" value="Trabajadores no cualificados" required>
          Trabajadores no cualificados
        </label>
        <br>
        <label>
          <input type="radio" v-model="stepData.socioEcon5" name="socioEcon5" value="Trabajadores cualificados en agricultura y pesca; artesanos y trabajadores cualificados de industrias manufactureras, construcción y minería" required>
          Trabajadores cualificados en agricultura y pesca; artesanos y trabajadores cualificados de industrias manufactureras, construcción y minería
        </label>
        <br>
        <label>
          <input type="radio" v-model="stepData.socioEcon5" name="socioEcon5" value="Trabajadores de servicios; fuerzas armadas hasta suboficiales" required>
          Trabajadores de servicios; fuerzas armadas hasta suboficiales
        </label>
        <br>
        <label>
          <input type="radio" v-model="stepData.socioEcon5" name="socioEcon5" value="Técnicos y profesionales de apoyo; empleados administrativos; pequeños empresarios" required>
          Técnicos y profesionales de apoyo; empleados administrativos; pequeños empresarios
        </label>
        <br>
        <label>
          <input type="radio" v-model="stepData.socioEcon5" name="socioEcon5" value="Técnicos, profesionales, científicos, intelectuales; fuerzas armadas desde oficiales" required>
          Técnicos, profesionales, científicos, intelectuales; fuerzas armadas desde oficiales
        </label>
        <br>
        <label>
          <input type="radio" v-model="stepData.socioEcon5" name="socioEcon5" value="Directivos de empresas o de la Administración pública" required>
          Directivos de empresas o de la Administración pública
        </label>
        <br>
        <label>
          <input type="radio" v-model="stepData.socioEcon5" name="socioEcon5" value="Lo desconozco" required>
          Lo desconozco
        </label>
      </div>
    </div>

    <!-- Pregunta 6 -->
    <div class="input-container ic1 input">
      6 El nivel ocupacional de la madre/madrastra/representante es
      <div style="text-align: justify;">
        <label>
          <input type="radio" v-model="stepData.socioEcon6" name="socioEcon6" value="Población inactiva" required>
          Población inactiva
        </label>
        <br>
        <label>
          <input type="radio" v-model="stepData.socioEcon6" name="socioEcon6" value="Labores domésticas en el propio hogar" required>
          Labores domésticas en el propio hogar
        </label>
        <br>
        <label>
          <input type="radio" v-model="stepData.socioEcon6" name="socioEcon6" value="Trabajadores no cualificados" required>
          Trabajadores no cualificados
        </label>
        <br>
        <label>
          <input type="radio" v-model="stepData.socioEcon5" name="socioEcon6" value="Trabajadores cualificados en agricultura y pesca; artesanos y trabajadores cualificados de industrias manufactureras, construcción y minería" required>
          Trabajadores cualificados en agricultura y pesca; artesanos y trabajadores cualificados de industrias manufactureras, construcción y minería
        </label>
        <br>
        <label>
          <input type="radio" v-model="stepData.socioEcon6" name="socioEcon6" value="Trabajadores de servicios; fuerzas armadas hasta suboficiales" required>
          Trabajadores de servicios; fuerzas armadas hasta suboficiales
        </label>
        <br>
        <label>
          <input type="radio" v-model="stepData.socioEcon6" name="socioEcon6" value="Técnicos y profesionales de apoyo; empleados administrativos; pequeños empresarios" required>
          Técnicos y profesionales de apoyo; empleados administrativos; pequeños empresarios
        </label>
        <br>
        <label>
          <input type="radio" v-model="stepData.socioEcon6" name="socioEcon6" value="Técnicos, profesionales, científicos, intelectuales; fuerzas armadas desde oficiales" required>
          Técnicos, profesionales, científicos, intelectuales; fuerzas armadas desde oficiales
        </label>
        <br>
        <label>
          <input type="radio" v-model="stepData.socioEcon6" name="socioEcon6" value="Directivos de empresas o de la Administración pública" required>
          Directivos de empresas o de la Administración pública
        </label>
        <br>
        <label>
          <input type="radio" v-model="stepData.socioEcon6" name="socioEcon6" value="Lo desconozco" required>
          Lo desconozco
        </label>
      </div>
    </div>

    <!-- Pregunta 7 a -->
    <div class="input-container ic1 input">
      7 En tu casa, disponen de Teléfono fijo
      <div>
        <label>
          <input type="radio" v-model="stepData.socioEcon7" name="socioEcon7" value="si" required>
          si
        </label>
        <label>
          <input type="radio" v-model="stepData.socioEcon7" name="socioEcon7" value="no" required>
          no
        </label>
      </div>
    </div>

    <!-- Pregunta 7 b -->
    <div class="input-container ic1 input">
      8 En tu casa, disponen de Teléfono celular
      <div>
        <label>
          <input type="radio" v-model="stepData.socioEcon8" name="socioEcon8" value="si" required>
          si
        </label>
        <label>
          <input type="radio" v-model="stepData.socioEcon8" name="socioEcon8" value="no" required>
          no
        </label>
      </div>
    </div>

    <!-- Pregunta 7 c -->
    <div class="input-container ic1 input">
      9 En tu casa, disponen de Tablet
      <div>
        <label>
          <input type="radio" v-model="stepData.socioEcon9" name="socioEcon9" value="si" required>
          si
        </label>
        <label>
          <input type="radio" v-model="stepData.socioEcon9" name="socioEcon9" value="no" required>
          no
        </label>
      </div>
    </div>

    <!-- Pregunta 7 d -->
    <div class="input-container ic1 input">
      10 En tu casa, disponen de Computadora
      <div>
        <label>
          <input type="radio" v-model="stepData.socioEcon10" name="socioEcon10" value="si" required>
          si
        </label>
        <label>
          <input type="radio" v-model="stepData.socioEcon10" name="socioEcon10" value="no" required>
          no
        </label>
      </div>
    </div>

    <!-- Pregunta 7 e -->
    <div class="input-container ic1 input">
      11 En tu casa, disponen de Conexión a internet
      <div>
        <label>
          <input type="radio" v-model="stepData.socioEcon11" name="socioEcon11" value="si" required>
          si
        </label>
        <label>
          <input type="radio" v-model="stepData.socioEcon11" name="socioEcon11" value="no" required>
          no
        </label>
      </div>
    </div>

    <!-- Pregunta 7 f -->
    <div class="input-container ic1 input">
      12 En tu casa, disponen de Televisor digital, por cable o satélite
      <div>
        <label>
          <input type="radio" v-model="stepData.socioEcon12" name="socioEcon12" value="si" required>
          si
        </label>
        <label>
          <input type="radio" v-model="stepData.socioEcon12" name="socioEcon12" value="no" required>
          no
        </label>
      </div>
    </div>

    <!-- Pregunta 7 g -->
    <div class="input-container ic1 input">
      13 En tu casa, disponen de Auto
      <div>
        <label>
          <input type="radio" v-model="stepData.socioEcon13" name="socioEcon13" value="si" required>
          si
        </label>
        <label>
          <input type="radio" v-model="stepData.socioEcon13" name="socioEcon13" value="no" required>
          no
        </label>
      </div>
    </div>

    <!-- Pregunta 8 a -->
    <div class="input-container ic1 input">
      14 En tu casa, disponen de Lugar para Estudiar
      <div>
        <label>
          <input type="radio" v-model="stepData.socioEcon14" name="socioEcon14" value="si" required>
          si
        </label>
        <label>
          <input type="radio" v-model="stepData.socioEcon14" name="socioEcon14" value="no" required>
          no
        </label>
      </div>
    </div>

    <!-- Pregunta 8 b -->
    <div class="input-container ic1 input">
      15 En tu casa, disponen de Mesa de estudio
      <div>
        <label>
          <input type="radio" v-model="stepData.socioEcon15" name="socioEcon15" value="si" required>
          si
        </label>
        <label>
          <input type="radio" v-model="stepData.socioEcon15" name="socioEcon15" value="no" required>
          no
        </label>
      </div>
    </div>

    <!-- Pregunta 8 c -->
    <div class="input-container ic1 input">
      16 En tu casa, disponen de Material de consulta y apoyo escolar
      <div>
        <label>
          <input type="radio" v-model="stepData.socioEcon16" name="socioEcon16" value="si" required>
          si
        </label>
        <label>
          <input type="radio" v-model="stepData.socioEcon16" name="socioEcon16" value="no" required>
          no
        </label>
      </div>
    </div>

    <!-- Pregunta 9 -->
    <div class="input-container ic1 input">
      17 Aproximadamente, ¿cuántos libros hay en tu casa? Excluye revistas, libros de texto o libros infantiles
      <div style="text-align: justify;">
        <label>
          <input type="radio" v-model="stepData.socioEcon17" name="socioEcon17" value="0-10 libros" required>
          0-10 libros
        </label>
        <br>
        <label>
          <input type="radio" v-model="stepData.socioEcon17" name="socioEcon17" value="11-25 libros" required>
          11-25 libros
        </label>
        <br>
        <label>
          <input type="radio" v-model="stepData.socioEcon17" name="socioEcon17" value="26-50 libros" required>
          26-50 libros
        </label>
        <br>
        <label>
          <input type="radio" v-model="stepData.socioEcon17" name="socioEcon17" value="51 o más libros" required>
          51 o más libros
        </label>
      </div>
    </div>

    <!-- Pregunta 10 -->
    <div class="input-container ic1 input">
      18  ¿A dónde acude el Jefe de Hogar para atención médica cuando él tiene algún problema de salud?
      <div style="text-align: justify;">
        <label>
          <input type="radio" v-model="stepData.socioEcon18" name="socioEcon18" value="Centro de salud/ farmacia / naturista" required>
          Centro de salud/ farmacia / naturista
        </label>
        <br>
        <label>
          <input type="radio" v-model="stepData.socioEcon18" name="socioEcon18" value="Hospital del Ministerio de Salud / Hospital del Día" required>
          Hospital del Ministerio de Salud / Hospital del Día
        </label>
        <br>
        <label>
          <input type="radio" v-model="stepData.socioEcon18" name="socioEcon18" value="Seguro Social / Hospital FFAA / Hospital de Policía" required>
          Seguro Social / Hospital FFAA / Hospital de Policía
        </label>
        <br>
        <label>
          <input type="radio" v-model="stepData.socioEcon18" name="socioEcon18" value="Médico particular en consultorio" required>
          Médico particular en consultorio
        </label>
        <br>
        <label>
          <input type="radio" v-model="stepData.socioEcon18" name="socioEcon18" value="Médico particular en clínica privada" required>
          Médico particular en clínica privada
        </label>
      </div>
    </div>

        <!-- Pregunta 10 -->
    <div class="input-container ic1 input">
      19  Cuál de las siguientes categorías se aproxima más al salario mensual de su casa?
      <div style="text-align: justify;">
        <label>
          <input type="radio" v-model="stepData.socioEcon19" name="socioEcon19" value="Menos de 380 dólares al mes aproximadamente" required>
          Menos de 380 dólares al mes aproximadamente
        </label>
        <br>
        <label>
          <input type="radio" v-model="stepData.socioEcon19" name="socioEcon19" value="Entre 380 – 570 dólares al mes aproximadamente" required>
          Entre 380 – 570 dólares al mes aproximadamente
        </label>
        <br>
        <label>
          <input type="radio" v-model="stepData.socioEcon19" name="socioEcon19" value="Entre 570 – 760 dólares al mes aproximadamente" required>
          Entre 570 – 760 dólares al mes aproximadamente
        </label>
        <br>
        <label>
          <input type="radio" v-model="stepData.socioEcon19" name="socioEcon19" value="Más de 760 dólares al mes aproximadamente" required>
          Más de 760 dólares al mes aproximadamente
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
