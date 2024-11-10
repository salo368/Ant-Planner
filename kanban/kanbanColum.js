let tareaArrastrada = null;

function empezarArrastre(event) {
    if (event.target.classList.contains("kanban-item")) {
        tareaArrastrada = event.target;
        event.target.style.opacity = 0.5;
      } else {
        tareaArrastrada = null;
      }
}

function permitirArrastre(event) {
  event.preventDefault();
}

function soltar(event) {
  event.preventDefault();
  if (event.target.classList.contains("kanban-body")) {
    tareaArrastrada.style.opacity = 1;
    const primerDiv = event.target.querySelector('div');
    primerDiv.appendChild(tareaArrastrada);
  } else {
    tareaArrastrada.style.opacity = 1;
    const contenedor = event.target.closest(".kanban-body").querySelector('div');
    const primerHijo = contenedor.firstChild;
    contenedor.insertBefore(tareaArrastrada, primerHijo);
  }
}

function terminarArrastre(event) {
  event.target.style.opacity = 1;
}
