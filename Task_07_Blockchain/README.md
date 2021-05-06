# Blockchain
* Zaimplementuj własną sieć blockchain analogiczną do linków przedstawionych na wykładzie
* Wiadomości mogą dotyczyć dowolnej rzeczy: od świata finansowego, do własnego budżetu czy kolekcji znaczków pocztowych
* Zadbaj, aby był to pełnoprawny projekt łatwy w obsłudze dla przeciętnego człowieka (a więc podstawowy frontend się przyda)
* Dodaj API do wykonywania "transakcji", pobierania stanu portfela, stanu sieci, liczby bloków w łańcuchu, itp.
## Usage:
Run app from `src/menu.py` with following code (Included in menu.py)
```python
Menu.start_app()
```
## Application appearance:
```text
--- MAIN MENU ---
[1] Show current state of blockchain
[2] Create new transaction (message)
[3] Create new block
[4] Show quantity of blocks in chain
[5] Display specific block
[6] Display current transactions (messages)
-----------------
[0] Exit the program.
```
## Methods:
You can find methods' docstrings in `src/blockchain.py`