from urllib.request import urlopen
import json

class ExchangeClient:

    def __init__(self, base):
        self.base = base
        self.URL = 'https://api.exchangeratesapi.io/latest?base=' + self.base
        self.rates = {}
        self.date = self.getDate()
        self.rates = self.getRates()

    def getDate(self):
        response = urlopen(self.URL)
        rates = json.loads(response.read())
        return rates['date']

    def getRates(self):
        response = urlopen(self.URL)
        rates = json.loads(response.read())
        return rates['rates']

    def convert(self, cantidad, baseDest):
        return cantidad * self.rates[baseDest]

    def convertDate(self):
        return self.date

ficheroEntrada = open('./divisas.txt', 'r')
ficheroSalida = open('./ahorros.txt', 'a')
conversor = ExchangeClient('EUR')
suma = 0
for linea in ficheroEntrada:
    datos = linea.split(', ')
    suma += conversor.convert(int(datos[1]), datos[0])
ficheroSalida.write('{}\t | {}\n'.format(conversor.convertDate(), suma))

ficheroEntrada.close()
ficheroSalida.close()