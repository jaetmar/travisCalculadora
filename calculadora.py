import math

class Calculadora(object):

	def __init__(self):
		self.resultado = 0
	
	def obtener_resultado(self):
		return self.resultado

	def sumar(self, n1, n2):
		try:
			if type(n1) in (int, float) and type(n2) in (int, float):
				self.resultado = n1 + n2
			else:
				self.resultado = 'Datos Incorrectos'
		except:
			self.resultado = 'Datos Incorrectos'

	def restar(self, n1, n2):
		try:
			if type(n1) in (int, float) and type(n2) in (int, float):
				self.resultado = n1 - n2
			else:
				self.resultado = 'Datos Incorrectos'
		except:
			self.resultado = 'Datos Incorrectos'

	def multiplicar(self, n1, n2):
		try:
			if type(n1) in (int, float) and type(n2) in (int, float):
				self.resultado = n1 * n2
			else:
				self.resultado = 'Datos Incorrectos'
		except:
			self.resultado = 'Datos Incorrectos'

	def dividir(self, n1, n2):
		try:
			if n1 == 0 and n2 == 0:
				self.resultado = 'Indeterminado'
				return
			elif n2 == 0:
				self.resultado = 'Infinito'
				return

			if type(n1) in (int, float) and type(n2) in (int, float):
				self.resultado =  n1 / n2
				return
			else:
				self.resultado =  'Datos Incorrectos'
				return
		except:
			self.resultado =  'Datos Incorrectos'

	def potencia(self, n1, n2):
		try:
			if type(n1) in (int, float) and type(n2) in (int, float):
				self.resultado = n1 ** n2
			else:
				self.resultado = 'Datos Incorrectos'
		except:
			self.resultado = 'Datos Incorrectos'

	def raiz(self, n1, n2):
		try:
			if type(n1) in (int, float) and type(n2) in (int, float):
				self.resultado = n1 ** (1 / n2)
			else:
				self.resultado = 'Datos Incorrectos'
		except:
			self.resultado = 'Datos Incorrectos'