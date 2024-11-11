const tareas = [
  { id: "task-id-1", title: "Tarea 1", category: "Desarrollo", status: "0" },
  { id: "task-id-2", title: "Tarea 2", category: "Revisión", status: "1" },
  { id: "task-id-3", title: "Tarea 3", category: "Desarrollo", status: "2" },
  { id: "task-id-4", title: "Tarea 4", category: "Test", status: "3" },
  { id: "task-id-5", title: "Tarea 5", category: "Desarrollo", status: "4" },
  { id: "task-id-6", title: "pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp", category: "Desarrollo", status: "3" },
  { id: "task-id-7", title: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum", category: "Desarrollo", status: "3" },
];
const tareasCopy =  JSON.parse(JSON.stringify(tareas));

function obtenerEquivalenteStatus(status) {
  switch (status) {
    case "0":
      return "kanban-todo";
    case "1":
      return "kanban-pause";
    case "2":
      return "kanban-process";
    case "3":
      return "kanban-verify";
    case "4":
      return "kanban-done";
    default:
      return "kanban-done";
  }
}

function obtenerEquivalenteStatusReverse(status) {
  switch (status) {
    case "kanban-todo":
      return "0";
    case "kanban-pause":
      return "1";
    case "kanban-process":
      return "2";
    case "kanban-verify":
      return "3";
    case "kanban-done":
      return "4";
    default:
      return "error";
  }
}

function actualizarEstadoPorTitulo(_id, newStatus) {
  const tarea = tareasCopy.find((tarea) => tarea.id === _id);
  if (tarea) {
    tarea.status = newStatus;
    //console.log(` "${_id}" updated: ${newStatus}`);
  } else {
   // console.log(`Don't find: "${_id}"`);
  }
}

function sonListasIguales(lista1, lista2) {
  if (lista1.length !== lista2.length) {
    return false;
  }

  for (let i = 0; i < lista1.length; i++) {
    if (!sonObjetosIguales(lista1[i], lista2[i])) {
      return false;
    }
  }

  return true;
}

function sonObjetosIguales(obj1, obj2) {
  const claves1 = Object.keys(obj1);
  const claves2 = Object.keys(obj2);

  if (claves1.length !== claves2.length) {
    return false;
  }

  for (let clave of claves1) {
    if (obj1[clave] !== obj2[clave]) {
      return false;
    }
  }

  return true;
}

function construirTareas() {
  tareasCopy.forEach((tarea) => {
    const tareaElemento = document.createElement("div");
    tareaElemento.classList.add("kanban-item");
    tareaElemento.id = tarea.id;
    tareaElemento.draggable = true;
    tareaElemento.style.opacity = 1;
    tareaElemento.ondragstart = (event) => empezarArrastre(event);
    tareaElemento.ondragend = (event) => terminarArrastre(event);

    const titleElemento = document.createElement("div");
    titleElemento.textContent = tarea.title;
    titleElemento.classList.add("kanban-item-title");
    tareaElemento.appendChild(titleElemento);

    const categoryElement = document.createElement("div");
    categoryElement.textContent = `Categoría: ${tarea.category}`;
    categoryElement.classList.add("kanban-item-body");
    tareaElemento.appendChild(categoryElement);
    const equStatus = obtenerEquivalenteStatus(tarea.status);
    const columna = document.getElementById(equStatus);
    const columnaBody = columna.querySelector(".kanban-body div");

    columnaBody.appendChild(tareaElemento);
  });
}

window.onload = construirTareas;
