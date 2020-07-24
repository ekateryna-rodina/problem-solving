# This problem was asked by Facebook.

# Given an unordered list of flights taken by someone, each represented as 
# (origin, destination) pairs, and a starting airport, compute the person's itinerary. 
# If no such itinerary exists, return null. If there are multiple possible itineraries, 
# return the lexicographically smallest one. All flights must be used in the itinerary.

# For example, given the list of flights [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')] 
# and starting airport 'YUL', you should return the list ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].

# Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')] 
# and starting airport 'COM', you should return null.

# Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')] 
# and starting airport 'A', you should return the list ['A', 'B', 'C', 'A', 'C'] 
# even though ['A', 'C', 'A', 'B', 'C'] is also a valid itinerary. 
# However, the first one is lexicographically smaller.
# BACTRACKING
def get_itinerary(flights, current_itinerary):
    # base case rreeturn itinerary
    if not flights:
        return current_itinerary
    last_stop = current_itinerary[-1]
    for i, (origin, destination) in enumerate(flights):
        flights_minus_current = flights[:i] + flights[i + 1:]
        current_itinerary.append(destination)
        if last_stop == origin:
            return get_itinerary(flights_minus_current, current_itinerary)
        current_itinerary.pop()
    return None
import collections
def get_itiner(tickts, start):
    if not tickts:
        return None
    tickts_dic = collections.defaultdict(list)
    for from_, to_ in tickts:
        tickts_dic[from_].append(to_)
    itinerary = [start]
    # send a partial source
    # all other params are global
    # with this approach wee need to understand what to push inside the list 
    # and what to put, and call dfs recurcively
    def dfs(src):
        # base case
        # itinerary list will be tickets pairs plus one
        if len(itinerary) == len(tickts) + 1:
            return True
        # get all destinations from last point
        destinations = sorted(tickts_dic[src])
        for destionation in destinations:
            # peerform bactracking
            # remove destinattion from dictionary 
            # and append itt later
            # 1. Make a change
            # 2. Recurse
            # 3. Undo the change
            itinerary.append(destionation)
            if destionation in tickts_dic[src]:
                tickts_dic[src].remove(destionation)
            # recurcively call first degree function
            if dfs(destionation):
                return
            
            tickts_dic[src].append(destionation)
            itinerary.pop()
    # we know the start
    dfs(start)
    return itinerary

res = get_itiner([('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')], 'A')
print(res)


# 1. what choice u do
# 2 where to stop followingg cerrtain path - constraints
# 3 our goal
# 
# A R
# 1 year ago (edited)
# The way I think of backtracking is as follows:

# 1. Make a change
# 2. Recurse
# 3. Undo the change

# If at any point we reach the goal state, return true/print/whatever.

# - So for the sudoku problem: For all possible squares on the board see if we can add any value between 1-9. If we can, add the value and recurse for the rest of the board. Then undo the changes by making the board blank again. Goal state is when we have successfully filled in last square

# - For n queens: Iterate through the first row. If we can place a queen at a given column place it and recurse for the remaining rows. Then undo the change by removing the queen and moving to the next column. Goal is when we have placed queen on nth row

# - Print all possible permutations: Initialize an empty String for results. In the input string iterate through each character. For each character, remove it from input and add it to result and recurse. Then remove the character from result and insert it back in same position in input string. Goal is when result size = n.

# - Given n print all sets of valid parentheses that amount to n: Start with blank input string and 2 numbers i, j initialized to n that denote number of opening/closing parentheses remaining - you can add opening parentheses to the string if i>0. You can add closing parentheses if j>i. If you can add opening parentheses, add it to stringbuilder, recurse and then remove it from end of stringbuilder. If you can add closing parentheses add it to stringbuilder, recurse and then remove it from end of stringbuilder. Goal is when both i, j =0.


# - Print all subsets of a set: For each character in set, remove it from input set add it to result set and if it has not been printed already, print (goal is any set that has not been printed already). Then recurse for remaining elements. Then remove element from result set and add it back to input set.

