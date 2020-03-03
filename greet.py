def greet (name):
	"""
	This function creates the greeting
	"""
	print ("Hello " + name)

def name_input():
	"""
	This is a function that asks your name
	"""
	name  = input("What is your name?")
	return name

greet(name_input())

