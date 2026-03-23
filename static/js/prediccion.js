/**
 * prediccion.js
 * Maneja la interacción del formulario de predicción de notas
 * con regresión lineal.
 */

document.addEventListener("DOMContentLoaded", function () {
    const formulario = document.getElementById("formularioPrediccion");
    const campoHoras = document.getElementById("horas");
    const mensajeError = document.getElementById("mensajeError");

    if (formulario) {
        formulario.addEventListener("submit", function (evento) {
            const horasIngresadas = parseFloat(campoHoras.value);

            // Validar que el valor esté en un rango razonable
            if (isNaN(horasIngresadas) || horasIngresadas < 0 || horasIngresadas > 168) {
                evento.preventDefault();
                mensajeError.textContent = "Por favor ingresa un número de horas válido (entre 0 y 168).";
                mensajeError.style.display = "block";
                return;
            }

            mensajeError.style.display = "none";

            // Mostrar indicador de carga mientras Flask procesa
            const botonPredecir = formulario.querySelector("button[type='submit']");
            botonPredecir.textContent = "Calculando...";
            botonPredecir.disabled = true;
        });
    }
});
