#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

# Bonus: Can you do this in one pass?

def is_sum_exists(arr, k):
    pointer = 0
    is_sum_exists = False
    while pointer < len(arr) - 1:
        for i in arr[pointer+1:]:
            if arr[pointer] + i == k:
                return True
        pointer = pointer + 1
    return is_sum_exists

result = is_sum_exists([10, 15, 4, 7], 22)
print(result)

def is_sum_exists_(arr, k):
    b = 0
    e = len(arr) - 1
    while b < e:
        if arr[b] + arr[e] == k:
            return True
        elif arr[b] + arr[e] < k:
            b = b + 1
        elif arr[b] + arr[e] > k:
            e = e - 1
    return False

result = is_sum_exists_([10, 15, 4, 7], 19)
print(result)
            
