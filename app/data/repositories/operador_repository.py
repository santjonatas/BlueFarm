from requests import Session
from app.application.contracts.data.repositories.i_operador_repository import IOperadorRepository
from app.domain.entities.operador_entity import OperadorEntity


class OperadorRepository(IOperadorRepository):
    def __init__(self, session: Session):
        super().__init__(session, OperadorEntity)

    def deletar_operador_por_id_funcionario(self, id_funcionario: int) -> None:
        operador = self.session.query(OperadorEntity).filter_by(id_funcionario=id_funcionario).first()
        if operador:
            self.session.delete(operador)
            self.session.commit()
