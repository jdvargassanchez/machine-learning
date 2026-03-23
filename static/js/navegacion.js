/**
 * navegacion.js
 * Maneja los toggles de navegación del index.
 */

function toggle(btn, menuId) {
    const menu = document.getElementById(menuId);
    const isOpen = menu.style.display === 'flex';
    menu.style.display = isOpen ? 'none' : 'flex';
    btn.classList.toggle('open', !isOpen);
}

function toggleSub(menuId) {
    const menu = document.getElementById(menuId);
    menu.style.display = menu.style.display === 'flex' ? 'none' : 'flex';
}

// Legacy aliases (in case other pages call old function names)
function alternarCasosDeUso()           { toggle(document.querySelector('[onclick*="menuCasos"]'), 'menuCasos'); }
function alternarAprendizajeSupervisado() { toggle(document.querySelector('[onclick*="menuSupervisado"]'), 'menuSupervisado'); }
function alternarRegresionLineal()       { toggleSub('menuRegresion'); }
