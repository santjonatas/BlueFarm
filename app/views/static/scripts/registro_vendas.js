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