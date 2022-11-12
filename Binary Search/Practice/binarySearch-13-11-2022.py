list_var = [24,14,15,87,16,21]
list_var.sort()
print(list_var)
left_index=0
right_index=len(list_var)-1   # len() starts counting from 1; thus substract 1 from total lenght
target=16

while left_index <= right_index:
    middle_index=(left_index+right_index)//2
    middle_value=list_var[middle_index]
    if target == middle_value:
        print("Result index:",middle_index)
    
    if middle_value < target:
        left_index = middle_index+1
    else:
        right_index = middle_index-1

