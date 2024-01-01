# string = '[()[{()}]]'     # Variant-1
# string = '[()'              # Variant-2
# string = '[(()]'              # Variant-3
string = ']()'              # Variant-4
string_list = list(string)

opening_brackets = ['(', '{', '[']
closing_brackets = [')', '}', ']']
matching_hashMap = {
    '(': ')',
    '{': '}',
    '[': ']',
}

stack = []

isBalanced = True

for i in string_list:
    if i in opening_brackets:
        stack.append(i)
    if i in closing_brackets:
        # If find any closing bracket at the very beginning, then firstly check if the stack is not empty before making any pop-operation on it.
        if len(stack) != 0:
            stack_pop = stack.pop()
            # print("stack pop:", stack_pop)
            # print(stack_pop, ":matching pair:", matching_hashMap[stack_pop])
            # break
            if matching_hashMap[stack_pop] != i:
                # print(f"{stack_pop} ----- {matching_hashMap[stack_pop]}")
                isBalanced = False
                break
        else:
            isBalanced = False
            break
    # print(i)

if isBalanced and len(stack) == 0:
    print("String is a balanced brackets!")
else:
    print("String is not a balanced brackets!")

# print(stack)
