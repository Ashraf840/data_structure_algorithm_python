def binary_search(number_list, target_value):
    left_index = 0
    right_index = len(number_list) - 1 
    mid_index = 0

    # iterate through all the list-elems
    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = number_list[mid_index]

        # return the mid_index (eventually of the targeted value)
        if mid_number == target_value:
            return mid_index
        
        # mid_value is less than the target_value
        if mid_number < target_value:
            # reset the left index of the list
            left_index = mid_index + 1
        # mid_value is greater than the target_value
        else:
            # reset the right index of the list
            right_index = mid_index - 1
        
    # if the target_value is not inside the list, return -1
    return -1


number_list = [12,15,17,19,21,24,45,67]

target_num = 44

result_bns = binary_search(number_list=number_list, target_value=target_num)
print(f'The targeted value is in the index (Binary Search): {result_bns}')



# [Cons]
# This application is not capable of handling the unsorted elements in the list.

# [Note]: Time complexity is not measured. Need to implement in 100k elems
