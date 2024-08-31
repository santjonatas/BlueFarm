import os, re
from dotenv import load_dotenv

from app.infra.services.ForDevs.for_devs import ForDevsService


load_dotenv()

for_devs = ForDevsService()


class RegexValidatorUtil:
    def __init__(self) -> None:
        self.email_regex = os.getenv('EMAIL_REGEX')
        self.password_regex = os.getenv('PASSWORD_REGEX')

    def verificar_email(self, email: str) -> bool:
        if self.email_regex:
            return bool(re.match(self.email_regex, email))
        raise ValueError("EMAIL_REGEX não foi definido nas variáveis de ambiente.")

    def verificar_senha(self, senha: str) -> bool:
        if self.password_regex:
            return bool(re.match(self.password_regex, senha))
        raise ValueError("PASSWORD_REGEX não foi definido nas variáveis de ambiente.")
    
    def validar_cpf(self, cpf):

        res = for_devs.validar_cpf(cpf)

        texto_lower = res.lower()

        if 'verdadeiro' in texto_lower:
            return True
        if 'falso' in texto_lower:
            return False
