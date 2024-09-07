from requests import Session
from app.application.contracts.data.repositories.i_usuario_repository import IUsuarioRepository
from app.domain.entities.usuario_entity import UsuarioEntity


class UsuarioRepository(IUsuarioRepository):
    def __init__(self, session: Session):
        super().__init__(session, UsuarioEntity)

    def get_by_username(self, username: str) -> UsuarioEntity:
        return self.session.query(self.entity).filter(self.entity.username==username).first()

    def username_exists(self, username: str) -> bool:
        return self.get_by_username(username=username) is not None
