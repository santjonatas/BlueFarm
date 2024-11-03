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
    const cards = document.querySelectorAll('.bt-login');
    
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