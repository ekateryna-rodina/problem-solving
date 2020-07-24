# This problem was asked by Amazon.

# Given an array of numbers, find the maximum sum of any contiguous subarray of the array.

# For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.

# Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.

# Do this in O(N) time.

# questtions:
# could be positives and negatives there?
# strsightforward n^2(wit caching) and n^3(no cache)
# answer is dynamic programming and subproblems
# at which index best performance
# make a choice on each step - what sum is max - element by itself or element + previous sum
def max_sum(arr_):
    result = 0
    max_ = 0
    for i in range(0, len(arr_)):
        # make a choice take previous sum + or just current
        max_ = max(max_ + arr_[i], arr_[i])
        if max_ == max_ + arr_[i]:
            #  current + previious sum is max -> continue array
            continue
        #else start new
        result = max(result, max_)
    return result
max_sum([34, -50, 42, 14, -5, 86])

# Kadane's algorithm
def max_sum(arr_):
    max_so_far = arr_[0]
    max_ending_here = 0
    for i in range(0, len(arr_)):
        # make a choice take previous sum + or just current
            #  current + previious sum is max -> continue array
        max_ending_here = max_ending_here + arr_[i]
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
        elif max_ending_here < 0:
            max_ending_here = 0
    return max_so_far
max_sum([34, -50, 42, 14, -5, 86])
