## This is for additional tasks

### SQL Injections

### Task 1
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
### Task 2
- The code to insert name and email to the table. The following code is safe from SQL injection because it uses parameterized queries which properly escape user input:
```python
name = input("Name: ")
email = input("Email: ")

def insert_student(id, name, email):
    query = "INSERT INTO students (id, name, email) VALUES (%s, %s, %s)"
    cursor.execute(query, (id, name, email))
```

### Task 3
- Here is the progress of creating a new role and granting permission and doing not granted query. the command failed because the role does have permission only to `SELECT`:

<img src="https://iili.io/fyg68S1.png" width="600">