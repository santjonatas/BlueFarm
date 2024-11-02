document.addEventListener('DOMContentLoaded', function() {
    const cards = document.querySelectorAll('.bt-cabecalho');
    
    cards.forEach(function(card) {
        card.addEventListener('mouseover', function() {
            card.style.color = '#bbb8e4'; 
        });
        
        card.addEventListener('mouseout', function() {
            card.style.color = 'white';
        });
    });
});

document.addEventListener("DOMContentLoaded", function() {
    const sobreNosButton = document.querySelector('.bt-cabecalho:nth-of-type(1)'); // Botão "Sobre Nós"
    const servicosButton = document.querySelector('.bt-cabecalho:nth-of-type(2)'); // Botão "Serviços"
    const produtosButton = document.querySelector('.bt-cabecalho:nth-of-type(3)'); // Botão "Produtos"

    sobreNosButton.addEventListener('click', function(event) {
        event.preventDefault();
        const targetSection = document.getElementById('sobre-nos');
        targetSection.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
        });
    });

    servicosButton.addEventListener('click', function(event) {
        event.preventDefault();
        const targetSection = document.getElementById('servicos');
        targetSection.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
        });
    });

    produtosButton.addEventListener('click', function(event) {
        event.preventDefault();
        const targetSection = document.getElementById('produtos');
        targetSection.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
        });
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const cards = document.querySelectorAll('.bt-login');
    
    cards.forEach(function(card) {
        card.addEventListener('mouseover', function() {
            card.style.color = '#bbb8e4'; 
        });
        
        card.addEventListener('mouseout', function() {
            card.style.color = 'white';
        });
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const cards = document.querySelectorAll('.form-control');
    
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
    const cards = document.querySelectorAll('.bt-registro');
    
    cards.forEach(function(card) {
        card.addEventListener('mouseover', function() {
            card.style.background = 'linear-gradient(to right bottom, #0f1413, #1d1e20, #363f2f)'; 
            card.style.boxshadow = '';
        });
        
        card.addEventListener('mouseout', function() {
            card.style.background = 'linear-gradient(to right bottom, #151C1A, #27282C, #47533E)';  
            card.style.boxshadow = '';
        });
    });
});