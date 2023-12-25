# Raise query by ownself; then found an article: https://www.geeksforgeeks.org/program-count-digits-integer-3-different-methods/

original = 3985
count = 0

# # Approach-1 (Time Complexity: O(n))
# # Run a loop untill the number is reduced to not equal to zero
# while original != 0:
#     count += 1
#     original = original // 10
# print(count)


# Approach-2 (Time Complexity: O(1))
# Convert into string & then count the length of the string
original_string = str(original)
print(len(original_string))

