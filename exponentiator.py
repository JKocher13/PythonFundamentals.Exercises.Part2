def exponentiate(x,y):
	"""
	This function takes one returns the value of the first integer raised to the power of the second integer.
	"""
	return x**y

def  raise_to_fourth_power(x):
	"""
	"This function returns the value of an integer to the fourth power
	"""
	return exponentiate(x,4)

square = lambda x :x**2

cube = lambda x:exponentiate(x,3)

print(square(2))

print(cube(2))

print(raise_to_fourth_power(2))
