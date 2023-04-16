import requests
import json


def convert(cur_from, cur_to, amount):
    D = {'Рубль': 'RUB', 'Доллар': 'USD', 'Евро': 'EUR', 'Юань': 'CNY'}
    url = f"https://api.apilayer.com/fixer/convert?to={D[cur_to]}&from={D[cur_from]}&amount={amount}"
    payload = {}
    headers = {
      "apikey": 'I0I7g0homYpzaA037a0jvULmQ84U5cjs'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    return json.loads(response.content)['result']

