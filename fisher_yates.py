# Given a function that generates perfectly random numbers between 1 and k (inclusive), 
# where k is an input, write a function that shuffles a deck of cards represented as an array using only swaps.

# It should run in O(N) time.

# Hint: Make sure each one of the 52! permutations of the deck is equally likely.
# using Fisher–Yates shuffle alg
from random import randint
def shuffle(arr_):
    for i in range(len(arr_) - 1, -1, -1):
        rand_index = randint(0, i)
        temp = arr_[rand_index]
        arr_[rand_index] = arr_[i]
        arr_[i] = temp
    return arr_
print(shuffle([1, 2, 3, 4, 5, 6, 7, 8]))