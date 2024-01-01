# Six ways of adding elements at the beginning of a string
# 1. By concatenating two strings togather maintaining the correct order.
# 2. By using f-string interpolation.
# 3. By using the "%" operator into string interpolation.
# 4. By using the "str.format" into string interpolation.
# 5. By converting string into list. Thus we can use all the ways from the "1_....py" file. Additionally, rejoin the list element at the end.
# 6. By using 'rjust' method


string = '123456'
elem = '+'

# Method-1
print("String concatenation: ", elem + string)

# Method-2
print(f"'f-string' interpolation: {elem}{string}")

# Method-3
print("'%%s' operator: %s%s"%(elem, string))

# Method-4
print("str.format: {}{}".format(elem, string))

# Method-5,1
string_list = list(string)
string_list.insert(0, elem)
temp1 = ''.join(string_list)
print('Convert into list (5.1):', temp1)

# Method-5.2
string_list = list(string)
elem_list = list(elem)
result1 = elem_list + string_list
temp2 = ''.join(result1)
print("list concatenation:", temp2)

# Method-5.3
string_list = list(string)
elem_list = list(elem)
for i in string_list:
    elem_list.append(i)
temp3 = ''.join(elem_list)
print("Using the combination of for-loop & append method:", temp3)

# Method-5.4
string_list = list(string)
elem_list = list(elem)
for i in range(len(string_list)):
    elem_list += string_list.pop(0)
temp = ''.join(elem_list)
print("Using the pop method:", temp)

# Method-5.5
string_list = list(string)
elem_list = list(elem)
elem_list.extend(string_list)
temp = ''.join(elem_list)
print("Using the extend method:", temp)

# Method-5.6
string_list = list(string)
elem_list = list(elem)
string_list[0:0] = elem_list
temp = ''.join(string_list)
print("By using the string slicing to create a subsequence from the sequence:", temp)

# Method-6
print("Using the rjust method:", string.rjust(len(string)+1, '+'))