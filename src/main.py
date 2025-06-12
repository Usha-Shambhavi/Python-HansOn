import passwordStrength
import palindrome
import oddEven



#Password check
print(passwordStrength.checkPassword("IndiaVictory2"))


#Palindrome check
varText = input("Enter the text to validate is it a Palindrome or not?")


print("Entered text is it Palindrome?: ", palindrome.isItPalindrome(varText))

#oddEven
print(oddEven.oddEven(500))