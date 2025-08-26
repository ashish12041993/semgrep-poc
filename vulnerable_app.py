import os
import sqlite3

def insecure_eval(user_input):
    # ❌ RCE risk
    return eval(user_input)

def sql_injection_example(user_input):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    # ❌ SQL Injection
    query = f"SELECT * FROM users WHERE name = '{user_input}'"
    cursor.execute(query)
    return cursor.fetchall()

def hardcoded_secret():
    # ❌ Hardcoded secret
    api_key = "sk_live_1234567890_SUPER_SECRET"
    return api_key

def command_injection(user_input):
    # ❌ Command injection
    os.system(f"echo {user_input}")

if __name__ == "__main__":
    user_data = input("Enter something: ")
    print("Eval result:", insecure_eval(user_data))
    print("SQL result:", sql_injection_example(user_data))
    print("API Key:", hardcoded_secret())
    command_injection(user_data)

