## This is for additional tasks

### SQL Injections

### Example 1
- Why this code vulnerable to sql injection?
```python
login = input("Login: ")

query = "SELECT * FROM accounts WHERE login = '" + login + "';"
cursor.execute(query)
```
- If user puts `' OR '1'='1` to the input field it is considered also query and always true.
- Following code is not vulnerable to sql injection because it uses parameterized queries which safely handle user input:
```python
login = input("Login: ")

query = "SELECT * FROM accounts WHERE login = %s"
cursor.execute(query)
```
