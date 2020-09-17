# def spiralTraverse(array):
#     result = []       
#     s_r, s_c, = 0, 0
#     e_r, e_c = len(array) - 1, len(array[0]) - 1
#     while s_r <= e_r and s_c <= e_c:
#         # asc row
#         for i in range(s_c, e_c + 1):
#             result.append(array[s_r][i])
#         # down col
#         for i in range(s_r + 1, e_r + 1):
#             result.append(array[i][e_c])
#         if s_r < e_r:
#             # desc row
#             for i in reversed(range(s_c, e_c)):
#                 result.append(array[e_r][i])
#         if s_c < e_c:
#             # up column
#             for i in reversed(range(s_r + 1, e_r)):
#                 result.append(array[i][s_c])
        
#         s_r += 1
#         s_c += 1
#         e_r -= 1
#         e_c -= 1
    
#     return result

def spiralTraverse(array):
    result = []       
    def helper(s_r, s_c, e_r, e_c):
        if s_r > e_r and s_c > e_c:
            return result
        for i in range(s_c, e_c + 1):
            result.append(array[s_r][i])
            # down col
        for i in range(s_r + 1, e_r + 1):
            result.append(array[i][e_c])
        if s_r < e_r:
            # desc row
            for i in reversed(range(s_c, e_c)):
                result.append(array[e_r][i])
        if s_c < e_c:
            # up column
            for i in reversed(range(s_r + 1, e_r)):
                result.append(array[i][s_c])

        s_r += 1
        s_c += 1
        e_r -= 1
        e_c -= 1 
        return helper(s_r, s_c, e_r, e_c)    
        
    s_r, s_c = 0, 0
    e_r, e_c = len(array) - 1, len(array[0]) - 1
    return helper(s_r, s_c, e_r, e_c)
        
res = spiralTraverse([[1, 2, 3, 4], [10, 11, 12, 5], [9, 8, 7, 6]])
# res = spiralTraverse([[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]])
print(res)