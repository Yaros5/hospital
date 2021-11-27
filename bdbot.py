import  telebot
import sqlite3

TOKEN = "2135915175:AAGz5gnZOTkkbb85n5TEg3QCtSA--wIkG_k"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    connect = sqlite3.connect("user.db")
    cursor = connect.cursor()
    
    cursor.execute("""CREATE TABLE IF NOT EXISTS login_id(
      id INTEGER
    )""")
    
    connect.commit()

    # check in fields
    peopole_id = message.chat.id
    cursor.execute(f"SELECT id FROM login_id WHERE id = {peopole_id}")
    data = cursor.fetchome()
    if data is None:
        # add values in fields
        user_id = [message.chat.id]
        cursor.execute("INSERT INTO login_id VALUES(?);", user_id)
    else:
        bot.send_message(message.chat.id, "Такий користувач вже є")




@bot.message_handler(commands=["delete"])
def delete(message):
    pass