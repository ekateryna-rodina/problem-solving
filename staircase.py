
def sol(m):
    memo = {}
    for i in range(0, m):
        count = num_ways(i)
    return count

def sol(m, set):
    memo = {}
    for i in range(0, m):
        count = num_ways(i)
    return count

def num_ways(n, memo = {}):
    if n == 0 or n == 1:
        memo[0] = 1
        memo[1] = 1
    else:
        count = memo[n-1] + memo[n-2]
        memo[n] = count

    return memo[n]

sol(5, {1, 3, 4})

