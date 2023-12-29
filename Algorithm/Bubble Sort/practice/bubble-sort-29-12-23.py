# There are 4 core conpets of bubble sort
# 1. Swapping only the bigger number to the next index, while traversing the iterable.
# 2. In each inner iteration, the number of traversing element should be decremented by 1.
# 3. The outer iteration will determine the number of inner iteration's traversal number.
# 4. If the outer for-loop traverse in a descending order, then the inner for-loop will get the actual decremental-type iteration number for traversing based on each iteration of the outer for-loop.
# 5. The outer for-loop should start a number less than the actual length of the array.

"""
Make this pattern first:
5 3 8 6 7 
5 3 8 6 
5 3 8 
5 3 
5 
"""

nums = [5, 3, 8, 6, 7, 2]

def sort(nums: list()) -> list():
    for i in range(len(nums)-1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
            # print(nums[j], end=" ")
    return nums


nums = sort(nums)
print(nums)
