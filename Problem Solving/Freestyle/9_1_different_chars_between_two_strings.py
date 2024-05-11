"""
Task: Find out different characters between two strings; If there is any different chars betwen two strings then return a list of characters into lowercased. Otherwise return -1
x = "Hello"
y = "World"
Different Chars: ["H", "e", "W", "r", "d"]
"""

x = "Hello"
y = "World"

# Make a list of characters out of those words
x_iterable = [i for i in x]
y_iterable = [i for i in y]

# Subtract the common element from first & second, make a vice versa. Finally, we can get the different chars between to sets
result1 = set(x_iterable) - set(y_iterable)
result2 = set(y_iterable) - set(x_iterable)

result = result1 | result2

# Convert the set into a list
result = list(result)

print(result)