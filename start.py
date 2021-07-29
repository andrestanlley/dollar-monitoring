import requests
import json
from time import sleep

valoratual = 0

while True:
    valor = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')
    valor = valor.json()
    cotacao = float(valor['USDBRL']["bid"])
    cotacao = f'{cotacao:.2f}'
    hora = valor['USDBRL']["create_date"].split()
    hora = hora[1]
    if valoratual == 0:
        valoratual = cotacao
        print(f'[{hora}] Iniciando monitoramento! Valor atual é de R$ {valoratual}')
    if cotacao > valoratual:
        print(f'[{hora}] Dolar subiu! Valor atual R$ {cotacao}')
    elif cotacao < valoratual:
        print(f'[{hora}] Dolar baixou! Valor atual R$ {cotacao}')
    valoratual = cotacao
    sleep(30)