from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
import cv2
import numpy as np
import math

global PATH
IMAGE_RESOLUTION = 200, 200
SHIFT = 3
LOWER_A_ASCII_CODE = 97
UPPER_A_ASCII_CODE = 65
ALPHABET_SIZE = 26


class Encryptor:

    @staticmethod
    def load_image():
        """
        Loads and displays image

        :return: None
        """
        global PATH
        PATH = filedialog.askopenfilename()
        load_image = Image.open(PATH)
        load_image.thumbnail(IMAGE_RESOLUTION, Image.ANTIALIAS)
        np_load_image = np.asarray(load_image)
        np_load_image = Image.fromarray(np.uint8(np_load_image))
        render = ImageTk.PhotoImage(np_load_image)
        img = Label(encryptor, image=render)
        img.image = render
        img.place(x=25, y=60)

    @staticmethod
    def encrypt_text_into_image():
        """
        Encodes text with Caesar Cipher,
        encrypts image with encoded text,
        saves new copy of an image

        :return: None
        """
        global PATH
        encrypted_text = ''
        text = input_text.get(1.0, "end-1c")
        for i in range(len(text)):
            char = text[i]
            if char.isupper():
                encrypted_text += chr((ord(char) + SHIFT - UPPER_A_ASCII_CODE) % ALPHABET_SIZE + UPPER_A_ASCII_CODE)
            elif char.islower():
                encrypted_text += chr((ord(char) + SHIFT - LOWER_A_ASCII_CODE) % ALPHABET_SIZE + LOWER_A_ASCII_CODE)
            else:
                encrypted_text += char
        img = cv2.imread(PATH)
        encrypted_text = [format(ord(i), '08b') for i in encrypted_text]
        _, width, _ = img.shape
        pixels_required = len(encrypted_text) * 3
        row_required = pixels_required / width
        row_required = math.ceil(row_required)
        counter = 0
        char_counter = 0
        for i in range(row_required + 1):
            while counter < width and char_counter < len(encrypted_text):
                char = encrypted_text[char_counter]
                char_counter += 1
                for index, j in enumerate(char):
                    if ((j == '1' and img[i][counter][index % 3] % 2 == 0) or (
                            j == '0' and img[i][counter][index % 3] % 2 == 1)):
                        img[i][counter][index % 3] -= 1
                    if index % 3 == 2:
                        counter += 1
                    if index == 7:
                        if char_counter * 3 < pixels_required and img[i][counter][2] % 2 == 1:
                            img[i][counter][2] -= 1
                        if char_counter * 3 >= pixels_required and img[i][counter][2] % 2 == 0:
                            img[i][counter][2] -= 1
                        counter += 1
            counter = 0
        cv2.imwrite("encrypted_image.png", img)
        success_label = Label(encryptor, text="Encryption Successful!",
                              bg='orange', font=("Times New Roman", 16))
        success_label.place(x=275, y=230)


if __name__ == '__main__':
    """
    Creates GUI for application and starts it
    """
    encryptor = Tk()
    encryptor.title("Image Encryptor")
    encryptor.geometry('500x280')
    encryptor.configure(background='orange')
    input_text = Text(encryptor, wrap=WORD, width=25, background="lightgrey")
    input_text.place(x=270, y=60, height=120)
    load_image_button = Button(encryptor, text="Choose Image", bg='darkorange', fg='black',
                               command=Encryptor.load_image)
    load_image_button.place(x=200, y=10, width=100)
    encrypt_button = Button(encryptor, text="Encrypt", bg='darkorange', fg='black',
                            command=Encryptor.encrypt_text_into_image)
    encrypt_button.place(x=345, y=190)
    encryptor.mainloop()
