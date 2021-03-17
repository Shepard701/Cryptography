import unittest

from Task_02_Hash_Functions.src.hashFunctions import HashFunctions


class HashFunctionsTest(unittest.TestCase):

    def test_init(self):
        hf = HashFunctions()
        self.assertIsInstance(hf, HashFunctions)

    # Works only if ubuntu file exists in test folder
    def test_hash_file_ubuntu(self):
        hashed_file = HashFunctions.hash_file('./ubuntu-20.10-desktop-amd64.iso', 'sha256')
        self.assertEqual(hashed_file, '3ef833828009fb69d5c584f3701d6946f89fa304757b7947e792f9491caa270e')

    def test_hash_file_txt(self):
        hashed_file = HashFunctions.hash_file('./test.txt', 'sha256')
        self.assertEqual(hashed_file, 'bd65cac529f4998de7c545f0def5153ae8e796b594e32ab7b9f5e030cc48e0d8')
