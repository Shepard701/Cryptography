import unittest

from Task_05_Cryptanalysis_V1.src.cipher import Cipher


class HashFunctionsTest(unittest.TestCase):

    def test_init(self):
        ci = Cipher()
        self.assertIsInstance(ci, Cipher)

    def test_encrypt(self):
        encrypted_text = Cipher.encrypt('./sample_text.txt', 4)
        self.assertEqual(encrypted_text, 'tlivdbxbsmwxojtmjxoxpvxkewwxemsmpdzk')
