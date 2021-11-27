import sqlite3
import random

global db, sql
db = sqlite3.connect('server.db')
sql = db.cursor()

sql.execute('''CREATE TABLE IF NOT EXISTS users (
	login Text,
	password Text,
	cash int

	)''')
db.commit()