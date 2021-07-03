# Working with lists

# Lists can contain both numbers and strings
a = list()
a.append(12)
print(a)

# Append a number in the last position of the vector
a.append(34)
print(a)

# Append a string
a.append("hello")
print(a)

# The first element of the list
print(a[0])

# The last element of the list
print(a[-1])

# The first elements
print(a[0:2])

# Adding more elements
a.append("qwerty")
a.append(56)
a.append(578)

# Show the last two elements with reverse order
print(a)
print(a[-1:3:-1])

# The penultimate element of the list
print(a[-2])
