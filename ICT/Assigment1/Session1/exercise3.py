# Write a program that shows the divisors of an introduced number

# Prompt user to introduce an integer
number = int(input("Introduce an integer: "))

# Create an empty list
divisors = []

# Calculate divisors
for i in range(1,number):
    div = number % i
    if div == 0:
        divisors.append(i)

# Print
print("Your number was " + str(number) + " " + "and its divisors are: ")
# Print divisors
print(divisors)
