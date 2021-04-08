from cryptography.fernet import Fernet


class Symmetric:

    def __init__(self):
        self._key = None

    @staticmethod
    def generate_random_key() -> str:
        return Fernet.generate_key().hex()

    def set_key(self, key: str) -> None:
        self._key = Fernet(bytearray.fromhex(key))

    def encode_message(self, msg: str) -> bytes:
        return self._key.encrypt(bytes(msg, "utf-8"))

    def decode_message(self, msg: str) -> bytes:
        return self._key.decrypt(bytes(msg, "utf-8"))
