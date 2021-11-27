import telebot

TOKEN = "2142529380:AAH9OvlYi9zcii99FWijDrQiVhwGOjuFRn0"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=["text"])
def buttons(message):
    # ! ADMIN
    # / remove webhook
    if message.text == "remove_webhook":
        bot.delete_message(message.chat.id, message.message_id)
        bot.remove_webhook()
    # / stop polling
    elif message.text == "stop_polling":
        bot.delete_message(message.chat.id, message.message_id)
        bot.stop_bot()
    # / secret
    elif message.text == "CHOSEN ONES":
        # delete
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, "*CHOSEN ONES ARE THE BEST!*", parse_mode="Markdown")