const imgPerfil = document.querySelector('.img-perfil');
const perfilExpandido = document.getElementById('perfil-expandido');

function togglePerfilExpandido() {
    if (perfilExpandido.style.display === 'none' || perfilExpandido.style.display === '') {
        perfilExpandido.style.display = 'flex'; 
    } else {
        perfilExpandido.style.display = 'none'; 
    }
}

imgPerfil.addEventListener('click', togglePerfilExpandido);


document.addEventListener('DOMContentLoaded', function() {
    const cards = document.querySelectorAll('.bt-div-header');
    
    cards.forEach(function(card) {
        card.addEventListener('mouseover', function() {
            card.style.backgroundColor = 'rgb(219, 217, 217)'; 
            card.style.boxshadow = '';
        });
        
        card.addEventListener('mouseout', function() {
            card.style.backgroundColor = '';  
            card.style.boxshadow = ''
        });
    });
});

document.addEventListener("DOMContentLoaded", function () {
    const imgPerfil = document.querySelector(".img-perfil");

    imgPerfil.addEventListener("mouseenter", function () {
        imgPerfil.style.backgroundImage = "url('../../static/images/profile-escuro.jpg')";
    });

    imgPerfil.addEventListener("mouseleave", function () {
        imgPerfil.style.backgroundImage = "url('../../static/images/profile.jpg')";
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const cards = document.querySelectorAll('.img-menu');
    
    cards.forEach(function(card) {
        card.addEventListener('mouseover', function() {
            card.style.backgroundColor = '#b8b5db'; 
            card.style.boxshadow = '';
        });
        
        card.addEventListener('mouseout', function() {
            card.style.backgroundColor = '';  
            card.style.boxshadow = ''
        });
    });
});