def romanToInteger(s: str) -> int:
    roman_numeral = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    user_input_list = list(s)

    result = 0
    lastRoman = 'I'

    for i in user_input_list[::-1]:
        if roman_numeral[i] < roman_numeral[lastRoman]:
            result -= roman_numeral[i]
        else:
            result += roman_numeral[i]
        lastRoman = i
    
    return result
    

result = romanToInteger('MCMXCIV')
print(result)
