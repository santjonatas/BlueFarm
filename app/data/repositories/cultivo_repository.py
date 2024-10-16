from requests import Session
from app.application.contracts.data.repositories.i_cultivo_repository import ICultivoRepository
from app.domain.entities.cultivo_entity import CultivoEntity


class CultivoRepository(ICultivoRepository):
    def __init__(self, session: Session):
        super().__init__(session, CultivoEntity)

    def atualizar_data_fim(self, cultivo_id: int, nova_data_fim) -> None:
        cultivo = self.session.query(CultivoEntity).filter_by(id=cultivo_id).first()
        if cultivo:
            cultivo.data_fim = nova_data_fim
            self.session.commit()
        else:
            raise ValueError(f'Cultivo com id {cultivo_id} não encontrado.')

    def atualizar_status_colhido(self, cultivo_id: int) -> None:
        cultivo = self.session.query(CultivoEntity).filter_by(id=cultivo_id).first()

        if cultivo:
            cultivo.status = 'Colhido'  
            self.session.commit() 
        else:
            print(f'Cultivo com ID {cultivo_id} não encontrado.')