elements = [5,9,2,1,67,34,88,34]    # Sorted Output: [1, 2, 5, 9, 34, 34, 67, 88]
# elements = [1,2,6,3,4,8,5]    # Sorted Output: [1, 2, 5, 9, 34, 34, 67, 88]
size = len(elements)   # output: 8
# print(size)
iterator,ifIterator,outerIter=0,0,0

for j in range(size):
    swapable=False
    # for i in range(size-1):
    for i in range(size-j-1):   # OPTIMIZATION
        if elements[i] > elements[i+1]:
            temp = elements[i]
            elements[i], elements[i+1] = elements[i+1], temp
            # ifIterator+=1
            swapable=True
        # iterator+=1
    # outerIter+=1
    if swapable == False:   # OPTIMIZATION
        break

# print(iterator, ifIterator, outerIter, elements)
print(elements)


"""
----------
Iterations
----------
Index   ->  0, 1, 2, 3, 4,  5,  6,  7
elements = [5, 9, 2, 1, 67, 34, 88, 34]

Inner: [5,2,1,9,34,67,34,88];  Outer - 0th (1)
swapable=False
Index   ->         0, 1, 2, 3, 4,  5,  6,  7
inner 0th (0,1):  [5, 9, 2, 1, 67, 34, 88, 34]; swapable=False, iterator=0
inner 1st (1,2):  [5, 2, 9, 1, 67, 34, 88, 34]; swapable=True, iterator=1
inner 2nd (2,3):  [5, 2, 1, 9, 67, 34, 88, 34]; swapable=True, iterator=2
inner 3rd (3,4):  [5, 2, 1, 9, 67, 34, 88, 34]; swapable=True, iterator=2
inner 4th (4,5):  [5, 2, 1, 9, 34, 67, 88, 34]; swapable=True, iterator=3
inner 5th (5,6):  [5, 2, 1, 9, 34, 67, 88, 34]; swapable=True, iterator=3
inner 6th (6,7):  [5, 2, 1, 9, 34, 67, 34, 88]; swapable=True, iterator=4

Inner: [2, 1, 5, 9, 34, 34, 67, 88]; Outer - 1st (2)
swapable=False
Index   ->         0, 1, 2, 3, 4,  5,  6,  7
inner 0th (0,1):  [2, 5, 1, 9, 34, 67, 34, 88]; swapable=True, iterator=5
inner 1st (1,2):  [2, 1, 5, 9, 34, 67, 34, 88]; swapable=True, iterator=6
inner 2nd (2,3):  [2, 1, 5, 9, 34, 67, 34, 88]; swapable=True, iterator=6
inner 3rd (3,4):  [2, 1, 5, 9, 34, 67, 34, 88]; swapable=True, iterator=6
inner 4th (4,5):  [2, 1, 5, 9, 34, 67, 34, 88]; swapable=True, iterator=6
inner 5th (5,6):  [2, 1, 5, 9, 34, 34, 67, 88]; swapable=True, iterator=7
inner 6th (6,7):  [2, 1, 5, 9, 34, 34, 67, 88]; swapable=True, iterator=7

Inner: [1, 2, 5, 9, 34, 34, 67, 88]; Outer - 2nd (3)
swapable=False
Index   ->         0, 1, 2, 3, 4,  5,  6,  7
inner 0th (0,1):  [1, 2, 5, 9, 34, 34, 67, 88]; swapable=True, iterator=8
inner 1st (1,2):  [1, 2, 5, 9, 34, 34, 67, 88]; swapable=True, iterator=8
inner 2nd (2,3):  [1, 2, 5, 9, 34, 34, 67, 88]; swapable=True, iterator=8
inner 3rd (3,4):  [1, 2, 5, 9, 34, 34, 67, 88]; swapable=True, iterator=8
inner 4th (4,5):  [1, 2, 5, 9, 34, 34, 67, 88]; swapable=True, iterator=8
inner 5th (5,6):  [1, 2, 5, 9, 34, 34, 67, 88]; swapable=True, iterator=8
inner 6th (6,7):  [1, 2, 5, 9, 34, 34, 67, 88]; swapable=True, iterator=8

Inner: [1, 2, 5, 9, 34, 34, 67, 88]; Outer - 3rd (4)
swapable=False
Index   ->         0, 1, 2, 3, 4,  5,  6,  7
inner 0th (0,1):  [1, 2, 5, 9, 34, 34, 67, 88]; swapable=False, iterator=8
inner 1st (1,2):  [1, 2, 5, 9, 34, 34, 67, 88]; swapable=False, iterator=8
inner 2nd (2,3):  [1, 2, 5, 9, 34, 34, 67, 88]; swapable=False, iterator=8
inner 3rd (3,4):  [1, 2, 5, 9, 34, 34, 67, 88]; swapable=False, iterator=8
inner 4th (4,5):  [1, 2, 5, 9, 34, 34, 67, 88]; swapable=False, iterator=8
inner 5th (5,6):  [1, 2, 5, 9, 34, 34, 67, 88]; swapable=False, iterator=8
inner 6th (6,7):  [1, 2, 5, 9, 34, 34, 67, 88]; swapable=False, iterator=8
"""
