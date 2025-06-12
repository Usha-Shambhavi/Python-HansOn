def toUpper(text):
	return text.upper()


def replaceText(text, replaceText, keyword):
	return text.strip().replace(replaceText, keyword)

def reverseString():
	strV = "The Text"
	rev = "".join(reversed(strV))
	print(rev)

reverseString()

print(replaceText("The quick brown fox jump over a lazy dog", "dog", "cat"))

print(toUpper("The quick brown fox jump over a lazy dog"))