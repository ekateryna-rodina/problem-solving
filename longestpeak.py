def peak_length(peak_i, array):
    peak = array[peak_i]
    count = 0
    def _peak(loc_peak_i, adj_i, is_left):
        nonlocal count
        if adj_i == -1 or adj_i == len(array):
            return count
        if array[loc_peak_i] <= array[adj_i]:
            return count
        count += 1
        if is_left:
            return _peak(adj_i, adj_i - 1, is_left)
        else:
            return _peak(adj_i, adj_i + 1, is_left)
    left_l = _peak(peak_i, peak_i - 1, True)
    count = 0
    right_l = _peak(peak_i, peak_i + 1, False)
    len_ =  left_l + right_l + 1
    return len_
    
def longestPeak(array):
    peaks_i = []
    max_length_peak = 0
    for i in range(len(array)):
        if i != 0 and i != len(array) - 1:
            # find all peaks
            if array[i] > array[i - 1] and array[i] > array[i + 1]:
                peaks_i.append(i)
    # how long the peaks
    for i in peaks_i:
        len_ = peak_length(i, array)
        max_length_peak = max(len_, max_length_peak)
    return max_length_peak
print(longestPeak([1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]))