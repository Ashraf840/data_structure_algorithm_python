# Return the index from the list if found the target value
def linear_search(var_lsit, target):
    for index, val in enumerate(var_lsit):
        if val == target:
            print(index, val)
            return index
    return -1

var_list = [142,12,43,47,45,26,47,38,59,108]
target = 59
index = linear_search(var_list, target)
if index != -1:
    print(f"Searched result index: {index}")
else:
    print("Not found!")
