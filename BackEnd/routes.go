package routes

import (
	"net/http"

	"github.com/gorilla/mux"
)

func RegisterRoutes() *mux.Router {
	r := mux.NewRouter()

	// Definir tus rutas y handlers aquí

	return r
}

func handlerFunc(w http.ResponseWriter, r *http.Request) {
	// Handler code...
}
