from cryptography.fernet import Fernet


class Symmetric:

    def __init__(self):
        self._key = None

    @staticmethod
    def generate_random_key() -> bytes:
        return Fernet.generate_key()

    def set_key(self, key: bytes) -> None:
        self._key = Fernet(key)

    def encode_message(self, msg: str) -> bytes:
        return self._key.encrypt(bytes(msg, "utf-8"))

    def decode_message(self, msg: str) -> bytes:
        return self._key.decrypt(bytes(msg, "utf-8"))
