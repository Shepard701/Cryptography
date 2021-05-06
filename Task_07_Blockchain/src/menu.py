import logging

from Task_07_Blockchain.src.blockchain import Blockchain


class Menu:
    logger = logging.getLogger("hashing")
    logging.basicConfig(level=logging.DEBUG)

    def __init__(self, key: int = 0):
        self._key = key
        pass

    @staticmethod
    def draw_menu():
        print("[1] Show current state of blockchain")
        print("[2] Create new transaction")
        print("[3] Create new block")
        print("[4] Show quantity of block in chain")
        print("[0] Exit the program.")

    @staticmethod
    def start_app():
        bc = Blockchain()
        option = -1
        while option != 0:
            Menu.draw_menu()
            option = int(input("Enter your option: "))
            if option == 0:
                print("Closing the app . . .")
            elif option == 1:
                print("Blockchain: ", bc.chain)
            elif option == 2:
                sender = input("Input your name: ")
                receiver = input("Input name of the receiver: ")
                amount = int(input("Input amount which you would tile to transfer: "))
                bc.new_transaction(sender, receiver, amount)
            elif option == 3:
                proof = int(input("Input proof value: "))
                bc.new_block(proof)
            elif option == 4:
                print("Quantity of blocks: ", bc.chain_quantity())
            else:
                print("Invalid option")
            print("\n-----------------------------------------------------------------------------------------------\n")


if __name__ == '__main__':
    Menu.start_app()
