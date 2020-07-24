import time

def constant(arr_):
    return 1 + arr_[0]
def summ(arr_):
    return sum(arr_)
def pairs(arr_):
    result = []
    for i in range(0, len(arr_)):
        for j in range(i + 1, len(arr_)):
            result.append([arr_[i], arr_[j]])
    return result

start = time.time()
constant([1, 2, 3, 4])
end = time.time()
print(end - start)

start = time.time()
summ([1, 2, 3, 4])
end = time.time()
print(end - start)


start = time.time()
pairs([1, 2, 3, 4])
end = time.time()
print(end - start)
# [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]