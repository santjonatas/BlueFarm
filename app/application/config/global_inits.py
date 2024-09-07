from flask import Flask
from app.application.settings.env_setting import EnvSetting
from app.application.settings.extensions_setting import ExtensionsSettings
from app.application.settings.globals_setting import GlobalsSetting
from app.application.settings.login_setting import LoginSetting
from app.application.settings.routes_setting import RoutesSetting


class GlobalInits:
    def __init__(self, app: Flask) -> None:
        EnvSetting(app=app)
        ExtensionsSettings(app=app)
        GlobalsSetting(app=app)
        RoutesSetting(app=app)
        LoginSetting(app=app)
    