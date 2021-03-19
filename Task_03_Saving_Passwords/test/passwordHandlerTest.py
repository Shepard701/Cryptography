import unittest

from Task_03_Saving_Passwords.src.passwordHandler import PasswordHandler


class SavingPasswordTest(unittest.TestCase):

    def test_init(self):
        ph = PasswordHandler()
        self.assertIsInstance(ph, PasswordHandler)

    def test_verify_password(self):
        boolean = PasswordHandler.verify_password("qwerty", b'\x0b\xaeH\x9a\xd8\xaf\xb4\xe28\x91$\xcb\x9d\xc8Sq',
                                                  "0947e782db8a310c232b5455f77fd5e23836166e05998b78aed6b11bf30b3d4d")
        self.assertTrue(boolean)

    def test_verify_wrong_password(self):
        boolean = PasswordHandler.verify_password("pass", b'\x0b', "isthishash?")
        self.assertFalse(boolean)

