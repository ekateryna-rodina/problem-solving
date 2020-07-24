# Given an array of integers, return a new array such that each element at index i of the new array is 
# the product of all the numbers in the original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], 
# the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

# Follow-up: what if you can't use division?

def find_products(arr):
    left =  [None]*len(arr)
    right = [None]*len(arr)
    new_arr = [None]*len(arr)
    pointer = 0
    array_len = len(arr)
    for l in range(0, array_len):
        if l == 0:
            left[l] = 1
        else:
            left[l] = left[l - 1]*arr[l - 1]
    for r in range(array_len - 1, -1, -1):
        if r == array_len - 1:
            right[r] = 1
        else:
            right[r] = right[r + 1]*arr[r + 1]
    while pointer < array_len:
        new_arr[pointer] = left[pointer]*right[pointer]
        pointer = pointer + 1
    return new_arr
find_products([1, 2, 3, 4, 5])
