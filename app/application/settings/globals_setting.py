from flask import Flask
from app.application.config.global_repositories import GlobalRepositories
from app.application.config.global_services import GlobalServices


class GlobalsSetting:
    def __init__(self, app: Flask) -> None:
        app.global_repositories = GlobalRepositories()
        app.global_services = GlobalServices(global_repositories=app.global_repositories)
        