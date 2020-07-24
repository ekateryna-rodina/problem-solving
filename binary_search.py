def binarySearch(array, target):
    start = 0
    end = len(array) - 1
    def helper(start, end):
        if start == end:
            return -1
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            return helper(start, mid)
        elif array[mid] < target:
            return helper(mid + 1, end)
    return helper(start, end)

binarySearch([1, 5, 23, 111], 111)
