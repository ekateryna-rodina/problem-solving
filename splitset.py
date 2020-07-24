# This problem was asked by Facebook.

# Given a multiset of integers, return whether it can be partitioned into 
# two subsets whose sums are the same.

# For example, given the multiset {15, 5, 20, 10, 35, 15, 10}, it would return true, 
# since we can split it up into {15, 5, 10, 15, 10} and {20, 35}, which both add up to 55.

# Given the multiset {15, 5, 20, 10, 35}, it would return false, since we 
# can't split it up into two subsets that add up to the same sum.

def can_partition(set_):
    sum_ = sum(set_)
    if sum_ % 2 != 0:
        return False
    return can_partition_recursive(set_, sum_, 0)
def can_partition_recursive(set_, sum_, current_index):
    # base case
    if sum_ == 0:
        return True
    len_ = len(set_)
    if len_ == 0 or current_index > len_:
        return False
    # include into a set and check if number doesn't exeed sum by ittself
    if set_[current_index] <= sum_:
        if can_partition_recursive(set_, sum_ - set_[current_index], current_index + 1):
            return True
    return can_partition_recursive(set_, sum_, current_index + 1)

print(can_partition([15, 5, 20, 10, 35, 15, 10]))
print(can_partition([15, 5, 20, 10, 35]))

# more efficient
def can_partition_(set_):
    sum_ = sum(set_)
    if sum_ % 2 != 0:
        return False
    # create 2-dimensional array 
    dp = [[-1 for x in range(int(sum_/2)+1)] for y in range(len(set_))]
    return True if can_partition_recursive(dp, set_, int(sum_/2), 0) == 1 else False
def can_partition_recursive(arr_, set_, sum_, current_index):
    # base case
    if sum_ == 0:
        return 1
    len_ = len(set_)
    if len_ == 0 or current_index > len_ - 1:
        return 0
    # if we havve not already processed similar problem
    if arr_[current_index][sum_] == -1:
        # include into a set and check if number doesn't exeed sum by ittself
        if set_[current_index] <= sum_:
            if can_partition_recursive(arr_, set_, sum_ - set_[current_index], current_index + 1) == 1:
                arr_[current_index][sum_] = 1
                return 1
        # recursive call after excluding item
        arr_[current_index][sum_] =  can_partition_recursive(arr_, set_, sum_, current_index + 1)
    return arr_[current_index][sum_]

print(can_partition_([15, 5, 20, 10, 35, 15, 10]))
# print(can_partition([15, 5, 20, 10, 35]))

