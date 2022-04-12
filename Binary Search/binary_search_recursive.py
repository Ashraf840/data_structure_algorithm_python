# assigning binary search in recussive
def binary_seach_recusive(number_list, target_value, left_index=0, right_index=0):
    # left_index = 0
    # right_index = len(number_list) - 1
    # mid_index = 0
    mid_index = (left_index + right_index) // 2
    mid_number = number_list[mid_index]

    # print(mid_index, '----', mid_number)

    # return the mid_index (eventually of the targeted value)
    if mid_number == target_value:
        return mid_index

    if mid_number < target_value:
        # reset the left index of the list
        return binary_seach_recusive(left_index=mid_index+1, right_index = len(number_list) - 1)
    
    if mid_number > target_value:
        # reset the right index of the list
        return binary_seach_recusive(right_index=mid_index-1, right_index = len(number_list) - 1)
        pass
    pass



number_list = [12,15,17,19,21,24,45,67]

target_num = 45

result_bns_recurssion = binary_seach_recusive(number_list=number_list, target_value=target_num)
print(f'The targeted value is in the index (Binary Search): {result_bns_recurssion}')

