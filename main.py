from telegram.ext import Application, CommandHandler, ConversationHandler, MessageHandler, filters
from bot_functions import *


if __name__ == '__main__':
    app = Application.builder().token('5998134435:AAEuhTLHqd5FGtzIpiVaOu8KfVnIoqlTpyQ').build()
    app.add_handler(converter)
    app.run_polling()
