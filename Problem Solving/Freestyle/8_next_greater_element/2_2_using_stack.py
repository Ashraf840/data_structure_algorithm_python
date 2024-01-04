# Working!!

x = [4,12,5,3,1,2,5,3,1,2,4,6]
# a = [12,-1,6,5,2,5,6,4,2,4,6,-1]

# print(len(x))

stack = []
# stack = [6,5,3,2]
# val = 6
# count = len(stack)-1
# while count >= 0:
#     # print(stack[count])
#     if val >= stack[count]:
#         stack.pop()
#     count -= 1

for i in range(len(x), 0, -1):
    # print(x[i-1])
    if len(stack):
        count = len(stack)-1
        while count >= 0:
            if x[i-1] >= stack[count]:
                stack.pop()
            count -= 1
        if len(stack):
            temp = x[i-1]
            x[i-1] = stack[-1]
            stack.append(temp)
        else:
            stack.append(x[i-1])
            x[i-1] = -1
    else:
        stack.append(x[i-1])
        x[i-1] = -1

print("x:", x)
print("stack:", stack)