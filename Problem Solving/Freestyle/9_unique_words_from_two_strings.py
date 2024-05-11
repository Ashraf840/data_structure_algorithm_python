# Get unique chars of two strings in an iterable

x = 'Hello'
x_iterable = [i for i in x]
# print(x_iterable)

y = 'World'
y_iterable = [i for i in y]
# print(y_iterable)

x_iterable.extend(y_iterable)
# print(x_iterable)

# Remove duplicates
result = set(x_iterable)
print(result)