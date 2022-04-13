# assigning binary search in recussive
def binary_search_recusive(number_list, target_value, left_index=0, right_index=0):
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
        # handling 'RecursionError' (2nd phase), if out of range
        if mid_index >= len(number_list)-1:
            return -1



        # reset the left index of the list to the (mid_index-1) & the right_index will be the (len(number_list) - 1)
        # print('Mid Number (mid_number < target_value): ', mid_number)
        right_index = len(number_list) - 1
        return binary_search_recusive(number_list, target_value, left_index=mid_index+1, right_index=right_index)
    
    if mid_number > target_value:
        # handling 'RecursionError' (2nd phase), if out of range
        if mid_index <= left_index:
            return -1

        # reset the right_index of the list to the (mid_index-1) & the left_index will be 0
        print('Mid Number: ', mid_number)
        return binary_search_recusive(number_list, target_value, left_index=0, right_index=mid_index-1)
        pass
    

number_list = [12,15,17,19,21,24,45,67]

target_num = 15

result_bns_recurssion = binary_search_recusive(number_list=number_list, target_value=target_num)
print(f'The targeted value is in the index (Binary Search): {result_bns_recurssion}')

