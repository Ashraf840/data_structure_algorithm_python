roman_numeral = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}

user_input = 'MCMXCIV'
user_input_list = list(user_input)

last = 'I'   # The comparision-checking using the hashMap will throw an error, if this variable is left as an empty variable.
result = 0

for i in user_input_list[::-1]:
    if roman_numeral[i] < roman_numeral[last]:
        result -= roman_numeral[i]
    else:
        result += roman_numeral[i]
    # print(f"{i}: {roman_numeral[i]}")
    last = i

# print("last:", last)
print("result:", result)
