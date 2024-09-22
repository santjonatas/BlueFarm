document.addEventListener('DOMContentLoaded', function() {
    const menuButton = document.querySelector('.img-menu');
    const mainElement = document.querySelector('main');
    const sidebarSection = document.querySelector('.section-sidebar'); 

    menuButton.addEventListener('click', function() {
        if (mainElement.contains(sidebarSection)) {
            mainElement.removeChild(sidebarSection);
        } else {
            mainElement.insertBefore(sidebarSection, mainElement.firstChild);
        }
    });
});

//////////////////////////////////

document.querySelectorAll('.botao-sidebar').forEach(button => {
    button.addEventListener('click', function() {
        document.querySelectorAll('.section-content').forEach(section => {
            section.style.display = 'none';
        });

        const sectionId = this.getAttribute('data-section');
        const sectionToShow = document.getElementById(sectionId);

        sectionToShow.style.display = 'grid';
    });
});

