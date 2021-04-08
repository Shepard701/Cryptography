from fastapi import FastAPI
from src.symmetric import Symmetric
from src.asymmetric import Asymmetric
from src.tools import Message, SignedMessage

symmetric = Symmetric()
asymmetric = Asymmetric()

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "This is 4th task of cryptography classes"}


@app.get("/symmetric/key")
def get_key():
    """
    Generate random key

    :return: Key as str in HEX format
    """
    return Symmetric.generate_random_key()


@app.post("/symmetric/key")
def post_key(key):
    """
    Sets given key as new one in the app

    :param key: Key as str in HEX
    :return: Information
    """
    symmetric.set_key(key)
    return {"Info": "Key has been set"}


@app.post("/symmetric/encode")
def post_encode(msg: Message):
    """
    Encode given message with key stored in the app

    :param msg: Message to encode
    :return: Encoded message as bytes
    """
    return {"Encoded message": symmetric.encode_message(msg.text)}


@app.post("/symmetric/decode")
def post_decode(msg: Message):
    """
    Decode given message with key stored in the app

    :param msg: Message to decode
    :return: Decoded message as bytes
    """
    return {"Decoded message": symmetric.decode_message(msg.text)}


@app.get("/asymmetric/key")
def get_asymmetric_keys():
    """
    Returns private and public keys stored in the app

    :return: Private and public keys in HEX format
    """
    asymmetric.generate_keys()
    keys = asymmetric.get_keys_hex()
    return {"Private Key": keys[0], "Public Key:": keys[1]}


@app.get("/asymmetric/key/ssh")
def get_asymmetric_keys_ssh():
    """
    Returns private and public keys stored in the app with SSH encoding

    :return: Private and public keys in HEX format and SSH encoding
    """
    keys = asymmetric.get_keys_hex_ssh()
    return {"Private SSH Key": keys[0], "Public SSH Key:": keys[1]}


@app.post("/asymmetric/key")
def post_asymmetric_keys(private_key, public_key):
    """
    Set given keys as new ones in the app

    :param private_key: Private Key in HEX format
    :param public_key: Public Key in HEX format
    :return: Information
    """
    asymmetric.set_keys(private_key, public_key)
    return {"Info": "Keys have been set"}


@app.post("/asymmetric/sign")
def post_asymmetric_sing_message(msg: Message):
    """
    Signs given message with private key stored in the app

    :param msg: Message to sign
    :return: Signed message as bytes
    """
    signed_message = asymmetric.sign_message(msg.text)
    return {"Signed Message": signed_message}


@app.post("/asymmetric/verify")
def post_asymmetric_sing_message(msg: SignedMessage):
    """
    Verifies if given message equals signature by the public key stored in app

    :param msg: Message to verify and signed message to compare with
    :return: Boolean value depending of correct verification
    """
    verification = asymmetric.verify_message(msg.text, msg.signature)
    return {"Sign verification": verification}


@app.post("/asymmetric/encode")
def post_asymmetric_encode_message(msg: Message):
    """
    Encode given message with public key stored in the app

    :param msg: Message to encode
    :return: Encoded message as bytes
    """
    encoded_message = asymmetric.encode_message(msg.text)
    return {"Encoded message": encoded_message}


@app.post("/asymmetric/decode")
def post_asymmetric_decode_message(msg: Message):
    """
    Decode given message with private key stored in the app

    :param msg: Message to decode
    :return: Decoded message
    """
    decoded_message = asymmetric.decode_message(msg.text)
    return {"Decoded message": decoded_message}
