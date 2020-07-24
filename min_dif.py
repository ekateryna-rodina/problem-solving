# def smallestDifference(arrayOne, arrayTwo):
#     arrayOne = sorted(arrayOne)
#     arrayTwo = sorted(arrayTwo)
#     start_f, start_s = 0, 0
#     end_f, end_s = len(arrayOne), len(arrayTwo)
#     min_ = -1
#     min_f, min_s = None, None
#     while start_f < end_f and start_s < end_s:
#         abs_ = abs(arrayOne[start_f] - arrayTwo[start_s])
#         min_temp= min(min_, abs_)
#         if min_== -1 or min_temp == abs_:
#             min_ = abs_
#             min_f = arrayOne[start_f]
#             min_s = arrayTwo[start_s]
        
#         if min_temp == 0:
#             return [min_f, min_s]
        
#         # increment index of potentially smaller item 
#         if arrayOne[start_f] < arrayTwo[start_s]:
#             start_f += 1
#         else:
#             start_s += 1
#     res = [min_f, min_s]
#     return res

def smallestDifference(arrayOne, arrayTwo):
    arrayOne = sorted(arrayOne)
    arrayTwo = sorted(arrayTwo)
    start_f, start_s = 0, 0
    end_f, end_s = len(arrayOne), len(arrayTwo)
    min_ = -1
    min_f, min_s = None, None
    while start_f < end_f and start_s < end_s:
        abs_ = abs(arrayOne[start_f] - arrayTwo[start_s])
        min_temp= min(min_, abs_)
        if min_== -1 or min_temp == abs_:
            min_ = abs_
            min_f = arrayOne[start_f]
            min_s = arrayTwo[start_s]
        
        if min_temp == 0:
            return [min_f, min_s]
        
        # increment index of potentially smaller item 
        if arrayOne[start_f] < arrayTwo[start_s]:
            start_f += 1
        else:
            start_s += 1
    res = [min_f, min_s]
    return res


# Function to count total bits in a number 

def countTotalBits(num): 
	
	# convert number into it's binary and 
	# remove first two characters 0b. 
	binary = bin(num)[2:] 
	print(len(binary)) 

# Driver program 
if __name__ == "__main__": 
	num = 13
	countTotalBits(num) 




smallestDifference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17])

