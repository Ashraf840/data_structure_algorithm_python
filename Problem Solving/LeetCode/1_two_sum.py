x = [1,2,3,4,5,6,7]

target = 5

resultIndex = []

hashMap = {}

for (i, n) in enumerate(x):
    diff = target - n
    if diff in hashMap:
        resultIndex = [hashMap[diff], i]
        break   # When it'll be in a function, it doesn't require a break, instead directly return the found list
    hashMap[n] = i


print(resultIndex)









# # print(len(x))

# stopIteration = False

# for i in range(0, len(x)):
#     print(x[i], end=": ")
#     if not stopIteration:
#         for j in range(0, len(x)):
#             if x[i] + x[j] == target:
#                 print(f"First index: {x[i]}; Second index: {x[j]}")
#                 # result = [x[i]] + [x[j]]
#                 stopIteration = True
#                 break
#             print(x[j], end=", ")
#         print()


# # print(result)