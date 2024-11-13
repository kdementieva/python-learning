# import os
# import telebot
# import random
# from telebot import types
#
# bot = telebot.TeleBot(os.getenv('token'))
#
# scores = {}
#
# YOU_WIN = 'Ты выиграл! Счет: {bot_wins} : {user_wins}'
# BOT_WINS = 'Я выиграл! Счет: {bot_wins} : {user_wins}'
# DRAW = 'Ничья! Счет: {bot_wins} : {user_wins}'
#
# @bot.message_handler(commands=["start"])
# def start(m):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     KeyboardButton1 = types.KeyboardButton('Камень')
#     KeyboardButton2 = types.KeyboardButton('Ножницы')
#     KeyboardButton3 = types.KeyboardButton('Бумага')
#     markup.add(KeyboardButton1, KeyboardButton2, KeyboardButton3)
#
#     user_id = m.chat.id
#     if user_id not in scores:
#         scores[user_id] = {'bot_wins': 0, 'user_wins': 0}
#
#     bot.send_message(m.chat.id, 'Нажми кнопку и начни игру ', reply_markup=markup)
#
#
# @bot.message_handler(content_types=["text"])
# def handle_text(message):
#     user_id = message.chat.id
#
#     if user_id not in scores:
#         scores[user_id] = {'bot_wins': 0, 'user_wins': 0}
#     bot_wins = scores[user_id]['bot_wins']
#     user_wins = scores[user_id]['user_wins']
#
#     bot_answers = ['Камень', 'Ножницы', 'Бумага']
#     bot_choice = random.choice(bot_answers)
#
#     user_choice = message.text
#     bot.send_message(message.chat.id, bot_choice)
#
#     if user_choice == bot_choice:
#         bot.send_message(
#             chat_id=message.chat.id,
#             text=DRAW.format(bot_wins = bot_wins, user_wins = user_wins)
#         )
#     elif (user_choice == 'Камень' and bot_choice == 'Ножницы') or \
#          (user_choice == 'Ножницы' and bot_choice == 'Бумага') or \
#          (user_choice == 'Бумага' and bot_choice == 'Камень'):
#         user_wins += 1
#         scores[user_id]['user_wins'] = user_wins
#         bot.send_message(
#             chat_id=message.chat.id,
#             text=YOU_WIN.format(bot_wins=bot_wins, user_wins=user_wins)
#         )
#     else:
#         bot_wins += 1
#         scores[user_id]['bot_wins'] = bot_wins
#         bot.send_message(
#             chat_id=message.chat.id,
#             text = BOT_WINS.format(bot_wins = bot_wins, user_wins = user_wins)
#         )
#
# bot.polling(none_stop=True, interval=0)
