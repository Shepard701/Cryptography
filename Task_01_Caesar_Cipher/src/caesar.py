class Caesar:
    ALPHABET_SIZE = 26
    LOWER_A_ASCII_CODE = 97
    LOWER_Z_ASCII_CODE = 122

    def __init__(self, key: int = 0):
        self._key = key
        pass

    @staticmethod
    def caesar_manual(text: str) -> tuple[str, int]:
        """
        Decrypts given text and returns user's answer as a string and its shift as an int

        :param text: encrypted text
        :return: decrypted text as a string and its shift as an int
        """
        text = text.lower()
        results = []
        for i in range(1, Caesar.ALPHABET_SIZE):
            temp_result = ""
            for j in range(len(text)):
                if Caesar.LOWER_A_ASCII_CODE <= ord(text[j]) <= Caesar.LOWER_Z_ASCII_CODE:
                    if ord(text[j]) - i < Caesar.LOWER_A_ASCII_CODE:
                        temp_result += chr(ord(text[j]) - i + Caesar.ALPHABET_SIZE)
                    else:
                        temp_result += chr(ord(text[j]) - i)
                else:
                    temp_result += text[j]
            results.append(temp_result)

        for i in range(len(results)):
            print("Nr {}: {}".format(i + 1, results[i]))
        shift = int(input("Choose number of correct decipher: "))

        return results[shift - 1], shift
