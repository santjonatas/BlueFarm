from app.models.data.repositories.common.base_repository import BaseRepository
from app.models.entities.usuario_management.pessoa_entity import PessoaEntity


class IPessoaRepository(BaseRepository[PessoaEntity]):
    def telefone_existe(self, telefone: str) -> bool:
        ...
