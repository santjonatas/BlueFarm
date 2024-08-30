

class RegistrarOperadorUseCase:
    def __init__(self, 
                 nome, 
                 data_nascimento, 
                 cpf, 
                 genero, 
                 telefone, 
                 email, 
                 endereco, 
                 data_admissao, 
                 cargo, 
                 salario,
                 data_demissao, 
                 username, 
                 senha,
                 permissao, 
                 area_operacao, 
                 supervisor_direto
                 ) -> None:
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.genero = genero
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
        self.data_admissao = data_admissao
        self.cargo = cargo
        self.salario = salario
        self.data_demissao = data_demissao
        self.username = username
        self.senha = senha
        self.permissao = permissao
        self.area_operacao = area_operacao
        self.supervisor_direto = supervisor_direto
        pass

    def execute():
        pass