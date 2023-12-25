x = [1,2,3,4,5,6,7,8,9]
y = []

# # Approach-1
# # Pop & push to another list from the previous list
# for i in range(0, len(x)):
#     y.append(x.pop())
# print(y)


# Approach-2
# Convert the list into deque object then execute the pop-push operations
from collections import deque
x_deque = deque(x)

for i in range(0, len(x_deque)):
    y.append(x_deque.pop())

print(y)