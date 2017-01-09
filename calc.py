import re


print('Python Calculator')
print('Type clear to start a new calculation')
print('Type operator to see list of equation operators')
print('Type quit to exit\n')

previous = 0
run = True


def perform_math():
	global run
	global previous
	equation = ""
	if previous == 0:
		equation = input('Enter Equation:')
	else:
		equation = input(str(previous))

	if equation == 'quit':
		print('Goodbye')
		run = False
	elif equation == 'clear':
		previous = 0
	elif equation == 'operator':
		print('+ = addition\n - = subtraction\n * = multiplication\n / = division\n % = modular division\n ** = exponent\n // = floor division\n')		
	else:
		equation = re.sub('[a-zA-Z,.:()" "]', '', equation)
		if previous == 0:
			previous = eval(equation)
		else:
			previous = eval(str(previous) + equation)


while run:
	perform_math()
