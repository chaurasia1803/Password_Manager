from cryptography.fernet import Fernet
from django.conf import settings

def get_fernet():
    return Fernet(settings.SECRET_ENCRYPTION_KEY)

def encrypt_password(raw_password: str) -> str:
    return get_fernet().encrypt(raw_password.encode()).decode()

def decrypt_password(encrypted_password: str) -> str:
    return get_fernet().decrypt(encrypted_password.encode()).decode()
