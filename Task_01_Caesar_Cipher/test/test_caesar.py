from unittest import TestCase

from Task_01_Caesar_Cipher.src.caesar import Caesar


class Test(TestCase):

    def test_init(self):
        c = Caesar()
        self.assertIsInstance(c, Caesar)

    def test_cesar_manual(self):
        data = "WKLV LV VDPSOH WHAW WR GHFUBSW LQ WKLV SURJUDP"
        decrypted_text, shift = Caesar.caesar_manual(data)
        self.assertEqual(decrypted_text, "this is sample text to decrypt in this program")
        self.assertEqual(shift, 3)
