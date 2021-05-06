import unittest

from Task_07_Blockchain.src.blockchain import Blockchain


class SavingPasswordTest(unittest.TestCase):

    def test_init(self):
        bc = Blockchain()
        self.assertIsInstance(bc, Blockchain)

    def test_new_transaction(self):
        bc = Blockchain()
        bc.new_transaction('sender', 'receiver', 'topic', 'message')
        transaction = bc.current_transactions()
        self.assertIsNotNone(transaction[0])

    def test_current_transaction(self):
        bc = Blockchain()
        bc.new_transaction('sender1', 'receiver1', 'topic1', 'message1')
        bc.new_transaction('sender2', 'receiver2', 'topic2', 'message2')
        bc.new_transaction('sender3', 'receiver3', 'topic3', 'message3')
        self.assertEqual(len(bc.current_transactions()), 3)

    def test_new_block(self):
        bc = Blockchain()
        bc.new_transaction('sender1', 'receiver1', 'topic1', 'message1')
        bc.new_transaction('sender2', 'receiver2', 'topic2', 'message2')
        bc.new_block(123)
        self.assertGreater(bc.chain_quantity(), 1)
