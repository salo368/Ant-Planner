document.addEventListener("DOMContentLoaded", () => {
  const daysContainer = document.getElementById("daysContainer");
  const prevWeekBtn = document.getElementById("prevWeek");
  const nextWeekBtn = document.getElementById("nextWeek");
  const todayBtn = document.getElementById("todayBtn");
  const currentMonthEl = document.getElementById("currentMonth");
  const dateRangeEl = document.getElementById("dateRange");
  const timeColumn = document.getElementById("timeColumn");

  let currentDate = new Date();
  let events = []; // Array para almacenar los eventos

  const popup = document.createElement("div");
  popup.classList.add("popup");
  popup.style.display = "none";
  const popupContent = document.createElement("div");
  popupContent.classList.add("popup-content");
  popup.appendChild(popupContent);
  document.body.appendChild(popup);

  let activeEvent = null;

  function generateTimeColumn() {
    timeColumn.innerHTML = "";
    for (let i = 0; i < 24; i++) {
      const timeSlot = document.createElement("div");
      timeSlot.className = "time-slot";
      timeSlot.textContent = `${i}:00`;
      timeColumn.appendChild(timeSlot);
    }
  }

  function renderCalendar() {
    generateTimeColumn();
    daysContainer.innerHTML = "";

    const startOfWeek = getStartOfWeek(currentDate);
    const endOfWeek = new Date(startOfWeek);
    endOfWeek.setDate(endOfWeek.getDate() + 6);

    const fragment = document.createDocumentFragment();

    for (let i = 0; i < 7; i++) {
      const day = new Date(startOfWeek);
      day.setDate(day.getDate() + i);

      const dayColumn = createDayColumn(day);
      addEventsToDay(day, dayColumn);
      fragment.appendChild(dayColumn);
    }

    daysContainer.appendChild(fragment);
    updateMonthAndDateRange(startOfWeek, endOfWeek);
  }

  function createDayColumn(date) {
    const dayColumn = document.createElement("div");
    dayColumn.className = "day-column";

    const dayHeader = document.createElement("div");
    dayHeader.className = "day-header";
    dayHeader.textContent = `${date.toLocaleDateString("es-ES", {
      weekday: "short",
    })} ${date.getDate()}`;
    dayColumn.appendChild(dayHeader);

    const dayContent = document.createElement("div");
    dayContent.className = "day-content";

    dayColumn.appendChild(dayContent);
    return dayColumn;
  }

  function addEventsToDay(date, dayColumn) {
    const dayContent = dayColumn.querySelector(".day-content");

    dayContent
      .querySelectorAll(".event")
      .forEach((eventEl) => eventEl.remove());

    const eventsForDay = events.filter((event) =>
      isSameDay(date, new Date(event.date))
    );

    eventsForDay.forEach((event) => {
      const eventEl = document.createElement("div");
      eventEl.className = "event";
      setEventPosition(event, eventEl);

      eventEl.addEventListener("click", () => {
        if (activeEvent === event) {
          hidePopup();
        } else {
          showPopup(event);
        }
      });

      dayContent.appendChild(eventEl);
    });
  }

  function setEventPosition(event, eventEl) {
    const startTime = event.startTime.split(":");
    const endTime = event.endTime.split(":");
    const startHour = parseInt(startTime[0]);
    const startMinute = parseInt(startTime[1]);
    const endHour = parseInt(endTime[0]);
    const endMinute = parseInt(endTime[1]);

    const startTop = (startHour * 60 + startMinute) * 1;
    const eventHeight =
      (endHour * 60 + endMinute - (startHour * 60 + startMinute)) * 1;

    eventEl.style.top = `${startTop}px`;
    eventEl.style.height = `${eventHeight}px`;

    const durationInMinutes =
      endHour * 60 + endMinute - (startHour * 60 + startMinute);

    if (durationInMinutes < 20) {
      eventEl.classList.add("short-event");
    } else if (durationInMinutes < 40) {
      eventEl.textContent = event.title;
    } else {
      eventEl.innerHTML = `${event.title}<br>(${formatTime(
        event.startTime
      )} - ${formatTime(event.endTime)})`;
    }
  }

  function showPopup(event) {
    activeEvent = event;
    const sortedParticipants = [
      event.host,
      ...event.participants.filter((participant) => participant !== event.host),
    ];

    // Convertir la fecha al formato local
    const localDate = new Date(event.date);

    // Asegurarse de que la fecha es sin hora (00:00) para evitar problemas de zona horaria
    localDate.setHours(0, 0, 0, 0); // Establecer la hora a las 00:00:00

    // Formatear la fecha para el input de tipo date (YYYY-MM-DD)
    const year = localDate.getFullYear();
    const month = (localDate.getMonth() + 1).toString().padStart(2, "0"); // Mes con 2 dígitos
    const day = localDate.getDate().toString().padStart(2, "0"); // Día con 2 dígitos
    const formattedDate = `${year}-${month}-${day}`;

    // Rellenar el contenido del popup
    popupContent.innerHTML = `
    <button id="closePopup" class="close-popup" style="position: absolute; top: 15px; right: 15px; background: none; border: none; cursor: pointer;">
      <svg width="20px" height="20px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path fill-rule="evenodd" clip-rule="evenodd" d="M19.207 6.207a1 1 0 0 0-1.414-1.414L12 10.586 6.207 4.793a1 1 0 0 0-1.414 1.414L10.586 12l-5.793 5.793a1 1 0 1 0 1.414 1.414L12 13.414l5.793 5.793a1 1 0 0 0 1.414-1.414L13.414 12l5.793-5.793z" fill="#303030"/>
      </svg>
    </button>
    <h2><input type="text" id="eventTitle" value="${event.title}" /></h2>
    <p><strong>Fecha:</strong> <input type="date" id="eventDate" value="${formattedDate}" /></p>
    <p><strong>Hora de inicio:</strong> <input type="time" id="startTime" value="${
      event.startTime
    }" /></p>
    <p><strong>Hora de fin:</strong> <input type="time" id="endTime" value="${
      event.endTime
    }" /></p>
    <p><strong>Participantes:</strong></p>
    <ul id="participantsList">
      ${sortedParticipants
        .map(
          (participant) =>
            `<li data-participant="${participant}" class="participant">${participant} ${
              participant === event.host ? "⭐" : ""
            } <span class="remove-participant" style="display:none; cursor: pointer; right: 50px; position:absolute;">
              <svg width="20px" height="20px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path fill-rule="evenodd" clip-rule="evenodd" d="M19.207 6.207a1 1 0 0 0-1.414-1.414L12 10.586 6.207 4.793a1 1 0 0 0-1.414 1.414L10.586 12l-5.793 5.793a1 1 0 1 0 1.414 1.414L12 13.414l5.793 5.793a1 1 0 0 0 1.414-1.414L13.414 12l5.793-5.793z" fill="#303030"/>
              </svg>
            </span></li>`
        )
        .join("")}
    </ul>
    <div style="margin-top: 15px;">
      <label for="audioUpload"><strong>Subir archivo de audio:</strong></label>
      <input type="file" id="audioUpload" accept="audio/*" style="width: 100%; padding: 8px;">
      <div id="audioError" style="color: red; display: none;">Por favor, sube un archivo de audio válido.</div>
    </div>
    <button id="saveChanges" style="margin-top: 20px;">Guardar cambios</button>
  `;

    // Mostrar el popup
    popup.style.display = "block";
    document.getElementById("closePopup").addEventListener("click", hidePopup);

    // Guardar los cambios
    document.getElementById("saveChanges").addEventListener("click", () => {
      saveEventChanges(event);
    });

    const audioUpload = document.getElementById("audioUpload");
    const audioError = document.getElementById("audioError");

    audioUpload.addEventListener("change", (e) => {
      const file = e.target.files[0];
      if (file && !file.type.startsWith("audio/")) {
        audioError.style.display = "block";
        e.target.value = ""; // Limpiar el campo
      } else {
        audioError.style.display = "none";
      }
    });

    // Agregar la funcionalidad de eliminar participantes al pasar el ratón
    const participants = document.querySelectorAll(".participant");
    participants.forEach((participant) => {
      const removeBtn = participant.querySelector(".remove-participant");
      participant.addEventListener("mouseenter", () => {
        if (!participant.textContent.includes("⭐")) {
          removeBtn.style.display = "inline"; // Mostrar la "X"
          participant.classList.add("hover-participant"); // Añadir sombreado
        }
      });
      participant.addEventListener("mouseleave", () => {
        removeBtn.style.display = "none"; // Ocultar la "X"
        participant.classList.remove("hover-participant"); // Quitar sombreado
      });
      removeBtn.addEventListener("click", () => {
        // Eliminar el participante de la lista
        const participantName = participant.getAttribute("data-participant");
        removeParticipantFromEvent(event, participantName);
        participant.remove(); // Eliminar el elemento de la lista en el popup
      });
    });
  }

  function removeParticipantFromEvent(event, participantName) {
    if (event.host !== participantName) {
      event.participants = event.participants.filter(
        (participant) => participant !== participantName
      );
    }
  }

  function saveEventChanges(event) {
    const title = document.getElementById("eventTitle").value;
    const date = document.getElementById("eventDate").value; // Obtener el valor del input
    const startTime = document.getElementById("startTime").value;
    const endTime = document.getElementById("endTime").value;

    // Validar que la hora de inicio no sea mayor que la hora de fin
    const startMinutes = convertToMinutes(startTime);
    const endMinutes = convertToMinutes(endTime);
    if (startMinutes >= endMinutes) {
      alert("La hora de inicio no puede ser mayor o igual a la hora de fin.");
      return;
    }

    // Corregir la fecha
    const [year, month, day] = date.split("-").map(Number); // Desglosar la fecha
    const correctedDate = new Date(year, month - 1, day); // Crear una nueva fecha sin que afecte la zona horaria

    // Verificar que el evento no se superponga con otro
    if (isEventOverlapping(correctedDate, startTime, endTime, event)) {
      alert(
        "El evento se superpone con otro evento existente en el mismo día."
      );
      return;
    }

    // Actualizar el evento con los nuevos valores
    event.title = title;
    event.date = correctedDate; // Asignar la fecha corregida
    event.startTime = startTime;
    event.endTime = endTime;

    renderCalendar(); // Volver a renderizar el calendario con los cambios
    hidePopup(); // Ocultar el popup
  }

  function removeParticipantFromEvent(event, participantName) {
    if (event.host !== participantName) {
      event.participants = event.participants.filter(
        (participant) => participant !== participantName
      );
    }
  }

  function saveEventChanges(event) {
    const title = document.getElementById("eventTitle").value;
    const date = document.getElementById("eventDate").value; // Obtener el valor del input
    const startTime = document.getElementById("startTime").value;
    const endTime = document.getElementById("endTime").value;

    // Validar que la hora de inicio no sea mayor que la hora de fin
    const startMinutes = convertToMinutes(startTime);
    const endMinutes = convertToMinutes(endTime);
    if (startMinutes >= endMinutes) {
      alert("La hora de inicio no puede ser mayor o igual a la hora de fin.");
      return;
    }

    // Corregir la fecha
    const [year, month, day] = date.split("-").map(Number); // Desglosar la fecha
    const correctedDate = new Date(year, month - 1, day); // Crear una nueva fecha sin que afecte la zona horaria

    // Verificar que el evento no se superponga con otro
    if (isEventOverlapping(correctedDate, startTime, endTime, event)) {
      alert(
        "El evento se superpone con otro evento existente en el mismo día."
      );
      return;
    }

    // Actualizar el evento con los nuevos valores
    event.title = title;
    event.date = correctedDate; // Asignar la fecha corregida
    event.startTime = startTime;
    event.endTime = endTime;

    renderCalendar(); // Volver a renderizar el calendario con los cambios
    hidePopup(); // Ocultar el popup
  }

  function saveEventChanges(event) {
    const title = document.getElementById("eventTitle").value;
    const date = document.getElementById("eventDate").value; // Obtener el valor del input
    const startTime = document.getElementById("startTime").value;
    const endTime = document.getElementById("endTime").value;

    // Validar que la hora de inicio no sea mayor que la hora de fin
    const startMinutes = convertToMinutes(startTime);
    const endMinutes = convertToMinutes(endTime);
    if (startMinutes >= endMinutes) {
      alert("La hora de inicio no puede ser mayor o igual a la hora de fin.");
      return;
    }

    // Corregir la fecha
    const [year, month, day] = date.split("-").map(Number); // Desglosar la fecha
    const correctedDate = new Date(year, month - 1, day); // Crear una nueva fecha sin que afecte la zona horaria

    // Verificar que el evento no se superponga con otro
    if (isEventOverlapping(correctedDate, startTime, endTime, event)) {
      alert(
        "El evento se superpone con otro evento existente en el mismo día."
      );
      return;
    }

    // Actualizar el evento con los nuevos valores
    event.title = title;
    event.date = correctedDate; // Asignar la fecha corregida
    event.startTime = startTime;
    event.endTime = endTime;

    renderCalendar(); // Volver a renderizar el calendario con los cambios
    hidePopup(); // Ocultar el popup
  }

  function isEventOverlapping(date, startTime, endTime, currentEvent) {
    // Filtrar los eventos que ocurren en el mismo día
    const eventsForDay = events.filter((event) =>
      isSameDay(date, new Date(event.date))
    );

    // Convertir las horas de inicio y fin del evento en minutos
    const startMinutes = convertToMinutes(startTime);
    const endMinutes = convertToMinutes(endTime);

    for (let event of eventsForDay) {
      // Evitar la comprobación de superposición con el mismo evento (cuando se edita)
      if (event === currentEvent) continue;

      // Convertir las horas de inicio y fin del evento existente en minutos
      const eventStartMinutes = convertToMinutes(event.startTime);
      const eventEndMinutes = convertToMinutes(event.endTime);

      // Verificar si el inicio del nuevo evento coincide con la hora de fin de otro evento
      if (startMinutes === eventEndMinutes) {
        return true; // El inicio del nuevo evento coincide con el fin de otro evento
      }

      // Verificar si hay superposición de eventos
      if (startMinutes < eventEndMinutes && endMinutes > eventStartMinutes) {
        return true; // Superposición encontrada
      }
    }

    return false; // No hay superposición
  }

  function convertToMinutes(time) {
    const [hours, minutes] = time.split(":").map(Number);
    return hours * 60 + minutes; // Convertir la hora a minutos
  }

  function hidePopup() {
    popup.style.display = "none";
    document.body.style.overflow = "auto";
    activeEvent = null;
  }

  function isSameDay(date1, date2) {
    return (
      date1.getDate() === date2.getDate() &&
      date1.getMonth() === date2.getMonth() &&
      date1.getFullYear() === date2.getFullYear()
    );
  }

  function formatTime(time) {
    return time.length === 4 ? `0${time}` : time;
  }

  function updateMonthAndDateRange(startOfWeek, endOfWeek) {
    currentMonthEl.textContent = startOfWeek.toLocaleDateString("es-ES", {
      month: "long",
      year: "numeric",
    });
    dateRangeEl.textContent = `${startOfWeek.getDate()} ${startOfWeek.toLocaleDateString(
      "es-ES",
      { month: "short" }
    )} - ${endOfWeek.getDate()} ${endOfWeek.toLocaleDateString("es-ES", {
      month: "short",
      year: "numeric",
    })}`;
  }

  function getStartOfWeek(date) {
    const day = date.getDay();
    const diff = date.getDate() - day;
    const startOfWeek = new Date(date);
    startOfWeek.setDate(diff);
    return startOfWeek;
  }

  function addEvent(date, startTime, endTime, title, participants, host) {
    events.push({
      date: new Date(date),
      startTime,
      endTime,
      title,
      participants,
      host,
    });
    renderCalendar();
  }

  prevWeekBtn.addEventListener("click", () => {
    currentDate.setDate(currentDate.getDate() - 7);
    renderCalendar();
  });

  nextWeekBtn.addEventListener("click", () => {
    currentDate.setDate(currentDate.getDate() + 7);
    renderCalendar();
  });

  todayBtn.addEventListener("click", () => {
    currentDate = new Date();
    renderCalendar();
  });

  // Cargar eventos de ejemplo
  addEvent(
    "2024-11-14",
    "01:00",
    "01:40",
    "Reunión de planificación",
    ["Ana", "Luis"],
    "Carlos"
  );
  addEvent(
    "2024-11-13",
    "14:00",
    "14:30",
    "Reunión de equipo",
    ["Carlos"],
    "Ana"
  );
});
