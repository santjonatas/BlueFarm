from requests import Session
from app.application.contracts.data.repositories.i_estoque_repository import IEstoqueRepository
from app.domain.entities.estoque_entity import EstoqueEntity
from sqlalchemy.orm.exc import NoResultFound
from datetime import datetime


class EstoqueRepository(IEstoqueRepository):
    def __init__(self, session: Session):
        super().__init__(session, EstoqueEntity)

    def decrementar_estoque(self, id_produto: int, quantidade: int):
        try:
            estoque = self.session.query(EstoqueEntity).filter_by(id_produto=id_produto).one()
            
            if estoque.quantidade_disponivel < quantidade:
                raise ValueError("Quantidade insuficiente no estoque.")
            
            if estoque.quantidade_disponivel >= quantidade:
                estoque.quantidade_disponivel -= quantidade
                
                estoque.ultima_atualizacao = datetime.now()

                self.session.commit()
        
        except NoResultFound:
            raise ValueError(f"Produto com id {id_produto} não encontrado no estoque.")

    def get_quantidade_por_produto(self, id_produto: int):
        resultado = self.session.query(EstoqueEntity.quantidade_disponivel)\
            .filter_by(id_produto=id_produto)\
            .first() 
        return resultado[0] if resultado else None
    
    def alterar_quantidade(self, produto_id: int, nova_quantidade: int) -> None:
        estoque = self.session.query(EstoqueEntity).filter_by(id_produto=produto_id).first()

        if estoque:
            estoque.quantidade_disponivel = nova_quantidade
            estoque.ultima_atualizacao = datetime.now()  

            self.session.commit()
        else:
            raise ValueError(f"Produto com ID {produto_id} não encontrado no estoque.")
        

    def incrementar_estoque(self, id_produto: int, quantidade: int):
        try:
            estoque = self.session.query(EstoqueEntity).filter_by(id_produto=id_produto).one()
            
            # Incrementa a quantidade disponível com a nova quantidade
            estoque.quantidade_disponivel += quantidade
            
            # Atualiza a data da última modificação
            estoque.ultima_atualizacao = datetime.now()

            # Confirma a transação
            self.session.commit()
        
        except NoResultFound:
            raise ValueError(f"Produto com id {id_produto} não encontrado no estoque.")