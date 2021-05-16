# Dictionaries

# Create a dictionary
b = dict()
b['key1'] = 23
print(b)

# Create more instances
b['temp'] = 23
b['hum'] = 95
b['press'] = 1000

print(b)

# Change one instance to a string
b['press'] =  'data string'
print(b)

# Delete element
del b['key1']
print(b)
