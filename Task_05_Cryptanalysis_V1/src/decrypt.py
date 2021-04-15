class Decrypt:
    ALPHABET_SIZE = 26
    LOWER_A_ASCII_CODE = 97
    LOWER_Z_ASCII_CODE = 122

    def __init__(self, key: int = 0):
        self._key = key
        pass

    @staticmethod
    def decrypt_text(path: str, key: int) -> str:
        sub = []
        decrypted_text = ""
        result = ""

        file = open(path)
        text = file.read()
        file.close()

        for i in range(len(text)):
            if i < 4:
                decrypted_text += chr((ord(text[i]) - Decrypt.LOWER_A_ASCII_CODE - key + Decrypt.ALPHABET_SIZE)
                                      % Decrypt.ALPHABET_SIZE + Decrypt.LOWER_A_ASCII_CODE)
                sub.append(ord(text[i]) - Decrypt.LOWER_A_ASCII_CODE)
            else:
                decrypted_text += chr((ord(text[i]) - Decrypt.LOWER_A_ASCII_CODE - sub[(i + 1) % 4])
                                      % Decrypt.ALPHABET_SIZE + Decrypt.LOWER_A_ASCII_CODE)
        decrypted_text = [decrypted_text[i:i + key] for i in range(0, len(decrypted_text), key)]
        for i in range(int(len(decrypted_text) / 2)):
            decrypted_text[i], decrypted_text[len(decrypted_text) - i - 2] = decrypted_text[
                                                                                 len(decrypted_text) - i - 2], \
                                                                             decrypted_text[i]
        for i in decrypted_text:
            result += i
        return result


if __name__ == '__main__':
    path = "sample_encrypted_text.txt"
    decrypted_text = Decrypt.decrypt_text(path, 4)
    print(decrypted_text)
