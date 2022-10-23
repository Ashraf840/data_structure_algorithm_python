"""
Bubble sort a name list alphabetically in ascending order
"""


list_var = ['Johnson','Smith','Williams','John','Andy','Joe']
size = len(list_var)
total_iteration = 0

for i in range(size-1):
    print(f'Outer Iteration:{i}')
    print()
    for j in range(size-1-i):
        # print(f'Inner iteartion:{j}', '-------', list_var[j], '-------', list_var[j+1])
        if list_var[j] > list_var[j+1]:
            list_var[j], list_var[j+1] = list_var[j+1], list_var[j]
        print(list_var)
        total_iteration += 1
    print()

print(f'Sorted list:{list_var}')
print(f'Total Iteration:{total_iteration}')