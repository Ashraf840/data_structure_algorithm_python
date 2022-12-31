# The stack data structure is a linear data structure that accompanies a principle known as LIFO (Last In/First Out) or FILO (First In/Last Out).
# Using list to construct & use "stack" data structure is not recommended.
# Performed Operations on Stack: push, pop, isEmpty, peek/top
# "Stack" doesn't exist in Python by default, but we can implement "stack" data structure using the following ways:
#   1# List     2# Collection/deque     3# queue/LifoQueue

stack = []
# "Push" operation
for i in range(10, 110, 10):
    stack.append(i)

# "Pop" operation
stack.pop()

# "isEmpty" operation
print(len(stack)==0)
print(not stack)

# "Peek/Top" operation
print(stack[-1])
