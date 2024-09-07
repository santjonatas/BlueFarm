class CreateUsuarioInputDto:
    def __init__(self, username: str=None, senha: str=None, id_funcionario: str=None) -> None:
        self.id_funcionario = id_funcionario
        self.username = username
        self.senha = senha

    @property
    def to_dict(self) -> dict:
        return {
            'id_funcionario': self.id_funcionario if self.id_funcionario is not None else '',
            'username': self.username if self.username is not None else '',
            'senha': self.senha if self.senha is not None else ''
        }
