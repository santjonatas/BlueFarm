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
