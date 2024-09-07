import os, re
from dotenv import load_dotenv

load_dotenv()


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
