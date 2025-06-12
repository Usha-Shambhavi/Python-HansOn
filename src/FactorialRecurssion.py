
# Using Recurssion
def factorial(num):
	if num == 0 or num ==1:
		return 1
	#recursssion
	return num * factorial(num - 1)

num = int(input("Enter the number"))
if(num <0):
	print("Number cannot be zero!")
else:
	print("factorial of a number is : ",factorial(num))


# Using Loop
num = int(input("Enter the number"))

if num == 0:
	print("Number cannot be zero!")

result =1
for i in range(1, num+1):
	result *= i

print("factorial of a number is : ",result)

#5 * 4 * 3 * 2 * 1 = 120