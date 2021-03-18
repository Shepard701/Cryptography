import hashlib as hl
import logging
import random
import string
import timeit
import plotly.express as pl


class HashFunctions:
    logger = logging.getLogger("hashing")
    logging.basicConfig(level=logging.DEBUG)

    def __init__(self, key: int = 0):
        self._key = key
        pass

    @staticmethod
    def hash_all(cleartext: str) -> None:
        """
        Prints all possible hashes from hashlib to a given text

        :param cleartext: text
        :return: None
        """
        encoded_text = cleartext.encode()

        for alg in hl.algorithms_available:
            out = hl.new(alg)
            out.update(encoded_text)
            time_check = timeit.timeit(lambda: hl.new(alg, encoded_text))
            if alg == 'shake_128' or alg == 'shake_256':
                print(f'{alg}: {out.hexdigest(16)} time: {time_check:.2f}')
            else:
                print(f'{alg}: {out.hexdigest()} time: {time_check:.2f}')

    @staticmethod
    def hash_file(path: str, alg: str) -> str:
        """
        Returns hash as a string to a given file

        :param path: path to file
        :param alg: hashing algorithm name from hashlib
        :return: hash returned as a string
        """
        out = hl.new(alg)
        with open(path, 'rb') as file:
            file_block = file.read(out.block_size)
            while len(file_block) > 0:
                out.update(file_block)
                file_block = file.read(out.block_size)
        return out.hexdigest()

    @staticmethod
    def hash_time_plot(amount: int, alg: str) -> None:
        """
        Displays plot with string length and time taken to hash it

        :param amount: amount of strings
        :param alg: hashing algorithm name from hashlib
        :return: None
        """
        result = {'length': [], 'speed': []}
        text = ""

        for i in range(1, amount + 1):
            # Loop to make string longer
            for j in range(200):
                text += random.choice(string.ascii_lowercase)
            result['length'].append(i * 200)
            result['speed'].append(timeit.timeit(lambda: hl.new(alg, text.encode())))

        plot = pl.line(result, x='length', y='speed')
        plot.show()
