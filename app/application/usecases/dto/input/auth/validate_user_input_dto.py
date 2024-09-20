class ValidateUserInputDto:
    def __init__(self, username: str=None, senha: str=None):
        self.username = username
        self.senha = senha

    @property
    def to_dict(self):
        return {
            'username': self.username if self.username is not None else '',
            'senha': self.senha if self.senha is not None else ''
        }
