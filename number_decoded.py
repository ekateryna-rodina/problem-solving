# This problem was asked by Facebook.

# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

# You can assume that the messages are decodable. For example, '001' is not allowed.

def helper(str_,k, memo):
    if k == 0:
        return 1
    s = len(str_)-k
    if str_[s] == '0':
        return 0
    if k in memo:
        return memo[k]
    result = helper(str_, k-1, memo)
    if k >= 2 and int(str_[s:s+2]) < 26:
        result+=helper(str_, k-2, memo)
    memo[k] = result
    return result
def count_ways(str_):
    memo = {}
    return helper(str_, len(str_), memo)

number = count_ways('1234567')
print(number)


    
