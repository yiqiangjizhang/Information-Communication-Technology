# This code prompts the user for a number and tell if the number is even or not

for i in range(0,10):
    number = input("Enter a number: ")
    new_number = int(number)

    if new_number % 2 == 0:
        print("The number is even")
    else: 
        print("The number is odd")

