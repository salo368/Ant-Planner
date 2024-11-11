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
    const primerDiv = event.target.querySelector("div");
    const contenedorCol = event.target.closest(".kanban-list");
    const equStatus = obtenerEquivalenteStatusReverse(contenedorCol.id);
    actualizarEstadoPorTitulo(tareaArrastrada.id, equStatus);
    primerDiv.appendChild(tareaArrastrada);
  } else {
    tareaArrastrada.style.opacity = 1;
    const contenedor = event.target
      .closest(".kanban-body")
      .querySelector("div");
    const contenedorCol = event.target.closest(".kanban-list");
    const equStatus = obtenerEquivalenteStatusReverse(contenedorCol.id);
    actualizarEstadoPorTitulo(tareaArrastrada.id, equStatus);
    const primerHijo = contenedor.firstChild;
    contenedor.insertBefore(tareaArrastrada, primerHijo);
  }
  console.log( tareas)
  console.log( tareasCopy)
  if (sonListasIguales(tareasCopy, tareas)) {
    buttonUpdateChange.style.visibility = "hidden";
  } else {
    buttonUpdateChange.style.visibility = "visible";
  }
}

function terminarArrastre(event) {
  event.target.style.opacity = 1;
}
