package main

import (
	"encoding/json"
	"log"
	"net/http"

	"github.com/gorilla/mux"
)

type FormInput struct {
	// Estructura para los datos del formulario
	// Asegúrate de que coincida con los datos que estás enviando desde Vue.js
	FirstName string `json:"firstName"`
	LastName  string `json:"lastName"`
	// ... Otros campos del formulario
}

func main() {
	r := mux.NewRouter()

	// Ruta para procesar el formulario
	r.HandleFunc("/submit", submitFormHandler).Methods("POST")

	// Inicia el servidor en el puerto 8000
	log.Fatal(http.ListenAndServe(":5173", r))
}

func submitFormHandler(w http.ResponseWriter, r *http.Request) {
	var formData FormInput
	err := json.NewDecoder(r.Body).Decode(&formData)
	if err != nil {
		http.Error(w, "Error en los datos del formulario", http.StatusBadRequest)
		return
	}

	// Procesar los datos del formulario
	// Puedes realizar las operaciones necesarias, como almacenar los datos en una base de datos, etc.

	// Generar una respuesta
	responseData := map[string]interface{}{
		"message": "Formulario recibido correctamente",
	}
	json.NewEncoder(w).Encode(responseData)
}
