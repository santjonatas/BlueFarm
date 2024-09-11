from app.domain.entities.usuario_entity import UsuarioEntity


class ValidateUserOutputDto:
    def __init__(self, usuario: UsuarioEntity):
        self.usuario = usuario

