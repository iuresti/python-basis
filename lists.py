# defining a list
integers = [1, 2, 3, 4]
print (integers)

# Indexing a list
integers = [1, 2, 3, 4]
print (integers[0])
print (integers[1])
print (integers[2])
print (integers[3])


# Indexing a list from the end
integers = [1, 2, 3, 4]
print (integers[-1])
print (integers[-2])
print (integers[-3])
print (integers[-4])

# Slicing a list
integers = [1, 2, 3, 4]
print (integers[1:3])


# Concatenating lists
integers = [1, 2, 3, 4]
moreIntegers = [5, 6, 7, 8]
print (integers + moreIntegers)

# Changing an element
integers = [1, 2, 3, 4]
integers[2] = 10
print (integers)


# Using append
integers = [1, 2, 3, 4]
integers.append(8)
print (integers)

# Assign to slice
integers = [1, 2, 3, 4]
integers[1:3] = [6, 7, 8, 9]
print (integers)

# Knowing list length
integers = [1, 2, 3, 4]
print (len(integers))