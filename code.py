import sqlite3

ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'password123'

def connect_db():
    conn = sqlite3.connect('users.db')
    return conn

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                      id INTEGER PRIMARY KEY,
                      username TEXT,
                      password TEXT)''')
    conn.commit()
    conn.close()

def add_user(username, password):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO users (username, password) VALUES ('{username}', '{password}')")
    conn.commit()
    conn.close()

def authenticate_user(username, password):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE username='{username}' AND password='{password}'")
    user = cursor.fetchone()
    conn.close()
    return user

def login():
    print("Welcome to the insecure login system!")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        print("Admin login successful!")
    elif authenticate_user(username, password):
        print("User login successful!")
    else:
        print("Login failed! Invalid credentials.")

def main():
    create_table()
    add_user('test_user', 'test_pass')
    login()

if __name__ == '__main__':
    main()
