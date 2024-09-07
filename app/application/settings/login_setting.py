from flask import Flask
from app.application.settings.extensions_setting import lm
from app.domain.entities.usuario_entity import UsuarioEntity


class LoginSetting:
    def __init__(self, app: Flask) -> None:
        lm.init_app(app=app)

        lm.login_view = 'auth.login'

        @lm.user_loader
        def load_user(user_id):
            return UsuarioEntity.query.get(user_id)
