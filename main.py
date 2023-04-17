from telegram.ext import Application
from bot_functions import *
from config import token


if __name__ == '__main__':
    app = Application.builder().token(token).build()  # Построение бота используя Application
    app.add_handler(CommandHandler('values', values))  # Отлов команды /values
    app.add_handler(CommandHandler('help', help))  # Отлов команды /help
    app.add_handler(converter)  # Отлов команды /start. Запуск диалога
    app.add_handler(CommandHandler('cancel', cancel_err))  # Отлов команды /cancel вне диалога
    app.run_polling()  # Запуск бота
