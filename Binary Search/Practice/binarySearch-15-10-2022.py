list1 = [24,14,15,87,16,21]
list1.sort()
print(list1)
target = 24


def binary_search(listVal, target):
    left_index = 0
    right_index = len(listVal)
    mid_index = 0

    # struggle to execute a dry run
    while (left_index <= right_index):
        mid_index = (left_index + right_index) // 2
        mid_num = listVal[mid_index]    # forgot to find the mid_number

        if mid_num == target:
            return mid_index
        
        if mid_num < target:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1
    return -1


print((binary_search(listVal=list1, target=target)))
