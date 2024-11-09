document.addEventListener("DOMContentLoaded", () => {
    const daysContainer = document.getElementById("daysContainer");
    const prevWeekBtn = document.getElementById("prevWeek");
    const nextWeekBtn = document.getElementById("nextWeek");
    const todayBtn = document.getElementById("todayBtn");
    const currentMonthEl = document.getElementById("currentMonth");
    const dateRangeEl = document.getElementById("dateRange");
    const timeColumn = document.getElementById("timeColumn");
    const mainSubCont = document.getElementById("mainSubCont");
    const popup = document.createElement("div");
    popup.className = "popup";
    popup.style.display = "none";
    mainSubCont.appendChild(popup);
  
    let currentDate = new Date();
    let meetingDay = 3; // 3 representa el miércoles
  
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
      daysContainer.innerHTML = ""; // Limpiar el contenedor de días
  
      const startOfWeek = getStartOfWeek(currentDate);
      const endOfWeek = new Date(startOfWeek);
      endOfWeek.setDate(endOfWeek.getDate() + 6);
  
      for (let i = 0; i < 7; i++) {
        const day = new Date(startOfWeek);
        day.setDate(day.getDate() + i);
  
        // Ejemplo de título y horas de la reunión
        let meetingTitle = "";
        let startTime = "";
        let endTime = "";
  
        // Mostrar la reunión solo en el día especificado y si la fecha actual está dentro de la semana actual
        if (day.getDay() === meetingDay && day >= startOfWeek && day <= endOfWeek && isCurrentWeek(day)) {
          meetingTitle = "Reunión Importante";
          startTime = "14:30";
          endTime = "16:00";
        }
  
        const dayColumn = createDayColumn(day, meetingTitle, startTime, endTime);
        daysContainer.appendChild(dayColumn);
      }
  
      updateMonthAndDateRange(startOfWeek, endOfWeek);
    }
  
    function isCurrentWeek(date) {
      const today = new Date();
      const startOfWeek = getStartOfWeek(today);
      const endOfWeek = new Date(startOfWeek);
      endOfWeek.setDate(endOfWeek.getDate() + 6);
      return date >= startOfWeek && date <= endOfWeek;
    }
  
    // Función para cambiar el día de la reunión
    function setMeetingDay(day) {
      meetingDay = day;
      renderCalendar();
    }
  
    // Ejemplo de cómo cambiar el día de la reunión a lunes (0 representa el domingo)
    setMeetingDay(2); // Cambia la reunión al lunes
  
    function createDayColumn(date, meetingTitle, startTime, endTime) {
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
  
      // Crear el div flotante para la reunión
      if (meetingTitle && startTime && endTime) {
        const meetingDiv = document.createElement("div");
        meetingDiv.className = "meeting";
        meetingDiv.style.position = "absolute";
        meetingDiv.style.backgroundColor = "lightblue";
        meetingDiv.style.padding = "10px";
        meetingDiv.style.margin = "0 auto"; // Centrar horizontalmente
        meetingDiv.style.left = "0";
        meetingDiv.style.right = "0";
        meetingDiv.style.zIndex = "10";
        meetingDiv.style.width = "80%"; // Ancho fijo para el centrado
        meetingDiv.style.boxShadow = "0 0 5px rgba(0, 0, 0, 0.2)";
        meetingDiv.style.borderRadius = "1vh";
  
        const meetingTitleEl = document.createElement("div");
        meetingTitleEl.className = "meeting-title";
        meetingTitleEl.textContent = meetingTitle;
  
        const meetingTimeEl = document.createElement("div");
        meetingTimeEl.className = "meeting-time";
        meetingTimeEl.textContent = `${startTime} - ${endTime}`;
  
        meetingDiv.appendChild(meetingTitleEl);
        meetingDiv.appendChild(meetingTimeEl);
  
        // Calcular la posición y altura del div basado en la hora de inicio y fin de la reunión
        const [startHour, startMinute] = startTime.split(":").map(Number);
        const [endHour, endMinute] = endTime.split(":").map(Number);
        const startInMinutes = startHour * 60 + startMinute;
        const endInMinutes = endHour * 60 + endMinute;
        const durationInMinutes = endInMinutes - startInMinutes;
  
        meetingDiv.style.top = `${startInMinutes}px`;
        meetingDiv.style.height = `${durationInMinutes}px`;
  
        // Añadir evento click para mostrar el popup
        meetingDiv.addEventListener("click", () => {
          popup.innerHTML = `
                      <div class="popup-content">
                          <h2>${meetingTitle}</h2>
                          <p>Fecha: ${date.toLocaleDateString(
                            "es-ES"
                          )} ${startTime} - ${endTime}</p>
                          <p>Integrantes: Juan, María, Pedro</p>
                          <button id="closePopup">Cerrar</button>
                      </div>
                  `;
          popup.style.display = "block";
          const closePopupBtn = document.getElementById("closePopup");
          closePopupBtn.addEventListener("click", () => {
            popup.style.display = "none";
          });
        });
  
        dayContent.appendChild(meetingDiv);
      }
  
      dayColumn.appendChild(dayContent);
  
      return dayColumn;
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
      const startOfWeek = new Date(date);
      startOfWeek.setDate(date.getDate() - date.getDay());
      return startOfWeek;
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
  
    renderCalendar();
  });