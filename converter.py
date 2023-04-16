from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from api import convert

keyboard = [
        ['Рубль', 'Доллар'],
        ['Евро', 'Юань']
]


def pair(currency):
    pair_ans = keyboard[0][:] + keyboard[1][:]
    pair_ans.remove(currency)
    return [[f'{currency} - {item}'] for item in pair_ans]


async def start_converter(update, context):
    text = f'Здравствуйте {update.message.chat.full_name}!\n' \
           f'Это бот - Конвертер валют\n' \
           f'Выберите валюту, которую хотите сконвертировать.'
    await update.message.reply_text(text=text, reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True))
    return 1


async def choise_currency(update, context):
    context.user_data['валюта'] = update.message.text
    await update.message.reply_text(f'Вы выбрали {update.message.text} Выберите пару конвертации',
                                    reply_markup=ReplyKeyboardMarkup(pair(update.message.text), one_time_keyboard=True))
    return 2


async def get_ammout(update, context):
    context.user_data['пара'] = update.message.text.split(' - ')[1]
    await update.message.reply_text(f'Вы выбрали пару {update.message.text}\nВведите колличество.')
    return 3


async def converter_result(update, context):
    result = convert(context.user_data['валюта'], context.user_data['пара'], update.message.text)
    await update.message.reply_text(f'При текущем курсе {update.message.text} {context.user_data["валюта"]}\n'
                                    f'равен {result} {context.user_data["пара"]}.', reply_markup=ReplyKeyboardRemove)
    context.user_data.clear()



async def cancel(update, context):
    await update.message.reply_text('Завершение работы')
