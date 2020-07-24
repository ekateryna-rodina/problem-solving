def spiralTraverse(array):
    size = len(array[0])
    init_end_index = size - 1
    count_times = 0
    row_ = 0
    column_ = 0
    start_index, end_index = array[0][0], array[0][init_end_index]
    # 	the array is square shaped
    count_total = size**2
    current_step = 0
    true_false_matrix = [size*[False]]*size
    result = []
    while start_index < end_index:
        
        start = print(array[start_index])
        current_step = array[start_index][end_index]
        print(current_step)
        current_step += 12
        
spiralTraverse([[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]])
