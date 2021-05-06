import hashlib
import json
from time import time

# -------------------------------------------------------------------------------------------------------------
# Class forked from the blockchain tutorial (https://github.com/mchrupcala/blockchain-walkthrough) and modified
# -------------------------------------------------------------------------------------------------------------


class Blockchain(object):

    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        self.new_block(previous_hash="One to rule them all", proof=1)

    def new_block(self, proof, previous_hash=None):
        """
        Create new block

        :param proof: integer number
        :param previous_hash: hash from previous block
        :return: new block
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.pending_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.pending_transactions = []
        self.chain.append(block)

        return block

    @property
    def last_block(self):
        """
        Getter for last block

        :return: Last block
        """
        return self.chain[-1]

    def new_transaction(self, sender, recipient, topic, message):
        """
        Creates new transaction

        :param sender: Name of sender
        :param recipient: Name of recipient
        :param topic: Topic of the message
        :param message: Message
        :return: None
        """
        transaction = {
            'sender': sender,
            'recipient': recipient,
            'topic': topic,
            'message': message,
        }
        self.pending_transactions.append(transaction)

    def hash(self, block):
        """
        Hashes block

        :param block: Block
        :return: Hashed block
        """
        string_object = json.dumps(block, sort_keys=True)
        block_string = string_object.encode()

        raw_hash = hashlib.sha256(block_string)
        hex_hash = raw_hash.hexdigest()

        return hex_hash

    # -------------------------------------
    # Methods added outside of the tutorial
    # -------------------------------------

    def chain_quantity(self):
        """
        Getter for chain quantity

        :return: Chain Quantity
        """
        return len(self.chain)

    def block_display(self, index):
        """
        Getter for specific block

        :param index: index of block
        :return: Block
        """
        return self.chain[index]

    def current_transactions(self):
        """
        Getter for pending transactions

        :return: Pending transactions
        """
        return self.pending_transactions
