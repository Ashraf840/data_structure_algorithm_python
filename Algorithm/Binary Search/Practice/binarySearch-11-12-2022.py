def findIndex(arr, n):
    left_index=0
    right_index=len(arr)-1
    middle_index=0
    while(left_index <= right_index):
        middle_index = (left_index+right_index)//2
        middle_num = arr[middle_index]
        if middle_num == n:
            print(middle_num)
            return middle_index
        if middle_num < n:
            left_index = middle_index+1
        else:
            right_index = middle_index-1
    return -1



number_list = [12,15,17,19,21,24,45,67]
target_num = 17
x = findIndex(arr=number_list, n=target_num)
print(x)