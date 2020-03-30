class Carro(object):

	# Define o consumo em litros por 1Km
	def __init__(self, consumo):
		self.consumo = consumo
		self.combustivel = 0

	# Define o método mover
	def mover(self,km):
        consumo = self.consumo * km
        self.combustivel -= consumo


	# Define o método gasolina
	def gasolina(self):
		return self.combustivel

	# Define o método abastecer
	def abastecer(self, combustivel):
		self.combustivel += combustivel

# Executando
def main():
	fusca = Carro(10)
	fusca.abastecer(100)
	fusca.mover(5)
	print(fusca.gasolina())


if __name__ == '__main__':
	main()
