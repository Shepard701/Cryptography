# Cryptanalysis V1
Spróbować wymyślić swój własny szyfr. Wymagania:
1. podstawieniowy, monoalfabetyczny lub homofoniczny (max 3 podstawienia per znak)
2. transpozycje kolumn
3. transpozycje wierszy
4. szyfr "przyjmuje" angielski alfabet
5. Spacje mogą zostać, ale nie muszą
## Usage
Run app from the `cipher.py` to encrypt text, or from `decrypt.py` to decrypt text.
##
**encrypt(path: str, key: int) -> str**
* input: `path: str` (path to file with text to encrypt); `key: int` (integer number the cipher will use in encrypting - shouldn't be to high)
* output: `text: str` (encrypted text returned as string)
```python
Cipher.encrypt(path = './sample_path.txt', key = '4')
```

**decrypt_text(path: str, key: int) -> str**
* input: `path: str` (path to file with text to decrypt); `key: int` (integer number the cipher will use in decrypting)
* output: `text: str` (decrypted text returned as string)
```python
Decrypt.decrypt_path(path = './sample_path.txt', key = '4')
```