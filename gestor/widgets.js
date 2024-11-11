
function initializeDropdowns(ids) {
    ids.forEach(id => {
        const dropdown = document.querySelector(`#${id}`);
        const dropdownHeader = dropdown.querySelector('.dropdown-header');
        const dropdownBody = dropdown.querySelector('.dropdown-body');
        const dropdownElements = dropdown.querySelectorAll('.dropdown-element');
        
        dropdownHeader.addEventListener('click', function(event) {
            ids.forEach(otherId => {
                if (otherId !== id) {
                    const otherDropdown = document.querySelector(`#${otherId}`);
                    const otherDropdownBody = otherDropdown.querySelector('.dropdown-body');
                    otherDropdownBody.style.display = 'none';
                }
            });
            
            if (dropdownBody.style.display === 'none' || dropdownBody.style.display === '') {
                dropdownBody.style.display = 'block';
            } else {
                dropdownBody.style.display = 'none';
            }

            event.stopPropagation();
        });

        document.addEventListener('click', function(event) {
            if (!dropdown.contains(event.target)) {
                dropdownBody.style.display = 'none';
            }
        });

        dropdownElements.forEach(element => {
            element.addEventListener('click', function() {
                dropdownBody.style.display = 'none';
            });
        });
    });
}

initializeDropdowns(['info-category-dropdown', 'info-state-dropdown', 'info-type-dropdown']);

