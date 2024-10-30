document.addEventListener('DOMContentLoaded', () => {
    const daysContainer = document.getElementById('daysContainer');
    const prevWeekBtn = document.getElementById('prevWeek');
    const nextWeekBtn = document.getElementById('nextWeek');
    const todayBtn = document.getElementById('todayBtn');
    const currentMonthEl = document.getElementById('currentMonth');
    const dateRangeEl = document.getElementById('dateRange');
    const viewBtns = document.querySelectorAll('.view-btn');

    let currentDate = new Date(2024, 5, 24); // 24 de junio de 2024
    let currentView = 'week';

    const events = [
        { id: 1, title: 'Preparación Presentación Cliente', start: new Date(2024, 5, 24, 8, 0), end: new Date(2024, 5, 24, 9, 0), type: 'purple' },
        { id: 2, title: 'Planificación Reunión Cliente', start: new Date(2024, 5, 24, 9, 0), end: new Date(2024, 5, 24, 10, 30), type: 'blue' },
        { id: 3, title: 'Reunión Inicio Nuevo Proyecto', start: new Date(2024, 5, 26, 8, 0), end: new Date(2024, 5, 26, 9, 0), type: 'blue' },
        // Añade más eventos aquí
    ];

    function renderCalendar() {
        daysContainer.innerHTML = '';
        const startOfWeek = getStartOfWeek(currentDate);
        const endOfWeek = new Date(startOfWeek);
        endOfWeek.setDate(endOfWeek.getDate() + 6);

        for (let i = 0; i < 7; i++) {
            const day = new Date(startOfWeek);
            day.setDate(day.getDate() + i);
            const dayColumn = createDayColumn(day);
            daysContainer.appendChild(dayColumn);
        }

        updateMonthAndDateRange(startOfWeek, endOfWeek);
    }

    function createDayColumn(date) {
        const dayColumn = document.createElement('div');
        dayColumn.className = 'day-column';

        const dayHeader = document.createElement('div');
        dayHeader.className = 'day-header';
        dayHeader.textContent = `${date.toLocaleDateString('es-ES', { weekday: 'short' })} ${date.getDate()}`;
        dayColumn.appendChild(dayHeader);

        const dayContent = document.createElement('div');
        dayContent.className = 'day-content';
        dayColumn.appendChild(dayContent);

        renderEventsForDay(dayContent, date);

        return dayColumn;
    }

    function renderEventsForDay(dayContent, date) {
        const dayEvents = events.filter(event => 
            event.start.toDateString() === date.toDateString()
        );

        dayEvents.forEach(event => {
            const eventElement = document.createElement('div');
            eventElement.className = `event event-${event.type}`;
            eventElement.textContent = event.title;

            const startHour = event.start.getHours() + event.start.getMinutes() / 60;
            const endHour = event.end.getHours() + event.end.getMinutes() / 60;
            const duration = endHour - startHour;

            eventElement.style.top = `${(startHour - 8) * 60}px`;
            eventElement.style.height = `${duration * 60}px`;

            dayContent.appendChild(eventElement);
        });
    }

    function updateMonthAndDateRange(startOfWeek, endOfWeek) {
        currentMonthEl.textContent = startOfWeek.toLocaleDateString('es-ES', { month: 'long', year: 'numeric' });
        dateRangeEl.textContent = `${startOfWeek.getDate()} ${startOfWeek.toLocaleDateString('es-ES', { month: 'short' })} - ${endOfWeek.getDate()} ${endOfWeek.toLocaleDateString('es-ES', { month: 'short', year: 'numeric' })}`;
    }

    function getStartOfWeek(date) {
        const startOfWeek = new Date(date);
        startOfWeek.setDate(date.getDate() - date.getDay() + (date.getDay() === 0 ? -6 : 1));
        return startOfWeek;
    }

    prevWeekBtn.addEventListener('click', () => {
        currentDate.setDate(currentDate.getDate() - 7);
        renderCalendar();
    });

    nextWeekBtn.addEventListener('click', () => {
        currentDate.setDate(currentDate.getDate() + 7);
        renderCalendar();
    });

    todayBtn.addEventListener('click', () => {
        currentDate = new Date();
        renderCalendar();
    });

    viewBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            viewBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            currentView = btn.dataset.view;
            // Aquí se implementaría la lógica para cambiar la vista
            // Por ahora, solo actualizamos la vista de semana
            renderCalendar();
        });
    });

    renderCalendar();
});