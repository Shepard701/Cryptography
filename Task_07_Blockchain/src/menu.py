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
        print("--- MAIN MENU ---")
        print("[1] Show current state of blockchain")
        print("[2] Create new transaction (message)")
        print("[3] Create new block")
        print("[4] Show quantity of blocks in chain")
        print("[5] Display specific block")
        print("[6] Display current transactions (messages)")
        print("-----------------\n[0] Exit the program.")

    @staticmethod
    def start_app():
        bc = Blockchain()
        option = 'init'
        while option != '0':
            Menu.draw_menu()
            option = input("Enter your option [0-6]: ")
            if option == '0':
                logging.info("Closing the app . . .\n")
            elif option == '1':
                print("Blockchain:\n", bc.chain)
            elif option == '2':
                sender = input("Input your name: ")
                recipient = input("Input name of the recipient: ")
                topic = input("Input the topic of the message: ")
                message = input("Input message: ")
                bc.new_transaction(sender, recipient, topic, message)
            elif option == '3':
                try:
                    proof = int(input("Input proof value: "))
                    bc.new_block(proof)
                except ValueError:
                    logging.warning("Proof value should be an integer number e.g. '1234' - Try again")
            elif option == '4':
                print("Quantity of blocks: ", bc.chain_quantity())
            elif option == '5':
                index = int(input("Input index of block: ")) - 1
                try:
                    print("Chosen block: ", bc.block_display(index))
                except IndexError:
                    logging.warning("Given index doesn't exist - Try again")
            elif option == '6':
                ct = bc.current_transactions()
                if ct:
                    print("Transactions: \n", bc.current_transactions())
                else:
                    logging.info("Currently there aren't any transactions pending\n")
            else:
                logging.warning("Invalid option\n")
            print("\n-----------------------------------------------------------------------------------------------\n")


if __name__ == '__main__':
    """
    Start app here
    """
    Menu.start_app()
