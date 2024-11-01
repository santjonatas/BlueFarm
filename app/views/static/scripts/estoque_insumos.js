document.addEventListener('DOMContentLoaded', function() {
    const cards = document.querySelectorAll('.card-insumo');
    
    cards.forEach(function(card) {
        card.addEventListener('mouseover', function() {
            card.style.backgroundColor = '#734aec'; 
            card.style.boxshadow = '0px 0px 15px #734aec';
        });
        
        card.addEventListener('mouseout', function() {
            card.style.backgroundColor = '';  
            card.style.boxshadow = ''
        });
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const cards = document.querySelectorAll('.bt-editar-insumo');
    
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