# Given an array of integers and a number k, where 1 <= k <= length of the array, 
# compute the maximum values of each subarray of length k.

# For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

# 10 = max(10, 5, 2)
# 7 = max(5, 2, 7)
# 8 = max(2, 7, 8)
# 8 = max(7, 8, 7)
# # Do this in O(n) time and O(k) space. You can modify the input array in-place and you do 
# not need to store the results. You can simply print them out as you compute them.
# inner loops O(n*k)
def print_max1(input, k):
    ak = []
    len_ = len(input)
    for i in range(len_ - k + 1):
        max_ = input[i]
        for j in range(1, k):
            max_ = max(input[i + j], max_)
        ak.append(max_)
    return ak

# mm = print_max1([10, 5, 2, 7, 8, 7], 3)
# print(mm)
# self balanced binary O(n)
from collections import deque
def print_max2(input, k):
    res = [] 
    n = len(input)
    # createt a douvle ended queue which will store useful indeces 
    qi = deque()
    # process first window of elements
    for i in range(k):
        # for eveery element the previous feewer elleementt is useleess so remove itt from queuee
        while qi and input[i] >= input[qi[-1]]:
            qi.pop()
        qi.append(i)
    # process rest of elements
    for i in range(k, n):
        # remove elements which are out of the winndow
        res.append(input[qi[-1]])
        while qi and qi[0] <= i-k:
            # remove from front of dequeue
            res.append(qi.popleft())
        # remove all elements which are less then currently added item
        while qi and input[i] >= input[qi[-1]]:
            qi.pop()
        qi.append(i)
    return res
mm = print_max2([10, 3, 11, 7, 8, 7], 3)