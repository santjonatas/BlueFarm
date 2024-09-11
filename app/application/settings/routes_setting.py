from flask import Flask


class RoutesSetting:
    def __init__(self, app: Flask) -> None:
        app.register_blueprint(app.global_controllers.login_controller.blueprint)
        app.register_blueprint(app.global_controllers.register_controller.blueprint)
        app.register_blueprint(app.global_controllers.home_controller.blueprint)
