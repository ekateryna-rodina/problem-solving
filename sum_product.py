
# sum 1
# def recursive_sum(array, index, sum_):
#     if index == -1:
#         return sum_
#     summ = sum_ + array[index]
#     next_index = index + 1 if index < len(array) - 1 else -1
#     return recursive_sum(array, next_index, summ)
# # type check
# def recursive_sum(array, index, sum_):
#     if index == -1:
#         return sum_
#     type_ = type(array[index])
#     next_index = index + 1 if index < len(array) - 1 else -1
#     summ = sum_ + array[index] if type_ == int else sum_ + recursive_sum(array[index], 0, 0)
#     return recursive_sum(array, next_index, summ)
# level
def recursive_sum(array, index, sum_, level_):
    if index == -1:
        return sum_*level_
    type_ = type(array[index])
    next_index = index + 1 if index < len(array) - 1 else -1
    summ = sum_ + array[index] if type_ == int else sum_ + recursive_sum(array[index], 0, 0, (level_ + 1))
    return recursive_sum(array, next_index, summ, level_)


