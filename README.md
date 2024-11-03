# BlueFarm 🌱

**BlueFarm** é uma aplicação web desenvolvida como parte do **PIM - Projeto Integrado Multidisciplinar** do 4º semestre da faculdade UNIP. A aplicação é voltada para o gerenciamento de uma fazenda urbana, conectando clientes e funcionários em uma plataforma prática e intuitiva.

## Descrição 📋

O BlueFarm visa simplificar a gestão e a comercialização de produtos frescos da fazenda urbana. A aplicação permite que clientes façam compras diretamente, enquanto os funcionários gerenciam diferentes aspectos operacionais da fazenda, de acordo com seus níveis de permissão.

## Funcionalidades 🛠️

### Para Clientes:
- **Catálogo de Produtos:** Visualização de produtos disponíveis com informações detalhadas.
- **Carrinho de Compras:** Adição e visualização de itens no carrinho.
- **Finalização de Compra:** Processo simples de checkout para finalizar a compra.

### Para Funcionários:
- **Tipos de Usuários:**
  - **Operadores:** Acesso a funcionalidades de gerenciamento da fazenda, como controle de inventário, atualização de informações de produtos, e monitoramento de pedidos.
  - **Administradores:** Possuem todas as permissões dos operadores, com algumas funções adicionais de administração e gerenciamento avançado.

## Tecnologias Utilizadas 🖥️

- **Backend:** Python (Flask) para gerenciar o servidor e as requisições.
- **Frontend:** HTML, CSS e JavaScript para a interface do usuário.
- **Banco de Dados:** Microsoft SQLServer
  
## Como Executar 🚀

1. Clone o repositório:
   ```bash
   git clone https://github.com/santjonatas/BlueFarm.git
   ```
2. Acesse o diretório do projeto:
   ```bash
   cd BlueFarm
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Execute o servidor:
   ```bash
   flask run
   ```

A aplicação estará disponível em `http://127.0.0.1:5000`.

## Estrutura de Usuários 👥

- **Clientes:** Utilizam a plataforma para visualizar e comprar produtos.
- **Funcionários:**
  - **Operadores:** Focados no gerenciamento das operações cotidianas da fazenda.
  - **Administradores:** Têm acesso completo, incluindo permissões avançadas de administração.

## Contribuição 🤝

Contribuições são bem-vindas! Sinta-se à vontade para fazer *fork* do repositório, abrir *issues*, e enviar *pull requests*.

## Licença 📄

Este projeto é distribuído sob a licença MIT. Para mais detalhes, consulte o arquivo [LICENSE](LICENSE).
