elements = [5,9,2,1,67,34,88,34]
size = len(elements)
# print("List Size:",size)
iteration = 0


for i in range(size-1):
    # print(f"iteration: {iteration} -------", elements[i], "-------", elements[i+1])
    if elements[i] > elements[i+1]:
        elements[i], elements[i+1] = elements[i+1], elements[i]
        print("#"*50, "After Swapped")

    print(f"Iteration no-{iteration}", elements)
    iteration += 1




"""
[Concept]: The initial iteration is able to iterate the current index-value, simultaneously the next value. 
But at the last iteration as per the length, the current index-value will be accessed, but there will be no next index-value.
Thus the iteration needs to be looped to the 2nd last element's index.
"""
