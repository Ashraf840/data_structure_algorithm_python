# Six ways to add element at the beginning of the list
# 1. By using "insert()" method.
# 2. By concatenating two lists together. The single elem which will be added at the beginning of the list needs to be converted into a single-elem-list before concatenation.
# 3. By using "append()" method of the single element (converted to single-elem-list) while inside a for-loop whose iteration number will be determined on the other list-length.
# 4. By using "extend()" method of the single elem which is intended to be appended at the beginning of the list.
# 5. By using the "pop(0)" method w/ specific index & concatenate to another list.
# 6. Using list slicing by array[0:0], which creates a subsequence from the original sequence (list, array) add add the new element at the beginning of the list.

single_elem = 1
arr1 = [2,3,4,5]
arr2 = [2,3,4,5]
arr3 = [2,3,4,5]
arr4 = [2,3,4,5]
arr5 = [2,3,4,5]
arr6 = [2,3,4,5]

# Method-1
arr1.insert(0, single_elem)
print("arr1:", arr1)

# Method-2
print("arr2:", [single_elem] + arr2)

# Method-3
single_elem_list1 = [single_elem]
for i in arr3:
    single_elem_list1.append(i)
print("arr3:", single_elem_list1)

# Method-4
single_elem_list2 = [single_elem]
single_elem_list2.extend(arr4)
print("arr4:", single_elem_list2)

# Method-5
single_elem_list3 = [single_elem]
for i in range(len(arr5)):
    # print(f"Popping out index: {i}", arr5.pop(0))
    single_elem_list3 += [arr5.pop(0)]
print("arr5:", single_elem_list3)

# Method-6
arr6[0:0] = [1]     # Using list-slicing, which creates a subsequence and after assigning an solo list into that subsequence, the subsequence automatically merged to the original list.
print("arr6:", arr6)
