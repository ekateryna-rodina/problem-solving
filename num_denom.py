def minNumberOfCoinsForChange(n, denoms):
#     create map
    nums = {k: float('inf') for k in range(n+1)}
    nums[0] = 0
    for den in denoms:
        for t_d in nums.keys():
            if den <= t_d:
                r_ = t_d - den 
                new_c_n = nums[r_] + 1
                nums[t_d] = min(nums[t_d], new_c_n)
    return nums[n] if nums[n] != float('inf') else -1

print(minNumberOfCoinsForChange(7, [2, 4]))