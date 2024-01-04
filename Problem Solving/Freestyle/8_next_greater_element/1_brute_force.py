x = [3,10,4,2,1,2,6,1,7,2,9]

result = []

isGreater = False

for i in range(len(x)):
    for j in range(i+1, len(x)-1):
        if x[i] < x[j]:
            isGreater = True
            break
    if isGreater:
        isGreater = False
        result.append(x[j])
    else:
        result.append(-1)
print(result)

# Time Complexity; O(n^2) since a nested loop is being executed.