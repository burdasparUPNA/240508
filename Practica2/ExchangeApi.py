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

ficheroEntrada = open('./ficheroEntrada.txt', 'r')
ficheroSalida = open('./ficheroSalida.txt', 'w')
ficheroSalida.write('Fecha\t\t | Total\n')
conversor = ExchangeClient('EUR')
for linea in ficheroEntrada:
    datos = linea.split(', ')
    ficheroSalida.write('{}\t | {}\n'.format(conversor.convertDate(), conversor.convert(int(datos[1]), datos[0])))

ficheroEntrada.close()
ficheroSalida.close()