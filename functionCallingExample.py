def rectangle(l,b):
	return l * b

def rectangleLength(b, area):
	return area / b


def rectangleP(l,b):
	return 2*(l + b)



def rectangle(l,b,area,indicator):
	if indicator == 'a':
		return l * b
	elif indicator == 'l':
		if b ==0:
			print("You need to pass positive value for breadth")
			return
		else:
			return area/b
	elif indicator == 'p':
		return 2*(l + b)
	else:
		print("Wrong indicator")



print("Area of the rectangle is: ",rectangle(67,5,0,'a'))
print("Length of the rectangle is: ",rectangle(0,67,rectangle(67,5,0,'a'),'l'))
print("Perimeter of the rectangle is: ",rectangle(rectangle(0,67,335,'l'),67,335,'p'))
