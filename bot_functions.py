

TODO: 'Написать инлайн клавиатуру, выбор пар обменника. Обработчик каллбаков. Библиотека python-telegram-bot'


async def start_command(update, context):
    await update.message.reply_text(f'Добрый день {update.message.chat.full_name}! Ваш чат ид = {update.message.chat.id}')

