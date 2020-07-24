def sort_array(array, len_):
	for ind in range(len_):
		pivot = array[ind]
		min_i = ind
		for inn_ind in range(ind + 1, len_):
			min_ = min(array[min_i], array[inn_ind])
			if min_ == array[inn_ind]:
				min_i = inn_ind
		array[ind] = array[min_i]
		array[min_i] = pivot
	return array 

def threeNumberSum(array, targetSum):
#     sort array first
	result = []
	len_ = len(array)
	sorted_a = sort_array(array, len_)
	for i in range(len_):
		current = array[i]
		left_i = i + 1
		right_i = len_ - 1
		while left_i < len_ and right_i > i and right_i > left_i:
			if sum([current, array[left_i], array[right_i]]) == targetSum:
				result.append([current, array[left_i], array[right_i]])
				left_i += 1
				right_i -= 1
				# continue
				# break
			elif sum([current, array[left_i], array[right_i]]) > targetSum:
				right_i -= 1
			else:
				left_i += 1
	return result

er = threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0)
print(er)