# Saving Passwords
1. Zaprojektuj i zaimplementuj prosty własny sposób przechowywania haseł w bazie sqlite: użytkownik podaje hasło dwa razy, losujesz sól, hashujesz wszystko i zapisujesz hash oraz sól do bazy. Dodaj funkcję weryfikującą hasło.
2. Przerób pkt 1. aby używał pbkdf2_hmac. Zrób z tego porządny projekt (testy, docstringi, itp.)
## Usage:
Run from `databaseHandler.py`
##
**add_user(self) -> None**
* input: None
* output: None
```python
DatabaseHandler.add_user()
```

**verify_user(self) -> str**
* input: None
* output: str (information about success as a string)
```python
DatabaseHandler.verify_user()
```