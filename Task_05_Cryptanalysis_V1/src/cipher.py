class Cipher:
    ALPHABET_SIZE = 26
    LOWER_A_ASCII_CODE = 97
    LOWER_Z_ASCII_CODE = 122
    UPPER_A_ASCII_CODE = 65
    UPPER_Z_ASCII_CODE = 90

    def __init__(self, key: int = 0):
        self._key = key
        pass

    @staticmethod
    def encrypt(path: str, key: int = 4) -> str:
        """
        Encrypts text in a given txt file

        :param path: path to a txt file
        :param key: integer number the cipher will use in encrypting - shouldn't be to high
        :return: encrypted text returned as string
        """
        file = open(path)
        text = file.read()
        file.close()
        text = Cipher.standardize_text(text)
        # Changes string to list with a regular chunks for future encrypting
        text = [text[i:i + key] for i in range(0, len(text), key)]
        text = Cipher.transposition_text(text)
        text = Cipher.substitute_letters(text, key)
        return text

    @staticmethod
    def standardize_text(text: str) -> str:
        """
        Standardize text to only lower case letters without other characters

        :param text: string text to standardize
        :return: standardized text as string
        """
        standardize_text = ""
        for i in range(len(text)):
            if Cipher.LOWER_A_ASCII_CODE <= ord(text[i]) <= Cipher.LOWER_Z_ASCII_CODE:
                standardize_text += text[i]
            elif Cipher.UPPER_A_ASCII_CODE <= ord(text[i]) <= Cipher.UPPER_Z_ASCII_CODE:
                standardize_text += chr(ord(text[i]) + 32)
        return standardize_text

    @staticmethod
    def transposition_text(text: list) -> str:
        """
        Transpose list to be slightly more complicated and converts list to a string

        :param text: list to transpose
        :return: transposed text as string
        """
        temp_string = ""
        for i in range(int(len(text) / 2)):
            text[i], text[len(text) - i - 2] = text[len(text) - i - 2], text[i]
        for i in text:
            temp_string += i
        return temp_string

    @staticmethod
    def substitute_letters(text: str, key: int) -> str:
        """
        Substitutes letters in a given string with a "secret" pattern

        :param text: string text to substitute
        :param key: key to encrypt with
        :return: encrypted text as a string
        """
        sub = []
        encrypted_text = ""

        # List with numbers needed in later encrypting
        for i in range(key):
            sub.append(ord(text[i]) - Cipher.LOWER_A_ASCII_CODE + key)

        # First *key-quantity* letters are encrypted with Caesar cipher, the rest of a text is encrypted
        # with a Vigenere cipher, based on the number list
        for i in range(len(text)):
            if i < key:
                encrypted_text += chr((ord(text[i]) - Cipher.LOWER_A_ASCII_CODE + key)
                                      % Cipher.ALPHABET_SIZE + Cipher.LOWER_A_ASCII_CODE)
            else:
                encrypted_text += chr((ord(text[i]) - Cipher.LOWER_A_ASCII_CODE + sub[(i + 1) % key])
                                      % Cipher.ALPHABET_SIZE + Cipher.LOWER_A_ASCII_CODE)
        return encrypted_text


if __name__ == '__main__':
    """
    Cipher.encrypt(path) - Use to encrypt text in a txt file
    """
#    print(Cipher.encrypt("path.txt", 4))
