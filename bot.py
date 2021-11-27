from typing import ItemsView
from telebot import types
from bot_admin import  bot

# ! start
@bot.message_handler(commands=["start", "help"])
def start_message(message):
    bot.remove_webhook()
    # remove keyboard
    remove_keyboard = types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, "*Привіт, {0.first_name}!👋*".format(message.from_user, bot.get_me()), reply_markup=remove_keyboard, parse_mode="Markdown")
    bot.send_message(message.chat.id, "*Якщо ти лікар, то тут ти можеш переглянути розклад своїх пацієнтів*", parse_mode="Markdown")
    ask_for_name(message)

# ! ask for name
def ask_for_name(message):
    # remove keyboard
    remove_keyboard = types.ReplyKeyboardRemove()
    msg = bot.send_message(message.chat.id, "Напиши мені своє *ім'я* та *прізвище*", parse_mode="Markdown", reply_markup=remove_keyboard)
    bot.register_next_step_handler(msg, verification)

# ! verification
def verification(message):
    # add inline
    markup_inline_yn = types.InlineKeyboardMarkup()
    item_yes = types.InlineKeyboardButton(text="Так", callback_data="yes")
    item_no = types.InlineKeyboardButton(text="Ні", callback_data="no")
    markup_inline_yn.add(item_yes, item_no)
    bot.send_message(message.chat.id, f"*Тебе звати {message.text}?*", reply_markup=markup_inline_yn, parse_mode="Markdown")
# ! verification_complete
@bot.callback_query_handler(func=lambda call: True)
def verification_complete(call):
    if call.data == "yes":
        # add keyboard
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item_change_name = types.KeyboardButton("✒️ Змінити ім'я")
        item_schedule = types.KeyboardButton("📰 Розклад")
        keyboard.add(item_change_name, item_schedule)
        bot.send_message(call.message.chat.id, "*Вибери, що робити далі*", reply_markup=keyboard, parse_mode="Markdown")
    elif call.data == "no":
        ask_for_name(call.message)
    # delete message
    # bot.delete_message(call.message.chat.id, call.message.message_id)

# ! buttons
@bot.message_handler(content_types=["text"])
def buttons(message):
    # ! change name
    if message.text == "✒️ Змінити ім'я":
        ask_for_name(message)
    # ! schedule
    elif message.text == "📰 Розклад":
        bot.send_message(message.chat.id, "*Розклад твоїх пацієнтів:*", parse_mode="Markdown")
        # example
        bot.send_message(message.chat.id, "Пацієнт 1")
        bot.send_message(message.chat.id, "Пацієнт 2")
        bot.send_message(message.chat.id, "Пацієнт 3")

# ! polling
bot.infinity_polling()