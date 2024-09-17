from flask import Flask
from app.application.config.global_apis import GlobalApis
from app.application.config.global_controllers import GlobalControllers
from app.application.config.global_repositories import GlobalRepositories
from app.application.config.global_services import GlobalServices
from app.application.config.global_usecases import GlobalUseCases
from app.application.config.global_utils import GlobalUtils


class GlobalsSetting:
    def __init__(self, app: Flask) -> None:
        app.global_repositories = GlobalRepositories()
        app.global_services = GlobalServices(global_repositories=app.global_repositories)
        app.global_utils = GlobalUtils()
        app.global_usecases = GlobalUseCases(
            global_services=app.global_services,
            global_utils=app.global_utils
        )
        app.global_controllers = GlobalControllers()
        app.global_apis = GlobalApis()
