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
    const cards = document.querySelectorAll('.card-produto');
    
    cards.forEach(function(card) {
        card.addEventListener('mouseover', function() {
            card.style.backgroundColor = '#ffffff21'; 
            card.style.boxshadow = '0px 0px 15px green';
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
            botao.style.boxshadow = '0px 0px 15px green';
        });
        
        botao.addEventListener('mouseout', function() {
            botao.style.backgroundColor = '';  
            botao.style.boxshadow = ''
        });
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const botao_fazer_pedido = document.querySelector('.form-bt-fazer-pedido');
    
    botao_fazer_pedido.addEventListener('mouseover', function() {
        botao_fazer_pedido.style.backgroundColor = '#b3b0da'; 
        botao_fazer_pedido.style.boxShadow = '0px 0px 10px green';  
        botao_fazer_pedido.style.borderRadius = '5px';   
    });
    
    botao_fazer_pedido.addEventListener('mouseout', function() {
        botao_fazer_pedido.style.backgroundColor = '';  
        botao_fazer_pedido.style.boxShadow = '';  
        botao_fazer_pedido.style.borderRadius = ''; 
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const botoes_item_carrinho = document.querySelectorAll('.card-produto-carrinho');
    
    botoes_item_carrinho.forEach(function(botao_item_carrinho) {
        botao_item_carrinho.addEventListener('mouseover', function() {
            botao_item_carrinho.style.backgroundColor = '#ffffff21'; 
            botao_item_carrinho.style.boxshadow = '0px 0px 15px green';
        });
        
        botao_item_carrinho.addEventListener('mouseout', function() {
            botao_item_carrinho.style.backgroundColor = '';  
            botao_item_carrinho.style.boxshadow = ''
        });
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const botoes_card_produto = document.querySelectorAll('.add-to-cart');
    
    botoes_card_produto.forEach(function(botao_card_produto) {
        botao_card_produto.addEventListener('mouseover', function() {
            botao_card_produto.style.backgroundColor = 'rgb(179, 179, 179)'; 
            botao_card_produto.style.boxshadow = '0px 0px 15px green';
        });
        
        botao_card_produto.addEventListener('mouseout', function() {
            botao_card_produto.style.backgroundColor = '';  
            botao_card_produto.style.boxshadow = ''
        });
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const itens_carrinho = document.querySelectorAll('.bt-item-carrinho');
    
    itens_carrinho.forEach(function(item_carrinho) {
        item_carrinho.addEventListener('mouseover', function() {
            item_carrinho.style.backgroundColor = 'rgb(179, 179, 179)'; 
            item_carrinho.style.boxshadow = '0px 0px 15px green';
        });
        
        item_carrinho.addEventListener('mouseout', function() {
            item_carrinho.style.backgroundColor = '';  
            item_carrinho.style.boxshadow = ''
        });
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const botoes_pagar_pedido = document.querySelectorAll('.bt-pagar-pedido');
    
    botoes_pagar_pedido.forEach(function(botao_pagar_pedido) {
        botao_pagar_pedido.addEventListener('mouseover', function() {
            botao_pagar_pedido.style.backgroundColor = 'rgb(0, 94, 0)'; 
            botao_pagar_pedido.style.boxshadow = '0px 0px 10px green';
        });
        
        botao_pagar_pedido.addEventListener('mouseout', function() {
            botao_pagar_pedido.style.backgroundColor = '';  
            botao_pagar_pedido.style.boxshadow = ''
        });
    });
});