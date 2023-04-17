import requests
import json
from config import api_key


D = {'Рубль': 'RUB', 'Доллар': 'USD', 'Евро': 'EUR', 'Юань': 'CNY'}  # словарь валют и их символов для запроса


def convert(cur_from, cur_to, amount: int):
    url = f'https://currate.ru/api/?get=rates&pairs={D[cur_from]}{D[cur_to]}&key={api_key}'
    payload = {}
    response = requests.request("GET", url, data=payload)
    data = json.loads(response.content)['data']
    # Возврат округленного до 2ух значения умножения переданного колличества входящей валюты на множитель из запроса
    return round(float(amount) * float(data[f'{D[cur_from]}{D[cur_to]}']), 2)

