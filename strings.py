# Assigning a string using single quotes
message = 'This is a simple string'
print(message)

# Assigning a string using double quotes
message = "This is a simple string"
print(message)

# Assigning a string using single quotes with double quotes in the midle
message = 'This is a "simple" string'
print(message)

# Escaping characters
message = 'This is a "simple"\n string with end of line'
print(message)

# Using raw strings
message = r'This is a "simple"\n string with end of line'
print(message)


# Using multiple lines
message = '''This is a "simple"
 string with \n end of line
 written in three lines
 '''
print(message)

# Concatenating strings
message = "Hello " + "world!"
print(message)

# Concatenating strings
message = "Hello "  "world!"
print(message)

# Repeating strings
message = "Hello " * 4 + 2 * 3 * "world!"
print(message)


# Indexing strings
message = "World"
print(message[0])
print(message[1])
print(message[2])
print(message[3])
print(message[4])
#print(message[5])

# Indexing string starting from last character
message = "World"
print(message[-1])
print(message[-2])
print(message[-3])
print(message[-4])
print(message[-5])

# Slice strings
message = "World"
print(message[1:3])
print(message[:3])
print(message[1:])
print(message[-3:])

# Length of string
message = "World"
print(len(message))



