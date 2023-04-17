from telegram import InlineKeyboardButton as Button
from telegram import InlineKeyboardMarkup as Markup
from telegram.ext import ConversationHandler
from api import convert, D

cyrrency_list = ['Рубль', 'Доллар', 'Евро', 'Юань']  # Список валют


def __pair(currency):  # Команда сбора списка пар конвертации для выбранной валюты
    pair_ans = cyrrency_list[:]
    pair_ans.remove(currency)
    pair_ans = [f'{currency} - {item}' for item in pair_ans]
    for item in pair_ans:
        yield item


async def start_converter(update, context):  # Старт диалога. Обработка команды /start
    text = f'Здравствуйте {update.message.chat.full_name}!\n' \
           f'Это бот - Конвертер валют\n' \
           f'Выберите валюту, которую хотите сконвертировать.'
    await update.message.reply_text(text=text, reply_markup=Markup([
        [
            Button(cyrrency_list[0], callback_data=cyrrency_list[0]),
            Button(cyrrency_list[1], callback_data=cyrrency_list[1])
        ],
        [
            Button(cyrrency_list[2], callback_data=cyrrency_list[2]),
            Button(cyrrency_list[3], callback_data=cyrrency_list[3])
        ]
    ]))
    return 1


async def choise_currency(update, context):  # 2ая ступень диалога. Запись callback_data в user_data и печать пар
    context.user_data['валюта'] = update.callback_query.data
    await context.application.bot.send_message(update.callback_query.message.chat_id,
                                               f'Вы выбрали {update.callback_query.data} Выберите пару конвертации',
            reply_markup=Markup([[Button(pairr, callback_data=pairr)] for pairr in __pair(update.callback_query.data)]))
    return 2


async def get_ammout(update, context):  # 3ая ступень диалога. Запись пары и вывод запроса колличества.
    context.user_data['пара'] = update.callback_query.data.split(' - ')[1]
    await context.application.bot.send_message(update.callback_query.message.chat_id,
                                               f'Вы выбрали пару {update.callback_query.data}\nВведите колличество.')
    return 3


# Последняя часть диалога. Попытка преобразования в число, Если да то отправка API запроса конвертации, вывод
# результата, очистка user_data, закрытие диалога если нет, то ответ пользователю и ожидание следующего сообщения.
async def converter_result(update, context):
    try:
        float(update.message.text)
    except ValueError:
        await update.message.reply_text('Ошибка. Вы ввели не число.\nПопробуйте еще раз')
    else:
        result = convert(context.user_data['валюта'], context.user_data['пара'], update.message.text)
        await update.message.reply_text(f'При текущем курсе {update.message.text} {D[context.user_data["валюта"]]} '
                                        f'равен {result} {D[context.user_data["пара"]]}.')
        context.user_data.clear()
        return ConversationHandler.END


async def cancel(update, context):  # Обработка команды /cancel внутри диалога
    await update.message.reply_text('Завершение работы')
    return ConversationHandler.END
