# Check if a word is a palindrome or not

# Function
def isPalindrome(str):
    # Run loop from 0 to len/2
    for i in range(0, int(len(word)/2)):
        if word[i] != word[len(word)-i-1]:
            return False
    return True

# Prompt user to introduce a word
word = str(input("Enter a word: "))

if isPalindrome(word)==True :
    print("The word " + word + " is a palindrome")
else:
    print("The word " + word + " is NOT a palindrome")