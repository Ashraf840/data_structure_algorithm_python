# rni = roman_number_index
rni = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}
# print(rni['I'])

# user_input = input("Enter a roman number: ")
user_input = 'XXIVII'
user_input_list = list(user_input)

print(user_input_list)
# print(user_input_list[::-1])

# for i in user_input:
#     print(f'{i}: {rni[i]}')

result = 0
# last = ''     # If I leavs it empty, then the check inside the for-loop will throw an error
last = 'I'      # Thus, I defined with the smallest unit of the roman number


for i in user_input_list[::-1]:
    if rni[i] < rni[last]:
        result -= rni[i]
    else:
        result += rni[i]
    # print(rni[i])
    last = i
    # print(last)

print(result)
# for ui in range(len(user_input_list), 0, -1):
#     # print(user_input_list[ui-1])
#     temp = user_input_list[ui-1]
#     temp2 = user_input_list[ui-2]

#     # # Check if temp variable is holding 'V' or 'X', then inside if-block check if the current iteration is holsing 'I', then subtract 1 from the current result.
#     # if temp == "V" or temp == "X":
#     #     if user_input_list[ui] == "I":
#     #         print("Subtract 1 from the total value")
#     # print(temp, temp2)