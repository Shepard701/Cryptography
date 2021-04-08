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
    return Symmetric.generate_random_key()


@app.post("/symmetric/key")
def post_key(key):
    symmetric.set_key(key)
    return {"Info": "Key has been set"}


@app.post("/symmetric/encode")
def post_encode(msg: Message):
    return {"Encoded message": symmetric.encode_message(msg.text)}


@app.post("/symmetric/decode")
def post_decode(msg: Message):
    return {"Decoded message": symmetric.decode_message(msg.text)}


@app.get("/asymmetric/key")
def get_asymmetric_keys():
    asymmetric.generate_keys()
    keys = asymmetric.get_keys_hex()
    return {"Private Key": keys[0], "Public Key:": keys[1]}


@app.get("/asymmetric/key/ssh")
def get_asymmetric_keys_ssh():
    keys = asymmetric.get_keys_hex_ssh()
    return {"Private SSH Key": keys[0], "Public SSH Key:": keys[1]}


@app.post("/asymmetric/key")
def post_asymmetric_keys(private_key, public_key):
    asymmetric.set_keys(private_key, public_key)
    return {"Info": "Keys have been set"}


@app.post("/asymmetric/sign")
def post_asymmetric_sing_message(msg: Message):
    signed_message = asymmetric.sign_message(msg.text)
    return {"Signed Message": signed_message}


@app.post("/asymmetric/verify")
def post_asymmetric_sing_message(msg: SignedMessage):
    verification = asymmetric.verify_message(msg.text, msg.signature)
    return {"Sign verification": verification}


@app.post("/asymmetric/encode")
def post_asymmetric_encode_message(msg: Message):
    encoded_message = asymmetric.encode_message(msg.text)
    return {"Encoded message": encoded_message}


@app.post("/asymmetric/decode")
def post_asymmetric_decode_message(msg: Message):
    decoded_message = asymmetric.decode_message(msg.text)
    return {"Decoded message": decoded_message}
