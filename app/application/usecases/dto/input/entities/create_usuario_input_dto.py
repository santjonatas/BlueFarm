class CreateUsuarioInputDto:
    def __init__(self, username: str=None, senha: str=None, id_pessoa: str=None) -> None:
        self.id_pessoa = id_pessoa
        self.username = username
        self.senha = senha

    @property
    def to_dict(self) -> dict:
        return {
            'id_pessoa': self.id_pessoa if self.id_pessoa is not None else '',
            'username': self.username if self.username is not None else '',
            'senha': self.senha if self.senha is not None else ''
        }
