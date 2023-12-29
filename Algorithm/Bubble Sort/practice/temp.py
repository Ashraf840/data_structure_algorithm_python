x = [5,3,8,6,7,2]

# for i in range(0, len(x)):
#     print(x[i])

# Good visual representation
for i in range(len(x), 0, -1):
    print("i", i, end=" --> ")
    for j in range(0, i):
        print("j:", j, end=" ")
    print()
