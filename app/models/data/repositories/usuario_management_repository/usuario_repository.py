from app.application.contracts.i_usuario_repository import IUsuarioRepository
from app.models.entities.usuario_management.usuario_entity import UsuarioEntity


class UsuarioRepository(IUsuarioRepository):
    def __init__(self, session):
        super().__init__(session, UsuarioEntity)

    def obter_username(self, username: str) -> UsuarioEntity:
        return self.session.query(self.entity).filter(self.entity.username==username).first()

    def username_existe(self, username: str) -> bool:
        return self.obter_username(username=username) is not None
