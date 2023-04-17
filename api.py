import requests
import json


D = {'Рубль': 'RUB', 'Доллар': 'USD', 'Евро': 'EUR', 'Юань': 'CNY'}

def convert(cur_from, cur_to, amount: int):
    # url = f"https://api.apilayer.com/fixer/convert?to={D[cur_to]}&from={D[cur_from]}&amount={amount}"
    url = f'https://currate.ru/api/?get=rates&pairs={D[cur_from]}{D[cur_to]}&key=dad5895f3e8060395348a5310ca8f846'
    payload = {}
    # headers = {
    #   "apikey": 'I0I7g0homYpzaA037a0jvULmQ84U5cjs'
    # }
    response = requests.request("GET", url, data=payload)
    data = json.loads(response.content)['data']
    return round(float(amount) * float(data[f'{D[cur_from]}{D[cur_to]}']), 2)

