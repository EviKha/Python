while  True:
	print("Options")
	print("Enter 'add' to add two numbers")
	print("Enter 'substract' to substract two numbers")
	print("Enter 'multiply' to mutliply two numbers")
	print("Enter'divide'to divide  two numbers")
	print("Enter'quit'to end the program")
	num1=float(input("Enter a number:"))
	num2=float(input("Enter another number:"))
	user_input = input(":")
	if user_input == "quit":
		break
	elif user_input == "add":
		result = str (num1+num2)
		print("The answer is" + result)
	elif user_input == "substract":
		result = str (num1-num2)
		print("The answer is" + result)
	elif user_input == "multiply":
		result = str (num1*num2)
		print("The answer is" + result)
	elif user_input == "divide":
		result = str (num1/num2)
		print("The answer is" + result)
else:
	print("Unknown input")