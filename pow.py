# This problem was asked by Google.

# Implement integer exponentiation. That is, implement the pow(x, y) function, where x and y are integers and returns x^y.

# Do this faster than the naive method of repeated multiplication.

# For example, pow(2, 10) should return 1024.

def pow(number, power):
    if power == 1:
        return number
    if power == 0:
        return 1
    result = pow(number, int(power/2))
    if power % 2 == 0:
        return result * result
    else:       
        return number * result * result

print(pow(2, 10))