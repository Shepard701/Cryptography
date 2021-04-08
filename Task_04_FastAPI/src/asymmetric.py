import base64

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import (
    padding, rsa
)


class Asymmetric:

    def __init__(self):
        self._privateKey = None
        self._publicKey = None

    def get_keys_hex(self) -> list:
        """
        Returns private and public keys stored in the class

        :return: list which contains private and public keys in HEX format
        """
        private_pem = self._privateKey.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        )
        public_pem = self._privateKey.public_key().public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        return [private_pem.hex(), public_pem.hex()]

    def get_keys_hex_ssh(self) -> list:
        """
        Returns private and public keys stored in the class with SSH encoding

        :return: list which contains private and public keys in HEX format and SSH encoding
        """
        private_ssh = self._privateKey.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.OpenSSH,
            encryption_algorithm=serialization.NoEncryption()
        )
        public_ssh = self._privateKey.public_key().public_bytes(
            encoding=serialization.Encoding.OpenSSH,
            format=serialization.PublicFormat.OpenSSH
        )
        return [private_ssh.hex(), public_ssh.hex()]

    def set_keys(self, private_key, public_key) -> None:
        """
        Set given keys as new ones in the class

        :param private_key: Private Key in HEX format
        :param public_key: Public Key in HEX format
        :return: None
        """
        self._privateKey = serialization.load_pem_private_key(
            bytearray.fromhex(private_key),
            password=None,
        )
        self._publicKey = serialization.load_pem_public_key(bytearray.fromhex(public_key))

    def generate_keys(self) -> None:
        """
        Generate random private and public keys and saves them in the class

        :return: None
        """
        self._privateKey = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
        )
        self._publicKey = self._privateKey.public_key()

    def sign_message(self, msg: str) -> bytes:
        """
        Signs given message with private key stored in the class

        :param msg: String message to sign
        :return: Signed message as bytes
        """
        return base64.b64encode(self._privateKey.sign(
                bytes(msg, "utf-8"),
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
        )

    def verify_message(self, msg: str, signature: str) -> bool:
        """
        Verifies if given message equals signature by the public key stored in class

        :param msg: String Message to verify
        :param signature: Signed message to compare with
        :return: Boolean value depending of correct verification
        """
        decoded_sign = base64.b64decode(signature)
        try:
            self._publicKey.verify(
                decoded_sign,
                bytes(msg, "utf-8"),
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return True
        except InvalidSignature:
            return False

    def encode_message(self, msg: str) -> bytes:
        """
        Encode given message with public key stored in the class

        :param msg: String message to encode
        :return: Encoded message as bytes
        """
        return base64.b64encode(self._publicKey.encrypt(
                bytes(msg, "utf-8"),
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
        )

    def decode_message(self, msg: str) -> str:
        """
        Decode given message with private key stored in the class

        :param msg: String message to decode
        :return: Decoded message
        """
        decoded_msg = base64.b64decode(msg)
        return self._privateKey.decrypt(
            decoded_msg,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
