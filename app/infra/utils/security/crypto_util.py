import os
from dotenv import load_dotenv
from cryptography.fernet import Fernet

load_dotenv()


class CryptoUtil:
    @staticmethod
    def encrypt(value: str) -> str:
        key = os.getenv("CRYPTO_KEY")
        cipher = Fernet(key)
        return cipher.encrypt(value.encode()).decode()

    @staticmethod
    def decrypt(encrypted_value: str) -> str:
        key = os.getenv("CRYPTO_KEY")
        cipher = Fernet(key)
        return cipher.decrypt(encrypted_value.encode()).decode()
