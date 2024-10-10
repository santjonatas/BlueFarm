from requests import Session
from app.application.contracts.data.repositories.i_insumo_repository import IInsumoRepository
from app.domain.entities.insumo_entity import InsumoEntity


class InsumoRepository(IInsumoRepository):
    def __init__(self, session: Session):
        super().__init__(session, InsumoEntity)

    def atualizar_quantidade(self, insumo_id: int, nova_quantidade: int):
        # Busca o insumo com o id fornecido
        insumo = self.session.query(InsumoEntity).filter_by(id=insumo_id).first()
        
        if insumo:
            # Atualiza a quantidade
            insumo.quantidade = nova_quantidade
            
            # Comita a transação no banco
            self.session.commit()
            return True
        return False

