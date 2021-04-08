from cryptography.fernet import Fernet


class Symmetric:

    def __init__(self):
        self._key = None

    @staticmethod
    def generate_random_key() -> str:
        """
        Generate random key

        :return: Key as str in HEX format
        """
        return Fernet.generate_key().hex()

    def set_key(self, key: str) -> None:
        """
        Sets given key as new one in the class

        :param key: Key as str in HEX
        :return: None
        """
        self._key = Fernet(bytearray.fromhex(key))

    def encode_message(self, msg: str) -> bytes:
        """
        Encode given message with key stored in the class

        :param msg: String message to encode
        :return: Encoded message as bytes
        """
        return self._key.encrypt(bytes(msg, "utf-8"))

    def decode_message(self, msg: str) -> bytes:
        """
        Decode given message with key stored in the class

        :param msg: String message to decode
        :return: Decoded message as bytes
        """
        return self._key.decrypt(bytes(msg, "utf-8"))
