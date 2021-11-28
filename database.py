import sqlite3

global db, sql
db = sqlite3.connect('server.db')
sql = db.cursor()
sql.execute('''CREATE TABLE IF NOT EXISTS users (login TEXT, password TEXT)''')
db.commit()

def reg():
    user_login = input('Login: ')
    user_password = input('Password: ')

    sql.execute(f'SELECT login FROM users WHERE login = "{user_login}" ')
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO users VALUES (?, ?)" , (user_login, user_password))
        db.commit()
        print("[Вас успішно зареєстровано]\n")
    else:
        print("[Такий акаунт вже існує]\n")

        for value in sql.execute(f"SELECT * FROM users"):
            print(value)

def main():
    reg()

main()