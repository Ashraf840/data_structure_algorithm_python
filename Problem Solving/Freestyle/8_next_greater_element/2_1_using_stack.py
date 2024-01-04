# Not Working


x = [4,12,5,3,1,2,5,3,1,2,4,6]
# a = [12,-1,6,5,2,5,6,4,2,4,6,-1]

stack = []

# stack = [6,3,2,4]
# y=6
# count = len(stack)-1
# while count >= 0:
#     if y > stack[count]:
#         stack.pop()
#     count -= 1


for i in range(len(x), 0, -1):
    # print(x[i-1])
    if len(stack):
        count = len(stack)-1
        while count >= 0:
            if x[i-1] > stack[count]:
                stack.pop()
            count -= 1
        if len(stack):
            temp = x[i-1]
            # print(temp)
            # if stack[-1] < x[i-1]: 
            x[i-1] = stack[-1]
            stack.append(temp)
        else:
            stack.append(x[i-1])
            x[i-1] = -1
        # break
    else:
        stack.append(x[i-1])
        x[i-1] = -1


print("x:", x)
print("stack:", stack)
