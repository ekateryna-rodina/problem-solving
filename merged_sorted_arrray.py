# return a new sorted merged list from K sorted lists, each with size N
import heapq
# heap sort
def merge(list_):
    merged = []
    heap = [(l[0], i, 0) for i, l in enumerate(list_) if list_]
    heapq.heapify(heap)
    while heap:
        item, l_i, i_i = heapq.heappop(heap)
        merged.append(item)
        if i_i + 1 < len(list_[l_i]):
            next_item = (list_[l_i][i_i + 1], l_i, i_i + 1)
            heapq.heappush(heap, next_item)
    return merged

# merge sort
def merge_():
    merged = []
    
merge([[10, 15, 30], [12, 15, 20], [17, 20, 32]])
