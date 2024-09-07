import os
from dotenv import load_dotenv
from cryptography.fernet import Fernet

load_dotenv()


class CryptoUtil:
    def __init__(self, key: str = None):
        key = os.getenv("CRYPTO_KEY")
        self.cipher = Fernet(key)

    def encrypt(self, message: str) -> str:
        return self.cipher.encrypt(message.encode()).decode()

    def decrypt(self, encrypted_message: str) -> str:
        return self.cipher.decrypt(encrypted_message.encode()).decode()
