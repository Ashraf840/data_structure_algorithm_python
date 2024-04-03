# Problem Ref: https://www.hackerrank.com/challenges/list-comprehensions

x=1
y=1
z=2
n=3

# Uncomment to understand the flow
# for i in range(x+1):
#     print("value of x:", i)
#     for j in range(y+1):
#         print("value of y:", j)
#         for k in range(z+1):
#             print("value of z:", k)
#             print()


# List of Possible Coordinates
# for i in range(x+1):
#     for j in range(y+1):
#         for k in range(z+1):
#             print(i, j, k)


# Show only the coordinates whose sum is not equal to 3
# for i in range(x+1):
#     for j in range(y+1):
#         for k in range(z+1):
#             if i + j + k != 3:
#                 print(i, j, k)


# Apply list comprehension
print([[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n])

