from app.domain.entities.administrador_entity import AdministradorEntity


class CreateAdminUserOutputDto:
    def __init__(self, admin_entity: AdministradorEntity) -> None:
        self.admin_entity = admin_entity
