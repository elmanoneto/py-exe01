import sqlite3

def create_table(con):
    con.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")

def add_user(con, name):
    con.execute("INSERT INTO users (name) VALUES (?)", (name,))
    con.commit()
    
def get_users(con):
    return con.execute("SELECT name FROM users").fetchall()

def delete_user(con, id):
    con.execute("DELETE FROM users WHERE id=?", (id,))
    con.commit()