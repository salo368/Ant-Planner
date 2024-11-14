const dias = document.querySelectorAll('.widget-calendar-day');
const hoy = new Date();
const mes = hoy.getMonth(); // mes actual (0 = enero, 1 = febrero, ...)
const año = hoy.getFullYear(); // año actual


// Primer día del mes actual (ej. si es martes, valor será 2)
const primerDiaMes = new Date(año, mes, 1).getDay();

// Último día del mes actual (número total de días en el mes)
const ultimoDiaMes = new Date(año, mes + 1, 0).getDate();

dias.forEach((dia, index) => {
    dia.innerText = ""; // Reiniciar todos los días en blanco
});

for (let i = 1; i <= ultimoDiaMes; i++) {
    const posicion = primerDiaMes + i - 1; // Posición en la cuadrícula
    dias[posicion].innerText = i;
}
