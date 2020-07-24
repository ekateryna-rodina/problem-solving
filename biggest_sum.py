# This problem was asked by Airbnb.

# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. 
# Numbers can be 0 or negative.

# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, 
# since we pick 5 and 5.

# Follow-up: Can you do this in O(N) time and constant space?

def get_largest_sum(arr):
    # using dynamic programming to solve this problem
    incl_ = 0
    excl_ = 0
    for i in arr:
        temp_incl_ = incl_
        incl_ = max(incl_, i + excl_)
        excl_ = temp_incl_
    
    return incl_

pr = get_largest_sum([2, 4, 6, 2, 5])
print(pr)