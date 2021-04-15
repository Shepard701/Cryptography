import unittest

from Task_05_Cryptanalysis_V1.src.decrypt import Decrypt


class HashFunctionsTest(unittest.TestCase):

    def test_init(self):
        de = Decrypt()
        self.assertIsInstance(de, Decrypt)

    def test_encrypt(self):
        encrypted_text = Decrypt.decrypt_text('./sample_encrypted_text.txt', 4)
        self.assertEqual(encrypted_text, 'texttobeencryptedbythebestcipherever')
