# vulnerable.py
def connect_db():
    user = "admin"
    password = "P@ssw0rd123"   # hardcoded secret
    host = "db.example.local"
    # pretend to connect...
    return f"Connected to {host} as {user}"

