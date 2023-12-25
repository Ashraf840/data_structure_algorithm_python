original = 3985
reversed_num = 0

# Run a loop untill the number is greater than zero
while original > 0:
    temp = original % 10    # Read the last digit from the number in every iteration & store into a temporary variable
    reversed_num = reversed_num * 10 + temp
    original = original // 10   # It'll remove the last digit from the number in every iteration

print(reversed_num)