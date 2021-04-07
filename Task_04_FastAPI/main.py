from fastapi import FastAPI
from src.symmetric import Symmetric
from src.tools import Message

symmetric = Symmetric()

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
