#Password Strength

def checkPassword(text):
	if(len(text) < 8):
		return "Weak"
	has_letter = any(c.isalpha() for c in text)
	has_number = any(c.isdigit() for c in text)

	if(has_letter and has_number):
		return "moderate strong"

	else:
		return "Invalid"