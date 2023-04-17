from telegram.ext import ConversationHandler, CommandHandler, MessageHandler, filters, CallbackQueryHandler
from converter import *

TODO:  'Библиотека python-telegram-bot'


def __to_unpack(update, context):  # Распаковка объектов бот и сообщение из полученных аргументов
    if update.callback_query:
        return context.application.bot, update.callback_query
    else:
        return context.application.bot, update.message


converter = ConversationHandler(
    entry_points=[CommandHandler('start', start_converter)],
    states={
        1: [CallbackQueryHandler(choise_currency)],
        2: [CallbackQueryHandler(get_ammout)],
        3: [MessageHandler(filters.TEXT, converter_result)]
        },
    fallbacks=[CommandHandler('cancel', cancel)]
)






