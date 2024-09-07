from requests import Session
from app.application.contracts.data.repositories.i_usuario_repository import IUsuarioRepository
from app.domain.entities.usuario_entity import UsuarioEntity


class UsuarioRepository(IUsuarioRepository):
    def __init__(self, session: Session):
        super().__init__(session, UsuarioEntity)
