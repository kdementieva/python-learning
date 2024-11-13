import os
import telebot
import random
import glob

bot = telebot.TeleBot(os.getenv('token'))

image_folder_path = 'mems'
image_files = glob.glob(os.path.join(image_folder_path, '*.jpg'))

GET_MEME_COMMAND ='mem'
START_MESSAGE = f'Привет! Я бот, который отправляет мемы. Для получения мема, используй команду /{GET_MEME_COMMAND} '
EMPTY_FILE = 'Извините, мемы не найдены!'
NO_IMAGES = 'Извините, мемы закончились! Начинаем сначала.'

sent_images = []

@bot.message_handler(commands=["start"])
def start(m):
    bot.send_message(m.chat.id, text = START_MESSAGE )

@bot.message_handler(commands=[GET_MEME_COMMAND])
def send_mem(message):
    if not image_files:
        bot.send_message(message.chat.id, text = EMPTY_FILE )
        return
    available_img = list(set(image_files) - set(sent_images))
    if not available_img:
        bot.send_message(message.chat.id, text = NO_IMAGES )
        sent_images.clear()
        available_img = image_files
    random_image = random.choice(available_img)
    with open(random_image, 'rb') as photo:
        bot.send_photo(message.chat.id, photo)
        sent_images.append(random_image)


bot.polling(none_stop=True)