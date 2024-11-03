from requests import Session
from app.application.contracts.data.repositories.i_administrador_repository import IAdministradorRepository
from app.domain.entities.administrador_entity import AdministradorEntity


class AdministradorRepository(IAdministradorRepository):
    def __init__(self, session: Session):
        super().__init__(session, AdministradorEntity)

    def deletar_administrador_por_id_funcionario(self, id_funcionario: int) -> None:
        administrador = self.session.query(AdministradorEntity).filter_by(id_funcionario=id_funcionario).first()
        if administrador:
            self.session.delete(administrador)
            self.session.commit()
