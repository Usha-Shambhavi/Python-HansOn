def countConsonants(text):
	
	vowels = "aeiou"
	count = 0

	for letter in text.lower():
		if letter not in vowels:
			count += 1
	return count


print(countConsonants("The quick brown fox jump over a lazy dog"))
print(countConsonants("hello world!"))
