import os
from dotenv import load_dotenv
from cryptography.fernet import Fernet

load_dotenv()


class CryptoUtil:
    def __init__(self):
        key = os.getenv("CRYPTO_KEY")
        self.cipher = Fernet(key)

    def encrypt(self, value: str) -> str:
        return self.cipher.encrypt(value.encode()).decode()

    def decrypt(self, encrypted_value: str) -> str:
        return self.cipher.decrypt(encrypted_value.encode()).decode()
