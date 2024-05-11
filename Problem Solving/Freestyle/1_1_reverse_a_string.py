# Different types of reversing

name = "Bro Code"

# Reverse a string using string slicing indexing
name[::-1]

# Get the last string from each word using split & string slicing indexing
result = []
for word in name.split(" "):
  result.append(word[-1])
print(result)

# Reverse the word from the string literal (eg. Code Bro)
splitted = name.split(" ")
reversed = splitted[::-1]
result = " ".join(reversed)
result