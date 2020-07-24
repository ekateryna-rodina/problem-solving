def isMonotonic(array):
    if len(array) == 1 or len(array) == 0:
        return True
    count_iter = 0
    initial_trend = None
    while count_iter + 1 < len(array):
        if array[count_iter] != array[count_iter + 1]:
            current_trend = array[count_iter] < array[count_iter + 1]
            if initial_trend is None:
                initial_trend = current_trend
            following_trend = current_trend
            if initial_trend != following_trend:
                return False
        count_iter += 1
    return True

print(isMonotonic([1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 11]))