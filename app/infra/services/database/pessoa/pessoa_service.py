from app.application.contracts.data.repositories.i_pessoa_repository import IPessoaRepository
from app.application.usecases.dto.input.entities.create_pessoa_input_dto import CreatePessoaInputDto
from app.domain.entities.pessoa_entity import PessoaEntity


class PessoaService:
    def __init__(self, pessoa_repository: IPessoaRepository) -> None:
        self.pessoa_repository = pessoa_repository
    
    def create(self, input_dto: CreatePessoaInputDto) -> PessoaEntity:
        pessoa_entity = PessoaEntity(**input_dto.to_dict)
        return self.pessoa_repository.add(pessoa_entity)
