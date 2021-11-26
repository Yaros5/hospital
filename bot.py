import telebot


# ! API
TOKEN = "2142529380:AAH9OvlYi9zcii99FWijDrQiVhwGOjuFRn0"


bot = telebot.TeleBot(TOKEN)


# ! start
@bot.message_handler(commands=['start', 'help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привіт, {0.first_name}!👋'.format(
        message.from_user, bot.get_me()), parse_mode='html')
    bot.send_message(message.chat.id, 'Напиши своє ім\'я та прізвише')
    name = message.text


# ! changename
@bot.message_handler(commands=['changename'])
def changename(message):
    bot.send_message(message.chat.id, 'Напиши своє ім\'я та прізвише')
    name = message.text


bot.infinity_polling()