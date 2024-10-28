const dias = document.querySelectorAll('.widget-calendar-day');
dias.forEach((dia, index) => {
    dia.innerText = index + 1;
});
