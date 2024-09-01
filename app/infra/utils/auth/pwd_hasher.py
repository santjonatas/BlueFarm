from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError


class PwdHasherUtil:
    def __init__(self,
        time_cost: int=2,
        memory_cost: int=102400,
        parallelism: int=8,
        hash_len: int=16,
        salt_len: int=16):
        """
        Inicializa a classe PasswordHasher com as configurações do Argon2.
        - time_cost: número de iterações de hashing.
        - memory_cost: quantidade de memória usada (em KiB).
        - parallelism: quantas threads para processamento paralelo.
        - hash_len: comprimento do hash gerado.
        - salt_len: comprimento do salt gerado automaticamente.
        """
        self.ph = PasswordHasher(
            time_cost=time_cost, 
            memory_cost=memory_cost, 
            parallelism=parallelism, 
            hash_len=hash_len, 
            salt_len=salt_len
        )

    def hash_password(self, password: str) -> str:
        return self.ph.hash(password)

    def verify_password(self, hashed_password: str, password: str) -> bool:
        try:
            return self.ph.verify(hashed_password, password)
        except VerifyMismatchError:
            return False
