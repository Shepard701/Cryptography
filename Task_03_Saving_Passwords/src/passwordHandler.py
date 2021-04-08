import hashlib
import os


class PasswordHandler:
    SALT_SIZE = 16

    @staticmethod
    def hash_password(password: str) -> tuple[bytes, str]:
        """
        Hashes given password with random salt and returns salt as a bytes and hash as a string

        :param password: password given by the user
        :return: salt as a bytes and hash as a string
        """
        salt = os.urandom(hashlib.blake2b.SALT_SIZE)
        hashed_password = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 100000)
        return salt, hashed_password.hex()

    @staticmethod
    def verify_password(password: str, salt: bytes, correct_password: str) -> bool:
        """
        Verifies given by the user password with existing in a database

        :param password: password given by the user to verify existing
        :param salt: salt from the database
        :param correct_password: correct, hashed password from the database
        :return: True if succeed and false if doesn't
        """
        hashed_password = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 100000)
        return hashed_password.hex() == correct_password
