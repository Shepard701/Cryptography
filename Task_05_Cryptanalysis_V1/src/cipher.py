import logging


class Cipher:
    ALPHABET_SIZE = 26
    LOWER_A_ASCII_CODE = 97
    LOWER_Z_ASCII_CODE = 122
    UPPER_A_ASCII_CODE = 65
    UPPER_Z_ASCII_CODE = 90

    logger = logging.getLogger("hashing")
    logging.basicConfig(level=logging.DEBUG)

    def __init__(self, key: int = 0):
        self._key = key
        pass

    @staticmethod
    def encrypt(path: str, key: int = 4) -> str:
        file = open(path)
        text = file.read()
        file.close()
        text = Cipher.standardize_text(text)
        text = [text[i:i + key] for i in range(0, len(text), key)]
        text = Cipher.transposition_text(text)
        text = Cipher.substitute_letters(text, key)
        return text

    @staticmethod
    def standardize_text(text: str) -> str:
        standardize_text = ""
        for i in range(len(text)):
            if Cipher.LOWER_A_ASCII_CODE <= ord(text[i]) <= Cipher.LOWER_Z_ASCII_CODE:
                standardize_text += text[i]
            elif Cipher.UPPER_A_ASCII_CODE <= ord(text[i]) <= Cipher.UPPER_Z_ASCII_CODE:
                standardize_text += chr(ord(text[i]) + 32)
        return standardize_text

    @staticmethod
    def transposition_text(text: list) -> str:
        temp_string = ""
        for i in range(int(len(text) / 2)):
            text[i], text[len(text) - i - 2] = text[len(text) - i - 2], text[i]
        for i in text:
            temp_string += i
        return temp_string

    @staticmethod
    def substitute_letters(text: str, key: int) -> str:
        sub = []
        encrypted_text = ""

        for i in range(key):
            sub.append(ord(text[i]) - Cipher.LOWER_A_ASCII_CODE + key)
        for i in range(len(text)):
            if i < 4:
                encrypted_text += chr((ord(text[i]) - Cipher.LOWER_A_ASCII_CODE + key)
                                      % Cipher.ALPHABET_SIZE + Cipher.LOWER_A_ASCII_CODE)
            else:
                encrypted_text += chr((ord(text[i]) - Cipher.LOWER_A_ASCII_CODE + sub[(i + 1) % 4])
                                      % Cipher.ALPHABET_SIZE + Cipher.LOWER_A_ASCII_CODE)
        return encrypted_text

# if __name__ == '__main__':
#    path = "sample_text.txt"
#    encrypted_text = Cipher.encrypt(path)
#    print(encrypted_text)
