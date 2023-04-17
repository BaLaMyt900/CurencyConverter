from telegram.ext import CommandHandler, MessageHandler, filters, CallbackQueryHandler
from converter import *
from warnings import filterwarnings
from telegram.warnings import PTBUserWarning

# Фильтрация предупреждения в ConversationHandler
filterwarnings(action="ignore", message=r".*CallbackQueryHandler", category=PTBUserWarning)


async def help(update, context):  # Команда /help
    await update.message.reply_text('Бот работает в режиме диалога. После команды /start\n'
                                    'он начнет диалог и будет предлагать ответы. В конце\n'
                                    'Вы получите стоимость сконвертированной валюты.\n'
                                    'Для получения доступных валют, введите /values\n'
                                    'Для преждевременного выхода из диалога, введите /cancel.')


async def values(update, context):  # Команда /values
    await update.message.reply_text('Список доступных валют:\n'
                                   '1) Рубль\n2) Доллар\n3) Евро\n4) Юань')


async def cancel_err(update, context):  # Отлов команды /cancel вне диалога
    await update.message.reply_text('Ошибка.\nДиалог не запущен.')


converter = ConversationHandler(  # Сборка команды /start
    entry_points=[CommandHandler('start', start_converter)],
    states={
        1: [CallbackQueryHandler(choise_currency)],
        2: [CallbackQueryHandler(get_ammout)],
        3: [MessageHandler(filters.TEXT, converter_result)]
        },
    fallbacks=[CommandHandler('cancel', cancel)],
    block=False
)






