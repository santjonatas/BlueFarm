// Seleciona o elemento de perfil e a div a ser expandida
const imgPerfil = document.querySelector('.img-perfil');
const perfilExpandido = document.getElementById('perfil-expandido');

// Função para alternar a visibilidade da div
function togglePerfilExpandido() {
    if (perfilExpandido.style.display === 'none' || perfilExpandido.style.display === '') {
        perfilExpandido.style.display = 'flex'; // Mostra a div
    } else {
        perfilExpandido.style.display = 'none'; // Esconde a div
    }
}

// Adiciona o evento de clique para alternar a div quando clicar na imagem de perfil
imgPerfil.addEventListener('click', togglePerfilExpandido);
