import traceback
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

    def atualizar_senha_usuario(self, id_pessoa: int, nova_senha: str = None) -> bool:
        try:
            # Busca o usuário pelo ID
            usuario = self.session.query(UsuarioEntity).filter_by(id_pessoa=id_pessoa).first()

            if not usuario:
                return False  # Se o usuário não for encontrado, retorna falso

            # Atualiza a senha se não for None
            if nova_senha is not None and nova_senha != '':
                usuario.senha = nova_senha

            # Faz o commit das alterações no banco
            self.session.commit()
            return True
        except Exception as e:
            stacktrace = traceback.format_exc()
            pass