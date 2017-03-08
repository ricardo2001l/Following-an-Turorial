""" This proyect has a class that calculates the value of an unity to other """

class Covert(object):

	def __init__(self, value, unity1="cm", unity2="in", measure="length"):
		self.value = value
		self.unity1 = unity1
		self.unity2 = unity2
		self.measure= measure

	def calculate(self, value, measure):# arreglar para que al no pasar argumentos a este metodo
		# se usen los del metodo __init__ recuerda: es para crear juegos ;)
		measure=measure.lower()

		# The greater poupuse if done: calculate from cm to in and upside down :)
		if measure == "length":
			if unity1 == "cm" and unity2 == "in":
				total = value * 0.393701
				return total
			elif unity2 == "cm" and unity1 == "in":
				total = value * 2.54
				return total

		# for mass
		elif value == "mass":
			if unity1 == "kg" and unity2 == "gr":
				total = value * 1000
			elif unity2 == "kg" and unity1 == "gr":
				total = value * 0.001

		# and other that are not defined, i can add some more like area, angles, data...
		elif value == "volume":
			pass

		elif value == "time":
			pass

		elif value == "temperature":
			pass


# we take input from user
value = float(input("Quantity: "))

length = Covert(value, unity1, unity2, measure)
print(length.calculate(value, measure))