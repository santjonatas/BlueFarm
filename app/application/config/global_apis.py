from app.api.v1.endpoints.auth.auth_endpoint import AuthEndpoint


class GlobalApis:
    def __init__(self) -> None:
        self.auth_endpoint = AuthEndpoint()
