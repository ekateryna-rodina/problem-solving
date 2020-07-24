def selectionSort(array):
    len_ = len(array)
    for all_ in range(len_):
        pivot = array[all_]
        min_i = all_
        for i in range(all_ + 1, len_):
            min_v = min(array[min_i], array[i])
            if min_v == array[i]:
                min_i = i
    # 		swap
        array[all_] = array[min_i]
        array[min_i] = pivot
    return array

selectionSort([8, 5, 2, 9, 5, 6, 3])