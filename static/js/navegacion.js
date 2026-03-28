function toggleHamburgerMenu() {
    const menu = document.getElementById("hamburgerMenu");

    if (menu.style.display === "block") {
        menu.style.display = "none";
    } else {
        menu.style.display = "block";
    }
}

function toggleSub(id) {
    const submenu = document.getElementById(id);

    if (submenu.style.display === "block") {
        submenu.style.display = "none";
    } else {
        submenu.style.display = "block";
    }
}

// Cerrar menú al hacer click fuera
document.addEventListener("click", function(event) {
    const menu = document.getElementById("hamburgerMenu");
    const button = document.querySelector(".hamburger-btn");

    if (!menu || !button) return;

    const clickedInsideMenu = menu.contains(event.target);
    const clickedButton = button.contains(event.target);

    if (!clickedInsideMenu && !clickedButton) {
        menu.style.display = "none";
    }
});