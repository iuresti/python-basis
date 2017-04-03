# For each
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

# Using range
for i in range(5):
    print(i)

# Setting start point, end point and increment
for i in range(20, 100, 5):
    print(i)


# Using indices
words = ['cat', 'window', 'defenestrate']
for index in range(len(words)):
    print(index, words[index])