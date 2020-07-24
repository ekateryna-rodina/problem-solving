def insertionSort(array):
    len_ = len(array)
    for i in range(len_):
        # comparable = array[i]
        range_to_insert = range(0, i + 1)
        for ii in range_to_insert[::-1]:
            comparable = array[ii]
            if ii == 0 or comparable >= array[ii - 1]:
                break
            
    # 				swap
            temp = array[ii - 1]
            array[ii - 1] = comparable
            array[ii] = temp
    return array

insertionSort([8, 5, 2, 9, 5, 6, 3])