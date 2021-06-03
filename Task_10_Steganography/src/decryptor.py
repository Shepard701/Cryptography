import cv2
from tkinter import filedialog, Tk, Button, Label, Text, END, WORD
from PIL import Image, ImageTk
import numpy as np

global PATH
IMAGE_RESOLUTION = 300, 300
SHIFT = 3
LOWER_A_ASCII_CODE = 97
UPPER_A_ASCII_CODE = 65
ALPHABET_SIZE = 26


class Decryptor:

    @staticmethod
    def decrypt_text_from_image():
        """
        Loads and displays image,
        decrypts text from given image,
        decodes text with Caesar Cipher,
        displays decoded text

        :return: None
        """
        global PATH
        decrypted_text = ''
        path = filedialog.askopenfilename()
        load_image = Image.open(path)
        load_image.thumbnail(IMAGE_RESOLUTION, Image.ANTIALIAS)
        load_image = np.asarray(load_image)
        load_image = Image.fromarray(np.uint8(load_image))
        render = ImageTk.PhotoImage(load_image)
        img = Label(decryptor, image=render)
        img.image = render
        img.place(x=50, y=50)

        img = cv2.imread(path)
        data = []
        flag = False
        for index_i, i in enumerate(img):
            i.tolist()
            for index_j, j in enumerate(i):
                if index_j % 3 == 2:
                    data.append(bin(j[0])[-1])
                    data.append(bin(j[1])[-1])
                    if bin(j[2])[-1] == '1':
                        flag = True
                        break
                else:
                    data.append(bin(j[0])[-1])
                    data.append(bin(j[1])[-1])
                    data.append(bin(j[2])[-1])
            if flag:
                break

        text = []
        for i in range(int((len(data)+1)/8)):
            text.append(data[i*8:(i*8+8)])
        text = [chr(int(''.join(i), 2)) for i in text]
        text = ''.join(text)
        for i in range(len(text)):
            char = text[i]
            if char.isupper():
                decrypted_text += chr((ord(char) - SHIFT - UPPER_A_ASCII_CODE) % ALPHABET_SIZE + UPPER_A_ASCII_CODE)
            elif char.islower():
                decrypted_text += chr((ord(char) - SHIFT - LOWER_A_ASCII_CODE) % ALPHABET_SIZE + LOWER_A_ASCII_CODE)
            else:
                decrypted_text += char
        message_text.insert(END, decrypted_text)


if __name__ == '__main__':
    """
    Creates GUI for application and starts it
    """
    decryptor = Tk()
    decryptor.title("Image Decryptor")
    decryptor.geometry('400x475')
    decryptor.configure(background='orange')
    load_image_and_decrypt_button = Button(decryptor, text="Choose Image and decrypt", bg='darkorange', fg='black',
                                           command=Decryptor.decrypt_text_from_image)
    load_image_and_decrypt_button.place(x=113, y=10, width=176)
    message_label = Label(decryptor, text="Decrypted Text", bg='orange', font=("Times New Roman", 15))
    message_label.place(x=135, y=360)
    message_text = Text(decryptor, wrap=WORD, width=43, background="lightgrey")
    message_text.place(x=25, y=390, height=65)
    decryptor.mainloop()
