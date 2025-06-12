
print("Welcome to prime number check!")

varNum = int(input("Enter the number to check prime?"))

for i in range(2, varNum):
	if (varNum % i == 0):
		print("Is is a prime")
		break
	else:
		print("It's not a prime")
		break