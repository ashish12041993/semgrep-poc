import sqlite3

def get_user_by_name(name):
    conn = sqlite3.connect('app.db')
    cur = conn.cursor()
    # vulnerable: string interpolation into SQL
    query = f"SELECT id, username FROM users WHERE username = '{name}'"
    cur.execute(query)
    return cur.fetchall()

