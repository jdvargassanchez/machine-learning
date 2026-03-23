/**
 * navegacion.js
 * Controla los menús desplegables del índice principal.
 */

function alternarCasosDeUso() {
    const menuCasos = document.getElementById("casosDeUso");
    menuCasos.style.display = menuCasos.style.display === "block" ? "none" : "block";
}

function alternarAprendizajeSupervisado() {
    const menuSupervisado = document.getElementById("supervisado");
    menuSupervisado.style.display = menuSupervisado.style.display === "block" ? "none" : "block";
}

function alternarRegresionLineal() {
    const menuRegresion = document.getElementById("menuRegresionLineal");
    menuRegresion.style.display = menuRegresion.style.display === "block" ? "none" : "block";
}
