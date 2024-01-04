# Not Working


x = [3,10,4,2,1,2,6,1,7,2,9]
# count = 0
# while count <= len(x):
#     print(x[count])
#     count += 1

# [10, -1, 6, 6, 2, 6, 7, 7, -1, -1, -1]

# stack = [10,1,2,3,4]
stack = []
# print(len(stack))

for i in range(len(x), 0, -1):
    if len(stack):
        count = 0
        while count <= len(stack):
            if stack[-1] < x[i-1]:
                stack.pop()
            count += 1
        if len(stack):
            # if stack
            temp = x[i-1]
            x[i-1] = stack[-1]
            stack.append(temp)
        else:
            stack = x[i-1]
            x[i-1] = -1
    else:
        stack.append(x[i-1])
        x[i-1] = -1

    # # print(x[i-1])
    # # print(i-1)
    # if len(x):
    #     while x[i-1] > stack[-1]:
    #         stack.pop()
    #         if stack[-1] > x[i-1]:
    #             temp = x[i-1]
    #             x[i-1] = stack[-1]
    #             stack.append(x[i-1])
    #         else:
    #             x[i-1] = -1
    # else:
    #         x[i-1] = -1

    # # break


# print(stack[-1])
print(x)