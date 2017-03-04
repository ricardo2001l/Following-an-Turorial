# This module of python has funtions for calculating thing of a circle

from math import pi


# Defining Funtions
def circle_perimeter(radio):
	""" This funtion calculates the perimeter of a circle, it ask for the radio as parameter,
this is the formula:

perimeter = 2 * pi * radio
"""
	radio = float(radio)# We convert the input in floating
	perimeter = 2 * pi * radio

	return format(perimeter, ".1f")# We give format to one floating point

def cicle_area(radio):
	""" This funtion calculates the area of a circle it ask for the radio as parameter,
this is the formula:

area = pi * radio ** 2
"""
	radio = float(radio)# We convert the input in floating, again
	area = pi * radio ** 2 # We can too uses parenthesis, but this will work

	return format(area, ".1f")# We give format to one floating point


''' Callingg Funtions '''
# Perimeter
radio = input("Input the radio of the circle: ")
result_per = circle_perimeter(radio)

# Area
result_ar = cicle_area(radio)# We don't define again the "radio" so we had deined it before


""" Printing """
print("Perimetro:", result_per + "cm")
print("Area:", result_ar + "cm2")