
document.querySelectorAll('.main-category-settings-button-swap').forEach(button => {
    button.addEventListener('click', () => {
        const mainCategory = button.closest('.main-category');
        const body = mainCategory.querySelector('.main-category-body');

        const [imgUp, imgDown] = button.querySelectorAll('img');

        if (button.getAttribute('data-state') === 'up') {
            imgUp.style.display = 'none';
            imgDown.style.display = 'block';
            body.style.display = 'block'; 
            button.setAttribute('data-state', 'down');
        } else {
            imgUp.style.display = 'block';
            imgDown.style.display = 'none';
            body.style.display = 'none'; 
            button.setAttribute('data-state', 'up');
        }
    });
});

document.querySelectorAll('.main-category-header').forEach(header => {
    header.addEventListener('click', () => {
        const mainCategory = header.closest('.main-category');
        const body = mainCategory.querySelector('.main-category-body');

        const [imgUp, imgDown] = header.querySelectorAll('img');

        if (header.getAttribute('data-state') === 'up') {
            imgUp.style.display = 'none';
            imgDown.style.display = 'block';
            body.style.display = 'block'; 
            header.setAttribute('data-state', 'down');
        } else {
            imgUp.style.display = 'block';
            imgDown.style.display = 'none';
            body.style.display = 'none'; 
            header.setAttribute('data-state', 'up');
        }
    });
});

