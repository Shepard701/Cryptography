import sqlite3
import os

from Task_03_Saving_Passwords.src.passwordHandler import PasswordHandler


class DatabaseHandler:
    DATABASE = 'saving-passwords.db'

    def __init__(self) -> None:
        """
        Creates a database and necessary table if hasn't existed yet
        """
        if not os.path.exists(self.DATABASE):
            conn = sqlite3.connect(self.DATABASE)
            cursor = conn.cursor()
            cursor.execute("""CREATE TABLE users (username text, salt text, password text)""")
            conn.commit()
            conn.close()

    def add_user(self) -> None:
        """
        Asks user to enter necessary data and adds him to a database.

        :return: None
        """
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        password_repeated = input("Reenter your password: ")
        if password == password_repeated:
            conn = sqlite3.connect(self.DATABASE)
            cursor = conn.cursor()
            salt, hashed_password = PasswordHandler.hash_password(password)
            cursor.execute("INSERT INTO users VALUES (?,?,?)", (username, salt, hashed_password))
            conn.commit()
            conn.close()
        else:
            print("Passwords doesn't match!")

    def verify_user(self) -> str:
        """
        Verifies given by user data and returns information about compatibility

        :return: information about success as a string
        """
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        conn = sqlite3.connect(self.DATABASE)
        cursor = conn.cursor()
        cursor.execute("SELECT salt, password FROM users WHERE username = :username", {'username': username})
        data = cursor.fetchall()
        for row in data:
            salt = row[0]
            correct_password = row[1]
        print(salt)
        print(correct_password)
        check = PasswordHandler.verify_password(password, salt, correct_password)
        conn.close()
        if check:
            return "Password is correct."
        else:
            return "Passwords doesn't match! Try again."


if __name__ == '__main__':
    """
    dh = DatabaseHandler() - initialize database
    dh.add_user - use to add user to a database
    dh.verify_user - use to check user's password (needs print or logger to show information
    """
    dh = DatabaseHandler()

    # dh.add_user()
    # print(dh.verify_user())
