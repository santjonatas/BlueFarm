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

document.addEventListener('DOMContentLoaded', function() {
    const cards = document.querySelectorAll('.card-modulo');
    
    cards.forEach(function(card) {
        card.addEventListener('mouseover', function() {
            card.style.backgroundColor = '#bbb8e4'; 
            card.style.boxshadow = '0px 0px 15px #7D52FF';
        });
        
        card.addEventListener('mouseout', function() {
            card.style.backgroundColor = '';  
            card.style.boxshadow = ''
        });
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const botoes_sidebar = document.querySelectorAll('.botao-sidebar');
    
    botoes_sidebar.forEach(function(botao) {
        botao.addEventListener('mouseover', function() {
            botao.style.backgroundColor = '#ffffff21'; 
            botao.style.boxshadow = '0px 0px 15px #7D52FF';
        });
        
        botao.addEventListener('mouseout', function() {
            botao.style.backgroundColor = '';  
            botao.style.boxshadow = ''
        });
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const botoes_sidebar = document.querySelectorAll('.card-acessar');
    
    botoes_sidebar.forEach(function(botao) {
        botao.addEventListener('mouseover', function() {
            botao.style.backgroundColor = '#bbb8e4'; 
            botao.style.boxshadow = '0px 0px 15px #7D52FF';
        });
        
        botao.addEventListener('mouseout', function() {
            botao.style.backgroundColor = '';  
            botao.style.boxshadow = ''
        });
    });
});