from app.domain.entities.pessoa_entity import PessoaEntity


class UpdatePerfilUserOutputDto:
    def __init__(self, perfil_entity: PessoaEntity) -> None:
        self.perfil_entity = perfil_entity
