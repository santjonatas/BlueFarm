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
