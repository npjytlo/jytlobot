import telebot
bot = telebot.TeleBot('1816182854:AAHqu-TDZ_9ZZbTnglW-jDybb63wgn3qVOk')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f'Я бот. Радий знайомству, {message.from_user.first_name}')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Привіт!')
    else:
        bot.send_message(message.from_user.id, 'Не розумію, що це означає.')

  bot.polling(none_stop=True)  