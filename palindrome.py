#palindrome

#eg. MADAM

def reverseString(text):
	return "".join(reversed(text))

def isItPalindrome(text):
	if(text.lower() == reverseString(text).lower()):
		return True
	else:
		return False