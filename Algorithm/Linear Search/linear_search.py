def linear_search(number_list, target_value):
    # access the values & indecies of the list
    for index, value in enumerate(number_list):
        # retunr from the loop if the value is equals to the targeted value
        if value == target_value:
            return index
    return -1


number_list = [12,15,17,19,21,24,45,67]

target_num = 450

result_linear_search = linear_search(number_list=number_list, target_value=target_num)
print(f'The targeted value is in the index (Linear Search): {result_linear_search}')