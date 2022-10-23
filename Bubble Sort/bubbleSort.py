elements = [5,9,2,1,67,34,88,34]
size = len(elements)
# print("List Size:",size)
iteration = 0

print(f"Original list: {elements}")
for i in range(size-1):
    for j in range(size-1-i):
        # print(f"iteration: {iteration} -------", elements[i], "-------", elements[i+1])
        print(f"Current Inner-Loop Iteration: {j}")
        if elements[j] > elements[j+1]:
            elements[j], elements[j+1] = elements[j+1], elements[j]
            print("#"*50, "After Swapped")
        print(f"Iteration no-{iteration}", elements)
        iteration += 1
    print()




"""
[Concept]: 
The initial iteration is able to iterate the current index-value, simultaneously the next value. 
But at the last iteration as per the length, the current index-value will be accessed, but there will be no next index-value.
Thus the iteration needs to be looped to the 2nd last element's index.

[Efficiency]
The inner-loop is basically comparing the current & the consecutive value then swapping the values regarding the comparison if required.
Each complete cycle of the inner-loop moves the highest number to the end. 
Thus, after completing each inner-loop cycle, it doesn't require to re-visit the end-index for comparison since it holds the biggest number by that time.

Since each inner-loop is responsible for nudging each biggest number right to the end to its appropriate position, 
this inner-loop required to be looped till the (list_length-1) times.
AND EVERYTIME EACH INNER-LOOP IS NUDGING THE BIGGEST NUMBER TO THE END, DECREASE THE LIST LENGTH COUNT BY 1 INTO LOOP-RANGE AFTER EVERY COMPLETION OF INNER-LOOP.
"""
