import telebot


bot = telebot.TeleBot('5998134435:AAEuhTLHqd5FGtzIpiVaOu8KfVnIoqlTpyQ')


@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    bot.send_message(message.chat.id, f'Здравствуйте {message.chat.first_name}')
    print(123)
















if __name__ == '__main__':
    bot.polling(none_stop=True)