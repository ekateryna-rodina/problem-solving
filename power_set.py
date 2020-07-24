# The power set of a set is the set of all its subsets. 
# Write a function that, given a set, generates its power set.

# For example, given the set {1, 2, 3}, it should 
# return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

# You may also use a list or array to represent a set.

def p(l):
    if not l: return [[]]
    return p(l[1:]) + [[l[0]] + x for x in p(l[1:])]

def power_set(l):
    if not l: return [[]]
    minus_one = l[1:]
    element = l[0]
    return p(minus_one) + [[element] + x for x in p(minus_one)]


def power_set2(orig, new_):
    if orig == []:
        return [new_]
    else:
        res = []
        for s in power_set2(orig[1:], new_ + [orig[0]]):
            res.append(s)
        for k in power_set2(orig[1:], new_ ):
            res.append(k)
    return res

kk = power_set2([1, 2, 3], [])
print(kk)





# Possible questions to ask the interviewer — 

# Could the solution set contain duplicate subsets? (Ans: No)
# Can we print the subset in any order? (Ans: Yes)
# Backtracking and Bitmasking solutions
# Backtracking Approach - It's a recursive approach where we backtrack each solution after appending the subset to the resultset.
# BitMasking Approach - The binary representation of a number in range 0 to 2^n is used as a mask where the index of set bit represents the array index to be included in the subset.
# 1. Backtracking Approach
# Solution idea
# Why Backtracking? Because the backtracking technique is designed to generate every possible solution once. If we design the algorithm smartly, we can get the backtracking logic to work for us and generate all the possible subsets.

# The thought is that if we have N number of elements inside an array, we have exactly two choices for each of them, either we include that element in our subset or we do not include it. So, the take or not take strategy builds a pseudo-binary tree of choices returning only the leaves for each combination resulting in the powerset.

# The recursion tree for the above example will look like this:


# Solution steps
# We could just build up the subset of different size in an array i.e. subset[]. Here are the steps to generate it:

# Choose one element from input i.e. subset[len] = S[pos]. We can decide to include it in current subset or not.
# Recursively form subset including it i.e. allSubsets(pos+1, len+1, subset)
# Recursively form subset excluding it i.e. allSubsets(pos+1, len, subset)
# Make sure to generate each set once.
# Pseudo Code
# int S[N]
# void allSubsets(int pos, int len, int[] subset) 
# {
#   if(pos == N) 
#   { 
#      print(subset)
#      return
#   }
#   // Try the current element in the subset.
#   subset[len] = S[pos]
#   allSubsets(pos+1, len+1, subset)
#   // Skip the current element.
#   allSubsets(pos+1, len, subset)
# }
# Complexity Analysis
# Here we are generating every subset using recursion. The total number of subsets of a given set of size n = 2^n.

# Time Complexity :  O( 2^n)

# Space Complexity :  O(n) for extra array subset.

# Critical Ideas to Think
# Why are we keeping track of both the cases when we pick the element and when we don't pick the element?
# Can you write the recurrence relation for the above algorithm?
# Can you think of some different way to implement this solution?
# Can we solve this problem using stack?
# Identify problems which can be solved using similar approach.