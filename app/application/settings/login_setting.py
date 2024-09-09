from flask import Flask, flash, redirect, url_for
from app.application.settings.extensions_setting import lm
from app.domain.entities.usuario_entity import UsuarioEntity


class LoginSetting:
    def __init__(self, app: Flask) -> None:
        lm.init_app(app=app)

        lm.login_view = 'login.login'

        @lm.unauthorized_handler
        def unauthorized():
            flash("Por favor, faça login para acessar esta página.", "warning")
            return redirect(url_for(lm.login_view))

        @lm.user_loader
        def load_user(user_id):
            return UsuarioEntity.query.get(user_id)
