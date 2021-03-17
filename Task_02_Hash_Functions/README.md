# Hash Functions
1. Zaimplementuj hashowanie wszystkimi funkcjami zwracanymi przez algorithms_available z biblioteki hashlib wraz ze zwróceniem informacji o czasie hashowania dla danych wejściowych z konsoli.
2. Ściągnij duży plik (np. ubuntu) i sprawdź, czy hash się zgadza.
3. Zaimplementuj funkcję, która hashuje dowolny blik binarny z dysku. Sprawdź ją przez hashowanie obrazu ubuntu z pkt 2.
4. Za pomocą pakietu timeit zbadaj szybkość generowania hashy dla wiadomości o różnych rozmiarach. Przedstaw to na wykresie za pomocą matplotlib (mniej zalecane) czy plotly (zalecane).
## Usage:
**hash_all(cleartext: str) -> None**
* input: `cleartext: str` (text)
* output: `None` (prints all possible hashes from [hashlib](https://docs.python.org/3/library/hashlib.html), returns nothing)
```python
HashFunctions.hash_all(cleartext = 'Sample text.')
```

**hash_file(path: str, alg: str) -> str**
* input: `path: str` (path to file), `alg: str` (hashing algorithm name from [hashlib](https://docs.python.org/3/library/hashlib.html))
* output: `out.hexdigest(): str` (hash returned as a string)
```python
example = HashFunctions.hash_file(path = './sampleFile.txt', alg = 'md5')
```

**hash_time_plot(amount: int, alg: str) -> None**
* input: `amount: int` (amount of strings), `alg: str` (hashing algorithm name from [hashlib](https://docs.python.org/3/library/hashlib.html))
* output: `None` (results displayed as a plot, returns nothing)
```python
HashFunction.hash_time_plot(amount = 8, alg = 'md5')
```