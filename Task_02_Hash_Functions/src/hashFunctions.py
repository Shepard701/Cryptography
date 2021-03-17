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
    def hash_file(path: str) -> str:
        out = hl.sha256()
        with open(path, 'rb') as file:
            file_block = file.read(out.block_size)
            while len(file_block) > 0:
                out.update(file_block)
                file_block = file.read(out.block_size)
        return out.hexdigest()

    @staticmethod
    def hash_time_plot(length: int, alg: str) -> None:
        result = {'length': [], 'speed': []}
        text = ""

        for i in range(1, length + 1):
            # Loop to make string longer
            for j in range(200):
                text += random.choice(string.ascii_lowercase)
            result['length'].append(i*200)
            result['speed'].append(timeit.timeit(lambda: hl.new(alg, text.encode())))

        print(result)
        plot = pl.line(result, x='length', y='speed')
        plot.show()


# HashFunctions.hash_all('Text to hash.')
# print(HashFunctions.hash_file("./ubuntu-20.10-desktop-amd64.iso"))
# HashFunctions.hash_time_plot(8, 'md5')
