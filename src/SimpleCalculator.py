#simple calculator
numVar = float(input("Enter you first variable, for eg: 67.9 or 6 "))
numVar2 = float(input("Enter you second variable, for eg: 67.9 or 6 "))

operation = input("Enter your choice in the prompt (add, sub, mul,div, mod) for eg: add ")

print("A Simple Calculator!!!")

if(operation == "add"):
	print("Addition")
	print("Add Results: ",(numVar + numVar2))

elif (operation == "sub"):
	print("Subtraction")
	print("Sub Results: ",(numVar - numVar2))

elif (operation == "mul"):
	print("Multiply")
	print("Mul Results: ",(numVar * numVar2))

elif (operation == "div"):
	print("Division")
	if(numVar2 != 0):
		print("Divide Results: ",(numVar / numVar2))
	else:
		print("Error ZeroDivisionError: float division by zero!")
		print("run again with positive value")

elif (operation == "mod"):
	print("Modulos")
	print("Mod Results: ",(numVar % numVar2))

else:
	print("Invalid operation")


#Add, Multiple, Sub, Divide, Modulos










