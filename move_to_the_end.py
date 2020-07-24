def moveElementToEnd(array, toMove):
	len_ = len(array)
	start, end = 0, len_ - 1
	while start != end:
		if array[end] == toMove:
			end -= 1
		else:
			if array[start] == toMove:
				array[start] = array[end]
				array[end] = toMove
			start += 1
			
	return array
moveElementToEnd([4, 1, 3, 2, 2, 4, 3, 2], 2)