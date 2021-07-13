import requests
import json
from time import sleep

valoratual = 0

while True:
    valor = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')
    valor = valor.json()
    cotacao = valor['USDBRL']["bid"]
    cotacao = float(cotacao)
    if valoratual == 0:
        valoratual = cotacao
        print(f'Iniciando monitoramento! Valor atual é de R$ {valoratual}')
    if cotacao > valoratual:
        print(f'Dolar subiu! Valor atual R$ {cotacao}')
    elif cotacao < valoratual:
        print(f'Dolar baixou! Valor atual R$ {cotacao}')
    valoratual = cotacao
    sleep(30)
    
