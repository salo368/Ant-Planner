function toggleButton(selected) {
    const personalBtn = document.getElementById('personalBtn');
    const grupalBtn = document.getElementById('grupalBtn');

    if (selected === 'personal') {
        personalBtn.classList.add('active');
        grupalBtn.classList.remove('active');
    } else {
        grupalBtn.classList.add('active');
        personalBtn.classList.remove('active');
    }
}